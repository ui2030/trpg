from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid JSON"}), 400
    prompt = data.get("prompt")
    if prompt:
        response = openai.Completion.create(
            engine="davinci",
            prompt=prompt,
            max_tokens=150
        )
        return jsonify({"response": response.choices[0].text.strip()})
    return jsonify({"error": "No prompt provided"}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)