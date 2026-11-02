from flask_app import app
from flask import render_template, request, redirect, url_for, session, flash
from flask_app.models.usuario import Usuario

@app.route("/")
def inicio():
    return redirect(url_for("usuarios"))

@app.route("/usuarios")
def usuarios():
    todos_los_usuarios = Usuario.get_all()
    return render_template("usuarios.html", usuarios=todos_los_usuarios)

@app.route("/usuarios/nuevo")
def nuevo_usuario():
    # BONUS: Recuperar datos guardados temporalmente en session (si los hay)
    datos_formulario = session.pop("datos_formulario", {})
    return render_template("nuevo_usuario.html", datos=datos_formulario)

@app.route("/usuarios/crear", methods=["POST"])
def crear_usuario():
    data = {
        "nombre": request.form.get("nombre", "").strip(),
        "apellido": request.form.get("apellido", "").strip(),
        "email": request.form.get("email", "").strip()
    }

    # 1. Validación de campos y formato de correo
    if not Usuario.validar_usuario(data):
        session["datos_formulario"] = data  # Mantener los datos ingresados
        return redirect(url_for("nuevo_usuario"))

    # 2. BONUS: Validación de correo único en base de datos
    if Usuario.email_existe(data["email"]):
        flash("El e-mail ingresado ya se encuentra registrado.", "danger")
        session["datos_formulario"] = data  # Mantener los datos ingresados
        return redirect(url_for("nuevo_usuario"))

    # 3. Guardar en Base de Datos
    resultado = Usuario.save(data)

    if resultado is False:
        flash("No fue posible guardar el usuario.", "danger")
        session["datos_formulario"] = data
        return redirect(url_for("nuevo_usuario"))

    # Éxito: Limpiar sesión y redirigir
    session.pop("datos_formulario", None)
    flash("Usuario creado correctamente.", "success")
    return redirect(url_for("usuarios"))