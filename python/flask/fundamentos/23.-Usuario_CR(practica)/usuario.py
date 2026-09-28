from mysqlconnection import connectToMySQL


class Usuario:

    def __init__(
        self,
        id=None,
        nombre="",
        apellido="",
        email="",
        created_at=None,
        updated_at=None
    ):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.created_at = created_at
        self.updated_at = updated_at

    @classmethod
    def get_all(cls):
        query = """
            SELECT
                id,
                nombre,
                apellido,
                email,
                created_at,
                updated_at
            FROM usuarios
            ORDER BY id DESC;
        """

        resultados = connectToMySQL("esquema_usuarios").query_db(query)

        usuarios = []

        for usuario in resultados:
            usuarios.append(
                cls(
                    id=usuario["id"],
                    nombre=usuario["nombre"],
                    apellido=usuario["apellido"],
                    email=usuario["email"],
                    created_at=usuario["created_at"],
                    updated_at=usuario["updated_at"]
                )
            )

        return usuarios

    @classmethod
    def save(cls, usuario):
        query = """
            INSERT INTO usuarios
                (nombre, apellido, email, created_at, updated_at)
            VALUES
                (%(nombre)s, %(apellido)s, %(email)s, NOW(), NOW());
        """

        data = {
            "nombre": usuario.nombre,
            "apellido": usuario.apellido,
            "email": usuario.email
        }

        return connectToMySQL("esquema_usuarios").query_db(query, data)