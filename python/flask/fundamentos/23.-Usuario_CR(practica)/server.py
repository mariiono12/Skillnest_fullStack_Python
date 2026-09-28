from flask import Flask, render_template, request, redirect, url_for
from usuario import Usuario

app = Flask(__name__)


@app.route("/usuarios")
def usuarios():
    usuarios = Usuario.get_all()
    return render_template("usuarios.html", usuarios=usuarios)


@app.route("/usuarios/nuevo")
def nuevo_usuario():
    return render_template("usuario_nuevo.html")


@app.route("/usuarios/crear", methods=["POST"])
def crear_usuario():
    nombre = request.form["nombre"].strip()
    apellido = request.form["apellido"].strip()
    email = request.form["email"].strip()

    if not nombre or not apellido or not email:
        return render_template(
            "usuario_nuevo.html",
            error="Todos los campos son obligatorios."
        )

    usuario = Usuario(
        nombre=nombre,
        apellido=apellido,
        email=email
    )

    Usuario.save(usuario)

    return redirect(url_for("usuarios"))


if __name__ == "__main__":
    app.run(debug=True)