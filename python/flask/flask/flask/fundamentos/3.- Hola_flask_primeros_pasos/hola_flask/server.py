from flask import Flask

app = Flask(__name__)

@app.route("/")
def hola_mundo():
    return "¡Hola Mundo!"

@app.route("/nosotros")
def nosotros():
    return "¡conócenos un poco más!"

@app.route("/Anne")
def Anne():
    return "Tarea :3"

@app.route("/Eli")
def Eli():
    return "Ivan my BF"

if __name__ == "__main__":
    app.run(debug=True)