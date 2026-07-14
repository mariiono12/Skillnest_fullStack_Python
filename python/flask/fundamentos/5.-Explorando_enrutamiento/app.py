from flask import Flask
app = Flask(__name__)

# CORREGIDO: Se agregó la barra diagonal antes de 'inicio'
@app.route("/inicio")
def inicio():
    return "WENA soy el sesho"

@app.route("/explorar")
def explorar():
    return "Estas explorando el enrutamiento que tiene flask :°"

@app.route("/saludo/<nombre>")
def saludo_personalizado(nombre):
    return f"¡Wena, {nombre}! Bienvenido a esto T_T "

@app.route("/repetir/<string:mensaje>/<int:veces>")
def repetir_mensaje(mensaje, veces):
    # CORREGIDO: Cambiado de "- ".join a " ".join para evitar errores de sintaxis en la multiplicación
    resultado = " ".join([mensaje] * veces)
    return resultado

@app.errorhandler(404)
def pagina_no_encontrada(error):
    return (
        "Chuta, esta ruta parece que no existe...",
        404,
    )

if __name__ == "__main__":
    app.run(debug=True)