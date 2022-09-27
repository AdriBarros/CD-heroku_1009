import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Olá Isaías! Tudo bem com você? Esta é apenas o início de uma aprendizagem para em um futuro não muito distante eu aprender a desenvolver APIs"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
