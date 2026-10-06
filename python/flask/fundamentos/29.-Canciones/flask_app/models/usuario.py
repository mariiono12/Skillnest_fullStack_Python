from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import cancion

class Usuario:
    db = "esquema_canciones"

    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.favoritos = []  # Lista de canciones favoritas del usuario

    @classmethod
    def guardar(cls, data):
        query = """
            INSERT INTO usuarios (nombre, created_at, updated_at) 
            VALUES (%(nombre)s, NOW(), NOW());
        """
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def obtener_todos(cls):
        query = "SELECT * FROM usuarios;"
        resultados = connectToMySQL(cls.db).query_db(query)
        
        # Validamos que resultados no sea False ni None
        if not resultados:
            return []

        usuarios = []
        for fila in resultados:
            usuarios.append(cls(fila))
        return usuarios

    # Alias por si en tu controlador llamas a get_all()
    @classmethod
    def get_all(cls):
        return cls.obtener_todos()

    @classmethod
    def obtener_con_canciones(cls, data):
        query = """
            SELECT * FROM usuarios 
            LEFT JOIN favoritos ON usuarios.id = favoritos.usuario_id 
            LEFT JOIN canciones ON canciones.id = favoritos.cancion_id 
            WHERE usuarios.id = %(id)s;
        """
        resultados = connectToMySQL(cls.db).query_db(query, data)
        
        if not resultados:
            return None

        usuario_obj = cls(resultados[0])
        for fila in resultados:
            if fila['canciones.id'] is not None:
                cancion_data = {
                    'id': fila['canciones.id'],
                    'titulo': fila['titulo'],
                    'artista': fila['artista'],
                    'created_at': fila['canciones.created_at'],
                    'updated_at': fila['canciones.updated_at']
                }
                usuario_obj.favoritos.append(cancion.Cancion(cancion_data))
        return usuario_obj

    @classmethod
    def agregar_favorito(cls, data):
        query = """
            INSERT INTO favoritos (usuario_id, cancion_id) 
            VALUES (%(usuario_id)s, %(cancion_id)s);
        """
        return connectToMySQL(cls.db).query_db(query, data)