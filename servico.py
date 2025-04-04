from flask import Flask

servico = Flask(__name__)

@servico.route("/info")
def get_info():
    return "Teste de serviço web"

if __name__ == "__main__":
    servico.run(host="0.0.0.0", port=5000)