from mysqlconnection import connectToMySQL

class Mascota:
    def __init__(self, data):
        self.id = data["id"]
        self.nombre = data["nombre"]
        self.tipo = data["tipo"]
        self.color = data["color"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def get_all(cls):
        """
        Recupera todas las mascotas de la base de datos.
        """
        query = "SELECT * FROM mascotas;"
        resultados = connectToMySQL("primera_flask").query_db(query)

        mascotas = []
        if resultados:
            for mascota in resultados:
                mascotas.append(cls(mascota))

        return mascotas

    @classmethod
    def get_by_type(cls, data):
        """
        Recupera mascotas filtrando por el tipo recibido en el parámetro data.
        """
        query = "SELECT * FROM mascotas WHERE tipo = %(tipo)s;"
        resultados = connectToMySQL("primera_flask").query_db(query, data)

        mascotas = []
        if resultados:
            for mascota in resultados:
                mascotas.append(cls(mascota))

        return mascotas