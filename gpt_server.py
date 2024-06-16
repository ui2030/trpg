from flask import Flask, request, jsonify
import openai
import os
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__)

# Use ProxyFix to handle reverse proxy headers
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_port=1, x_prefix=1)

# Set the OpenAI API key from environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    prompt = data.get("prompt")
    if prompt:
        response = openai.Completion.create(
            model="gpt-4o",  # gpt-4o 모델 사용
            prompt=prompt,
            max_tokens=150
        )
        return jsonify(response.choices[0].text.strip())
    return jsonify({"error": "No prompt provided"}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)