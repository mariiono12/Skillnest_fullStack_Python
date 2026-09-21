from mysqlconnection import connectToMySQL

class Mascota:
    def __init__(self, data):
        self.id = data["id"]
        self.nombre = data["nombre"]
        self.tipo = data["tipo"]
        self.color = data["color"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    # ======================================================
    # ACTIVIDAD DE CONSOLIDACIÓN: Buscar por Nombre
    # ======================================================
    @classmethod
    def get_by_name(cls, nombre):
        """
        Busca una mascota por nombre usando sentencias preparadas.
        Retorna un objeto Mascota o None si no la encuentra.
        """
        query = """
            SELECT *
            FROM mascotas
            WHERE nombre = %(nombre_mascota)s;
        """
        
        data = {
            "nombre_mascota": nombre
        }

        resultados = connectToMySQL("primera_flask").query_db(query, data)

        if resultados:
            return cls(resultados[0])

        return None

    # ======================================================
    # DESAFÍO: Obtener todas las mascotas por Tipo
    # ======================================================
    @classmethod
    def get_by_tipo(cls, tipo):
        """
        Retorna una lista de objetos Mascota según el tipo recibido.
        """
        query = """
            SELECT *
            FROM mascotas
            WHERE tipo = %(tipo_mascota)s;
        """
        
        data = {
            "tipo_mascota": tipo
        }

        resultados = connectToMySQL("primera_flask").query_db(query, data)

        mascotas = []
        if resultados:
            for mascota in resultados:
                mascotas.append(cls(mascota))

        return mascotas