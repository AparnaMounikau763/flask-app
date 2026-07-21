from flask import Flask, jsonify
import socket
import datetime

app = Flask(__name__)

VERSION = "1.0.0"


@app.route("/")
def home():
    return jsonify(
        {
            "Application": "Python Flask CI/CD Demo",
            "Version": VERSION,
            "Hostname": socket.gethostname(),
            "Time": str(datetime.datetime.now())
        }
    )


@app.route("/health")
def health():
    return jsonify(
        {
            "status": "UP"
        }
    )


@app.route("/version")
def version():
    return jsonify(
        {
            "version": VERSION
        }
    )


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000
    )