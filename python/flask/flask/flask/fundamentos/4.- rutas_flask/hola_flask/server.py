from flask import Flask

app = Flask(__name__)

@app.route("/")
def hola_mundo():
    return "¡Hola Mundo!"

@app.route("/Papamericano")
def Mamammericana():
    return "<h2>paralelepipedo<h2> <h3>la mi la mi la mi la mía no cose bien<h3>"

@app.route("/saludo/<nombre>")
def saludo(nombre):
    return f"¡Hola {nombre}!"

@app.route("/color/<nombre>/<color>")
def color_favorito(nombre, color):
    return f"Hola {nombre}, tu color favorito es {color}"

@app.route("/saludo/<nombre>/<int:veces>")
def repetir(nombre, veces):
    return f"¡Hola {nombre}!" * veces

@app.route("/despedida/<nombre>")
def despedida(nombre):
    return f"¡Hasta mañana {nombre}, te extrañaré!"

@app.route("/presentacion/<nombre>/<int:edad>")
def presentación(nombre, edad):
    return f"{nombre}, tienes {edad} años"

if __name__ == "__main__":
    app.run(debug=True)