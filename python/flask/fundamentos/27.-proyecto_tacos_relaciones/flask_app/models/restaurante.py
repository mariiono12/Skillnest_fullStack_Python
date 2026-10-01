from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.taco import Taco

class Restaurante:

    def __init__(self, data):
        self.id = data["id"]
        self.nombre = data["nombre"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.tacos = []

    @classmethod
    def save(cls, datos):
        """CREATE: Crea un nuevo restaurante."""
        query = """
            INSERT INTO restaurantes (nombre)
            VALUES (%(nombre)s);
        """
        return connectToMySQL("esquema_tacos").query_db(query, datos)

    @classmethod
    def get_all(cls):
        """READ: Obtiene todos los restaurantes."""
        query = """
            SELECT id, nombre, created_at, updated_at
            FROM restaurantes
            ORDER BY id;
        """
        resultados = connectToMySQL("esquema_tacos").query_db(query)
        restaurantes = []
        if resultados:
            for restaurante in resultados:
                restaurantes.append(cls(restaurante))
        return restaurantes

    @classmethod
    def get_restaurante_y_tacos(cls, datos):
        """READ: Obtiene un restaurante junto a la lista de objetos Taco relacionados (JOIN)."""
        query = """
            SELECT
                restaurantes.id AS restaurante_id,
                restaurantes.nombre AS restaurante_nombre,
                restaurantes.created_at AS restaurante_created_at,
                restaurantes.updated_at AS restaurante_updated_at,
                tacos.id AS taco_id,
                tacos.tortilla AS taco_tortilla,
                tacos.guiso AS taco_guiso,
                tacos.salsa AS taco_salsa,
                tacos.restaurante_id AS taco_restaurante_id,
                tacos.created_at AS taco_created_at,
                tacos.updated_at AS taco_updated_at
            FROM restaurantes
            LEFT JOIN tacos ON tacos.restaurante_id = restaurantes.id
            WHERE restaurantes.id = %(id)s;
        """
        resultados = connectToMySQL("esquema_tacos").query_db(query, datos)

        if not resultados:
            return None

        restaurante_data = {
            "id": resultados[0]["restaurante_id"],
            "nombre": resultados[0]["restaurante_nombre"],
            "created_at": resultados[0]["restaurante_created_at"],
            "updated_at": resultados[0]["restaurante_updated_at"]
        }

        restaurante = cls(restaurante_data)

        for fila in resultados:
            if fila["taco_id"] is not None:
                datos_taco = {
                    "id": fila["taco_id"],
                    "tortilla": fila["taco_tortilla"],
                    "guiso": fila["taco_guiso"],
                    "salsa": fila["taco_salsa"],
                    "restaurante_id": fila["taco_restaurante_id"],
                    "created_at": fila["taco_created_at"],
                    "updated_at": fila["taco_updated_at"]
                }
                restaurante.tacos.append(Taco(datos_taco))

        return restaurante