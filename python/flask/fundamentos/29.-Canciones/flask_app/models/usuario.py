from flask_app.config.mysqlconnection import connectToMySQL

class Usuario:
    def __init__(self, data):
        self.id = data["id"]
        self.nombre = data["nombre"]
        self.email = data["email"]
        self.contrasena = data["contrasena"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.favoritos = []

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM usuarios ORDER BY nombre ASC;"
        resultados = connectToMySQL("esquema_canciones").query_db(query)
        usuarios = []
        if resultados:
            for u in resultados:
                usuarios.append(cls(u))
        return usuarios

    @classmethod
    def save(cls, data):
        query = "INSERT INTO usuarios (nombre, email, contrasena) VALUES (%(nombre)s, %(email)s, %(contrasena)s);"
        return connectToMySQL("esquema_canciones").query_db(query, data)

    @classmethod
    def get_by_id(cls, id):
        query = "SELECT * FROM usuarios WHERE id = %(id)s;"
        resultado = connectToMySQL("esquema_canciones").query_db(query, {"id": id})
        if resultado:
            return cls(resultado[0])
        return None

    @classmethod
    def get_by_id_with_favorites(cls, id):
        query = """
            SELECT usuarios.*, canciones.id AS cancion_id, canciones.titulo, canciones.artista
            FROM usuarios
            LEFT JOIN favoritos ON favoritos.usuario_id = usuarios.id
            LEFT JOIN canciones ON favoritos.cancion_id = canciones.id
            WHERE usuarios.id = %(id)s;
        """
        resultados = connectToMySQL("esquema_canciones").query_db(query, {"id": id})
        if not resultados:
            return None
        
        usuario = cls(resultados[0])
        for fila in resultados:
            if fila["cancion_id"] is not None:
                usuario.favoritos.append({
                    "id": fila["cancion_id"],
                    "titulo": fila["titulo"],
                    "artista": fila["artista"]
                })
        return usuario