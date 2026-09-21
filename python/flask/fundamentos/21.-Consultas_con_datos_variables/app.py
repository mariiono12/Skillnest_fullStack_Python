from flask import Flask, render_template
from mascota import Mascota

app = Flask(__name__)

# ==========================================================
# RUTA ACTIVIDAD: Buscar por nombre
# ==========================================================
@app.route("/mascota/nombre/<string:nombre>")
def buscar_mascota_por_nombre(nombre):
    """
    Ejemplo de URL: http://127.0.0.1:5000/mascota/nombre/Firulais
    """
    mascota = Mascota.get_by_name(nombre)

    if mascota is None:
        return f"No se encontró ninguna mascota llamada '{nombre}'", 404

    return render_template("mascota.html", mascota=mascota)


# ==========================================================
# RUTA DESAFÍO: Buscar por tipo
# ==========================================================
@app.route("/mascotas/tipo/<string:tipo>")
def buscar_mascotas_por_tipo(tipo):
    """
    Ejemplo de URL: http://127.0.0.1:5000/mascotas/tipo/Perro
    """
    mascotas = Mascota.get_by_tipo(tipo)

    return render_template("index.html", mascotas=mascotas)


if __name__ == "__main__":
    app.run(debug=True)