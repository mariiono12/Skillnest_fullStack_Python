from flask import flask, render_template

app = flask(__name__)

@app.route("/")
def inicio():

    return render_template(
        "index.html",
        nombre="Sergio",
        curso = "Desarrollo Web con Flask",
        ciudad = "Santiago",
        anio = 2026,
        profesor =False,
        tecnologias=[
        "Python",
        "Flask",
        "HTML",
        "CSS"
    ])

@app.route ("/jugador")
def jugador():
    return render_template(jugador.html,
    jugador="CyberWarrior",

    puntaje=9200,

    lider=True)



if __name__ == "__main__":

    app.run(debug=True)