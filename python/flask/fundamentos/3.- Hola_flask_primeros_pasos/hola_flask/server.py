from flask import Flask

app = Flask(__name__)

@app.route("/")
def hola_mundo():
    return "¡Hola Mundo!"

@app.route("/nosotros")
def nosotros():
    return "¡conócenos un poco más!"

@app.route("/eli")
def eli():
    return "Proyecto jejejej"

@app.route("/isi")
def isi():
    return "Recursos jijiji"

if __name__ == "__main__":
    app.run(debug=True)