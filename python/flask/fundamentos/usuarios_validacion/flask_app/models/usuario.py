import re
from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL

# Expresión regular para validar el formato del e-mail
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')

class Usuario:
    def __init__(self, data):
        self.id = data["id"]
        self.nombre = data["nombre"]
        self.apellido = data["apellido"]
        self.email = data["email"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @staticmethod
    def validar_usuario(usuario):
        es_valido = True

        # Validar campos vacíos
        if not usuario["nombre"].strip():
            flash("El nombre es obligatorio.", "danger")
            es_valido = False

        if not usuario["apellido"].strip():
            flash("El apellido es obligatorio.", "danger")
            es_valido = False

        if not usuario["email"].strip():
            flash("El e-mail es obligatorio.", "danger")
            es_valido = False
        # Validar formato de e-mail
        elif not EMAIL_REGEX.match(usuario["email"].strip()):
            flash("E-mail inválido.", "danger")
            es_valido = False

        return es_valido

    @classmethod
    def email_existe(cls, email):
        # BONUS: Validar si el e-mail ya existe en la base de datos
        query = "SELECT id FROM usuarios WHERE email = %(email)s;"
        resultados = connectToMySQL("esquema_usuarios").query_db(query, {"email": email})
        return bool(resultados)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM usuarios ORDER BY id DESC;"
        resultados = connectToMySQL("esquema_usuarios").query_db(query)
        usuarios = []
        if resultados:
            for usuario in resultados:
                usuarios.append(cls(usuario))
        return usuarios

    @classmethod
    def save(cls, data):
        query = """
            INSERT INTO usuarios (nombre, apellido, email)
            VALUES (%(nombre)s, %(apellido)s, %(email)s);
        """
        return connectToMySQL("esquema_usuarios").query_db(query, data)