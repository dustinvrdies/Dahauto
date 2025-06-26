from flask import Flask, render_template, jsonify
from bot_engine import run_faucet_bot

app = Flask(__name__)

logs = []

@app.route("/")
def home():
    return render_template("index.html", logs=logs)

@app.route("/run", methods=["POST"])
def run_bot():
    logs.clear()
    for log in run_faucet_bot():
        logs.append(log)
    return jsonify({"logs": logs})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
