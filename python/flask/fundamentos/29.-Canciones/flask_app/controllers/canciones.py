from flask_app import app
from flask import render_template, request, redirect, url_for, flash
from flask_app.models.usuario import Usuario
from flask_app.models.cancion import Cancion
from flask_app.models.favorito import Favorito

@app.route("/")
def inicio():
    return redirect(url_for("usuarios"))

# --- RUTAS DE USUARIOS ---
@app.route("/usuarios")
def usuarios():
    todos_usuarios = Usuario.get_all()
    return render_template("usuarios.html", usuarios=todos_usuarios)

@app.route("/usuarios/crear", methods=["POST"])
def crear_usuario():
    data = {
        "nombre": request.form["nombre"],
        "email": request.form["email"],
        "contrasena": request.form["contrasena"]
    }
    Usuario.save(data)
    return redirect(url_for("usuarios"))

@app.route("/usuarios/<int:id>")
def mostrar_usuario(id):
    usuario = Usuario.get_by_id_with_favorites(id)
    if not usuario:
        return "Usuario no encontrado", 404
    canciones = Cancion.get_all()
    return render_template("mostrar_usuario.html", usuario=usuario, canciones=canciones)

# --- RUTAS DE CANCIONES ---
@app.route("/canciones")
def canciones():
    todas_canciones = Cancion.get_all()
    return render_template("canciones.html", canciones=todas_canciones)

@app.route("/canciones/crear", methods=["POST"])
def crear_cancion():
    data = {
        "titulo": request.form["titulo"],
        "artista": request.form["artista"]
    }
    Cancion.save(data)
    return redirect(url_for("canciones"))

@app.route("/canciones/<int:id>")
def mostrar_cancion(id):
    cancion = Cancion.get_by_id_with_users(id)
    if not cancion:
        return "Canción no encontrada", 404
    # BONUS: Solo obtener usuarios que no han agregado esta canción
    usuarios_disponibles = Cancion.get_users_not_favorited(id)
    return render_template("mostrar_cancion.html", cancion=cancion, usuarios=usuarios_disponibles)

# --- RUTA PARA AGREGAR FAVORITO ---
@app.route("/favoritos/agregar", methods=["POST"])
def agregar_favorito():
    usuario_id = request.form["usuario_id"]
    cancion_id = request.form["cancion_id"]
    origen = request.form["origen"]

    data = {
        "usuario_id": usuario_id,
        "cancion_id": cancion_id
    }

    if not Favorito.existe(data):
        Favorito.agregar(data)

    if origen == "usuario":
        return redirect(url_for("mostrar_usuario", id=usuario_id))
    elif origen == "cancion":
        return redirect(url_for("mostrar_cancion", id=cancion_id))
    
    return redirect(url_for("usuarios"))