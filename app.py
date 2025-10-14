from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def health_check():
    return jsonify({"status": "API rodando"}), 200

@app.route("/api/question-and-answer", methods=['POST'])
def question_and_answer():
    data = request.get_json()
    if not data or 'question' not in data:
        return jsonify({"error": "Falta 'question' no corpo da requisição"}), 400

    question = data['question']

    # Resposta mockada por enquanto
    mock_response = f"Sua pergunta foi: '{question}'. A resposta da IA virá em breve."

    return jsonify({"response": mock_response})

if __name__ == '__main__':
    app.run(debug=True)