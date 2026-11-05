import re
from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')

class Usuario:
    def __init__(self, data):
        self.id = data["id"]
        self.nombre = data["nombre"]
        self.apellido = data["apellido"]
        self.email = data["email"]
        self.password = data["password"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @staticmethod
    def validar_usuario(datos):
        es_valido = True

        if not datos["nombre"].strip() or len(datos["nombre"].strip()) < 2:
            flash("El nombre debe tener al menos 2 caracteres.", "registro")
            es_valido = False

        if not datos["apellido"].strip() or len(datos["apellido"].strip()) < 2:
            flash("El apellido debe tener al menos 2 caracteres.", "registro")
            es_valido = False

        if not datos["email"].strip() or not EMAIL_REGEX.match(datos["email"].strip()):
            flash("El e-mail no tiene un formato válido.", "registro")
            es_valido = False

        if not datos["password"] or len(datos["password"]) < 8:
            flash("La contraseña debe tener al menos 8 caracteres.", "registro")
            es_valido = False

        return es_valido

    @classmethod
    def guardar(cls, datos):
        query = """
            INSERT INTO usuarios (nombre, apellido, email, password)
            VALUES (%(nombre)s, %(apellido)s, %(email)s, %(password)s);
        """
        return connectToMySQL("esquema_loginreg").query_db(query, datos)

    @classmethod
    def buscar_por_email(cls, datos):
        query = "SELECT * FROM usuarios WHERE email = %(email)s;"
        resultados = connectToMySQL("esquema_loginreg").query_db(query, datos)
        if resultados and len(resultados) == 1:
            return cls(resultados[0])
        return False

    @classmethod
    def buscar_por_id(cls, datos):
        query = "SELECT * FROM usuarios WHERE id = %(id)s;"
        resultados = connectToMySQL("esquema_loginreg").query_db(query, datos)
        if resultados and len(resultados) == 1:
            return cls(resultados[0])
        return False

    @classmethod
    def existe_email(cls, datos):
        query = "SELECT id FROM usuarios WHERE email = %(email)s;"
        resultados = connectToMySQL("esquema_loginreg").query_db(query, datos)
        return len(resultados) > 0