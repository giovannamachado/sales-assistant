import os

import requests
from dotenv import load_dotenv
from flask import Flask, jsonify, request

load_dotenv()
app = Flask(__name__)


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers',
                         'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods',
                         'GET,PUT,POST,DELETE,OPTIONS')
    return response


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


def call_groq_api(question):
    """Chama a API do Groq com fallback entre modelos"""
    if not GROQ_API_KEY:
        return None, "GROQ_API_KEY não configurada"

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    # Prompt especializado para assistente de vendas pet
    system_prompt = (
        "Você é um assistente de vendas especialista em produtos para pets. "
        "Responda de forma amigável e didática, explicando o básico em 4-5 linhas. "
        "Use emojis e organize as informações de forma clara. "
        "Dê recomendações práticas e específicas, mas explique o porquê. "
        "Seja educativo mas não muito extenso."
    )

    for model in AVAILABLE_MODELS:
        try:
            payload = {
                "model": model,
                "messages": [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": question}
                ],
                "max_tokens": 250,  # Permite explicações um pouco maiores
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
                # Outro erro
                return None, f"Erro {response.status_code}"

        except Exception:
            continue

    return None, "Nenhum modelo disponível"


@app.route("/api/question-and-answer", methods=['POST'])
def question_and_answer():
    """
    Endpoint principal do assistente de vendas
    Recebe uma pergunta e retorna a resposta da IA
    """
    # Valida Content-Type
    if not request.is_json:
        return jsonify({"error": "Content-Type deve ser application/json"}), 400

    # Obtém dados da requisição
    data = request.get_json()
    if not data or 'question' not in data:
        return jsonify({"error": "Campo 'question' é obrigatório"}), 400

    question = data['question']
    if not question or not question.strip():
        return jsonify({"error": "A pergunta não pode estar vazia"}), 400

    # Chama a API da IA
    response_text, error = call_groq_api(question.strip())

    if response_text:

        return jsonify({"response": response_text})
    else:
        return jsonify({"error": error}), 500


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
