from flask import Flask, render_template
from mascota import Mascota

app = Flask(__name__)

# ==========================================================
# RUTA PRINCIPAL
# ==========================================================
@app.route("/")
def index():
    mascotas = Mascota.get_all()
    return render_template("index.html", mascotas=mascotas)

# ==========================================================
# RUTA: BUSCAR POR ID
# ==========================================================
@app.route("/mascota/<int:id>")
def mostrar_mascota(id):
    mascota = Mascota.get_by_id(id)

    if mascota is None:
        return "Mascota no encontrada", 404

    return render_template("mascota.html", mascota=mascota)

# ==========================================================
# RUTA ACTIVIDAD: BUSCAR POR NOMBRE
# ==========================================================
@app.route("/mascota/nombre/<string:nombre>")
def buscar_por_nombre(nombre):
    mascota = Mascota.get_by_name(nombre)

    if mascota is None:
        return f"No se encontró ninguna mascota llamada '{nombre}'", 404

    return render_template("mascota.html", mascota=mascota)

# ==========================================================
# RUTA DESAFÍO: FILTRAR POR TIPO
# ==========================================================
@app.route("/mascotas/tipo/<string:tipo>")
def buscar_por_tipo(tipo):
    mascotas = Mascota.get_by_tipo(tipo)
    return render_template("index.html", mascotas=mascotas)

# ==========================================================
# ARRANQUE DEL SERVIDOR
# ==========================================================
if __name__ == "__main__":
    app.run(debug=True)