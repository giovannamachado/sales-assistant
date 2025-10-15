import os

import requests
from dotenv import load_dotenv
from flask import Flask, jsonify, request

load_dotenv()
app = Flask(__name__)

# Configuração
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"

# Modelos disponíveis (em ordem de preferência)
AVAILABLE_MODELS = [
    "llama-3.3-70b-versatile",
    "llama3-groq-70b-8192-tool-use-preview",
    "llama3-groq-8b-8192-tool-use-preview",
    "llama-3.1-8b-instant",
    "gemma2-9b-it",
    "gemma-7b-it"
]

# Prompt padrão para o assistente
ASSISTANT_PROMPT = (
    "Você é um assistente de vendas especialista em produtos para pets (cães e gatos) "
    "de um e-commerce como a Petlove. Responda de forma amigável, profissional e concisa."
)


def validate_request_data(data):
    """Valida os dados da requisição"""
    if not data:
        return "Corpo da requisição vazio ou inválido"

    if 'question' not in data:
        return "Campo 'question' é obrigatório"

    question = data['question']
    if not question or not question.strip():
        return "A pergunta não pode estar vazia"

    return None


def call_groq_api(question):
    """Chama a API do Groq com fallback entre modelos"""
    if not GROQ_API_KEY:
        return None, "GROQ_API_KEY não configurada"

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    for model in AVAILABLE_MODELS:
        try:
            payload = {
                "model": model,
                "messages": [
                    {"role": "system", "content": ASSISTANT_PROMPT},
                    {"role": "user", "content": question}
                ],
                "max_tokens": 500,
                "temperature": 0.7
            }

            response = requests.post(
                GROQ_URL, headers=headers, json=payload, timeout=30)

            if response.status_code == 200:
                result = response.json()
                return result['choices'][0]['message']['content'], None
            elif response.status_code == 400:
                # Modelo descontinuado, tenta o próximo
                continue
            else:
                # Outro erro, para aqui
                error_detail = response.json() if response.headers.get(
                    'content-type') == 'application/json' else response.text
                return None, f"Erro {response.status_code}: {error_detail}"

        except requests.RequestException as e:
            continue
        except Exception as e:
            continue

    return None, "Nenhum modelo disponível no momento"

# Routes


@app.route("/", methods=['GET'])
def health_check():
    """Health check da API"""
    return jsonify({
        "status": "API rodando",
        "version": "1.0.0",
        "groq_configured": bool(GROQ_API_KEY),
        "endpoints": [
            "GET /",
            "POST /api/question-and-answer",
            "POST /api/ask"
        ]
    })


@app.route("/api/question-and-answer", methods=['POST'])
def question_and_answer():
    """Endpoint principal - retorna resposta estruturada"""
    if not request.is_json:
        return jsonify({"error": "Content-Type deve ser application/json"}), 400

    validation_error = validate_request_data(request.get_json())
    if validation_error:
        return jsonify({"error": validation_error}), 400

    question = request.get_json()['question'].strip()
    response, error = call_groq_api(question)

    if response:
        return jsonify({
            "question": question,
            "response": response,
            "api_used": "groq"
        })
    else:
        return jsonify({"error": error}), 503


@app.route("/api/ask", methods=['POST'])
def ask_simple():
    """Endpoint simplificado - retorna apenas texto"""
    if not request.is_json:
        return "Content-Type deve ser application/json", 400

    validation_error = validate_request_data(request.get_json())
    if validation_error:
        return validation_error, 400

    question = request.get_json()['question'].strip()
    response, error = call_groq_api(question)

    if response:
        return response, 200, {'Content-Type': 'text/plain; charset=utf-8'}
    else:
        return f"Erro: {error}", 503




@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "error": "Endpoint não encontrado",
        "available_endpoints": [
            "GET /",
            "POST /api/question-and-answer",
            "POST /api/ask"
        ]
    }), 404


@app.errorhandler(405)
def method_not_allowed(error):
    return jsonify({
        "error": "Método não permitido",
        "allowed_methods": ["GET", "POST"]
    }), 405


if __name__ == '__main__':
    print("Sales Assistant API")
    print("http://localhost:5000")
    print("POST /api/question-and-answer")
    print("Powered by Groq AI")

    app.run(debug=True, host='0.0.0.0', port=5000)
