from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def health_check():
    return jsonify({"status": "API rodando"}), 200

if __name__ == '__main__':
    app.run(debug=True)