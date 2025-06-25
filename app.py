from flask import Flask, render_template, jsonify, request
from ai_scraper import find_faucets
from claim_engine import claim_from_faucets, sign_up_to_all

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/run", methods=["POST"])
def run_autobread():
    faucets = find_faucets()
    creds = sign_up_to_all(faucets)
    results = claim_from_faucets(faucets, creds)
    return jsonify({"claimed": results})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
