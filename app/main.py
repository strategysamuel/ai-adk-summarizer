from flask import Flask, request, jsonify, render_template
from app.agent_runner import run_agent

app = Flask(__name__)

# 🔥 UI route
@app.route("/")
def home():
    return render_template("index.html")

# API route
@app.route("/summarize", methods=["POST"])
def summarize():
    data = request.get_json()

    if not data or "text" not in data:
        return jsonify({"error": "Missing 'text' field"}), 400

    result = run_agent(data["text"])

    return jsonify({
        "input": data["text"],
        "summary": result
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)