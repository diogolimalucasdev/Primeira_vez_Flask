from flask import Flask

app = Flask(__name__)


@app.route("/<int:numero>/<int:numero2>", methods=['GET', 'POST'])
def ola(numero, numero2):
    return 'Olá mundo. {} {} '.format(numero, numero2)


if __name__ == "__main__":  # so vai ser executado se a camada vier desse proprio modulo run.py
    app.run(debug=True)  # restart a aplicação automaticamente sem que eu tenha que ficar dar Run
