from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Customer API v1"

@app.route("/health")
def health():
    return "OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
#if __name__ == "__main__":
#    raise Exception("Intentional failure for SRE troubleshooting lab")
