from flask_app import app
from flask import render_template, request, redirect, url_for, flash
from flask_app.models.usuario import Usuario
from flask_app.models.seguidor import Seguidor

@app.route("/")
def inicio():
    return redirect(url_for("usuarios"))

@app.route("/usuarios")
def usuarios():
    lista_usuarios = Usuario.get_all()
    relaciones = Seguidor.get_all()
    return render_template("usuarios.html", usuarios=lista_usuarios, relaciones=relaciones)

@app.route("/usuarios/crear", methods=["POST"])
def crear_usuario():
    nombre = request.form.get("nombre", "").strip()
    apellido = request.form.get("apellido", "").strip()
    email = request.form.get("email", "").strip()

    if not nombre or not apellido or not email:
        flash("Todos los campos son obligatorios.", "danger")
        return redirect(url_for("usuarios"))

    data = {"nombre": nombre, "apellido": apellido, "email": email}
    Usuario.save(data)
    flash("Usuario creado exitosamente.", "success")
    return redirect(url_for("usuarios"))

@app.route("/seguir", methods=["POST"])
def seguir():
    usuario_id = request.form.get("usuario_id")
    seguidor_id = request.form.get("seguidor_id")

    if not usuario_id or not seguidor_id:
        flash("Debe seleccionar ambos usuarios.", "danger")
        return redirect(url_for("usuarios"))

    if usuario_id == seguidor_id:
        flash("Un usuario no puede seguirse a sí mismo.", "warning")
        return redirect(url_for("usuarios"))

    data = {"usuario_id": usuario_id, "seguidor_id": seguidor_id}

    # BONUS: Evitar relaciones duplicadas
    if Seguidor.existe(data):
        flash("Esta relación de seguimiento ya existe.", "warning")
        return redirect(url_for("usuarios"))

    Seguidor.seguir(data)
    flash("Seguidor registrado exitosamente.", "success")
    return redirect(url_for("usuarios"))