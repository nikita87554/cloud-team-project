"""Учебное веб-приложение «Каталог облачных сервисов» (Flask)."""
import os
import json
from flask import Flask, jsonify

app = Flask(__name__)

DATA_FILE = os.getenv("DATA_FILE", os.path.join(os.path.dirname(__file__), "data", "services.json"))


def load_services():
    with open(DATA_FILE, encoding="utf-8") as f:
        return json.load(f)


@app.route("/")
def index():
    return jsonify({"project": "Cloud Team Project", "status": "ok"})


@app.route("/health")
def health():
    return jsonify({"status": "healthy"})


@app.route("/services")
def services():
    return jsonify(load_services())


if __name__ == "__main__":
    port = int(os.getenv("APP_PORT", "5000"))
    app.run(host="0.0.0.0", port=port)
