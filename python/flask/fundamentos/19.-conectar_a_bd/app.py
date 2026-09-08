from flask import Flask, render_template
from mascota import Mascota

app = Flask(__name__)

@app.route("/")
def index():
    mascotas = Mascota.get_all()
    return render_template("index.html", mascotas=mascotas)

# ESTAS DOS LÍNEAS SON LAS QUE MANTIENEN EL SERVIDOR ENCENDIDO:
if __name__ == "__main__":
    app.run(debug=True)