from flask import Flask, render_template
from mascota import Mascota

app = Flask(__name__)

@app.route("/")
def index():
    """
    Ruta principal: Obtiene y muestra todas las mascotas.
    """
    mascotas = Mascota.get_all()
    return render_template("index.html", todas_mascotas=mascotas)

@app.route("/mascotas/perros")
def solo_perros():
    """
    Ruta desafío: Obtiene y muestra únicamente mascotas de tipo 'Perro'.
    """
    data = {"tipo": "Perro"}
    perros = Mascota.get_by_type(data)
    return render_template("index.html", todas_mascotas=perros)

if __name__ == "__main__":
    app.run(debug=True)