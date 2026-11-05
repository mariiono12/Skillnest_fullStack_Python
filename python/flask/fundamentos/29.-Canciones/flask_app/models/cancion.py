from flask_app.config.mysqlconnection import connectToMySQL

class Cancion:
    def __init__(self, data):
        self.id = data["id"]
        self.titulo = data["titulo"]
        self.artista = data["artista"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.usuarios = []

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM canciones ORDER BY titulo ASC;"
        resultados = connectToMySQL("esquema_canciones").query_db(query)
        canciones = []
        if resultados:
            for c in resultados:
                canciones.append(cls(c))
        return canciones

    @classmethod
    def save(cls, data):
        query = "INSERT INTO canciones (titulo, artista) VALUES (%(titulo)s, %(artista)s);"
        return connectToMySQL("esquema_canciones").query_db(query, data)

    @classmethod
    def get_by_id(cls, id):
        query = "SELECT * FROM canciones WHERE id = %(id)s;"
        resultado = connectToMySQL("esquema_canciones").query_db(query, {"id": id})
        if resultado:
            return cls(resultado[0])
        return None

    @classmethod
    def get_by_id_with_users(cls, id):
        query = """
            SELECT canciones.*, usuarios.id AS usuario_id, usuarios.nombre, usuarios.email
            FROM canciones
            LEFT JOIN favoritos ON favoritos.cancion_id = canciones.id
            LEFT JOIN usuarios ON favoritos.usuario_id = usuarios.id
            WHERE canciones.id = %(id)s;
        """
        resultados = connectToMySQL("esquema_canciones").query_db(query, {"id": id})
        if not resultados:
            return None

        cancion = cls(resultados[0])
        for fila in resultados:
            if fila["usuario_id"] is not None:
                cancion.usuarios.append({
                    "id": fila["usuario_id"],
                    "nombre": fila["nombre"],
                    "email": fila["email"]
                })
        return cancion

    @classmethod
    def get_users_not_favorited(cls, cancion_id):
        # Cumple el BONUS: obtiene solo los usuarios que NO han agregado esta canción a favoritos
        query = """
            SELECT usuarios.* FROM usuarios
            LEFT JOIN favoritos ON favoritos.usuario_id = usuarios.id AND favoritos.cancion_id = %(cancion_id)s
            WHERE favoritos.usuario_id IS NULL;
        """
        return connectToMySQL("esquema_canciones").query_db(query, {"cancion_id": cancion_id})