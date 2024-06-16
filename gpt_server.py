from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

# Set the OpenAI API key from environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No JSON payload provided"}), 400

    prompt = data.get("prompt")
    if prompt:
        response = openai.ChatCompletion.create(
            model="gpt-4o-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=150
        )
        return jsonify(response.choices[0].message["content"].strip())
    return jsonify({"error": "No prompt provided"}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)