from flask import Flask, render_template, jsonify
from bot_engine.run_faucet_bot import run_faucet_bot

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/start")
def start_bot():
    result = run_faucet_bot()
    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
