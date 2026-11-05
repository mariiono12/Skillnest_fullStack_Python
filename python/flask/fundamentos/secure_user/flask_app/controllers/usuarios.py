from flask import render_template, redirect, request, session, flash
from flask_app import app, bcrypt
from flask_app.models.usuario import Usuario

@app.route("/")
def index():
    return render_template("login.html")

@app.route("/registro")
def registro():
    return render_template("registro.html")

@app.route("/registrar", methods=["POST"])
def registrar():
    datos = {
        "nombre": request.form.get("nombre", "").strip(),
        "apellido": request.form.get("apellido", "").strip(),
        "email": request.form.get("email", "").strip().lower(),
        "password": request.form.get("password", "")
    }

    # 1. Validar formulario
    if not Usuario.validar_usuario(datos):
        return redirect("/registro")

    # 2. Validar que el email sea único
    if Usuario.existe_email({"email": datos["email"]}):
        flash("El email ya se encuentra registrado.", "registro")
        return redirect("/registro")

    # 3. Hashear la contraseña con Bcrypt
    password_hash = bcrypt.generate_password_hash(datos["password"]).decode("utf-8")
    datos["password"] = password_hash

    # 4. Guardar usuario en BD y obtener su ID
    usuario_id = Usuario.guardar(datos)
    if not usuario_id:
        flash("Error al registrar el usuario.", "registro")
        return redirect("/registro")

    # 5. Guardar ID en sesión e ingresar al dashboard
    session["usuario_id"] = usuario_id
    return redirect("/dashboard")

@app.route("/login", methods=["POST"])
def login():
    datos = {
        "email": request.form.get("email", "").strip().lower(),
        "password": request.form.get("password", "")
    }

    # 1. Buscar usuario por email
    usuario = Usuario.buscar_por_email({"email": datos["email"]})
    if not usuario:
        flash("Email o contraseña incorrectos.", "login")
        return redirect("/")

    # 2. Comparar contraseña ingresada con el Hash de Bcrypt
    if not bcrypt.check_password_hash(usuario.password, datos["password"]):
        flash("Email o contraseña incorrectos.", "login")
        return redirect("/")

    # 3. Guardar ID en sesión
    session["usuario_id"] = usuario.id
    return redirect("/dashboard")

@app.route("/dashboard")
def dashboard():
    if "usuario_id" not in session:
        flash("Debes iniciar sesión para acceder.", "login")
        return redirect("/")

    usuario = Usuario.buscar_por_id({"id": session["usuario_id"]})
    return render_template("dashboard.html", usuario=usuario)

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")