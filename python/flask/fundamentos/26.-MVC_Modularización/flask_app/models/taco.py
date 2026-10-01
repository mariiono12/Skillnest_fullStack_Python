from flask_app.config.mysqlconnection import connectToMySQL

class Taco:

    def __init__(self, data):
        self.id = data["id"]
        self.tortilla = data["tortilla"]
        self.guiso = data["guiso"]
        self.salsa = data["salsa"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def save(cls, datos):
        """CREATE: Inserta un nuevo taco."""
        query = """
            INSERT INTO tacos (tortilla, guiso, salsa)
            VALUES (%(tortilla)s, %(guiso)s, %(salsa)s);
        """
        return connectToMySQL("esquema_tacos").query_db(query, datos)

    @classmethod
    def get_all(cls):
        """READ: Obtiene todos los tacos."""
        query = """
            SELECT id, tortilla, guiso, salsa, created_at, updated_at
            FROM tacos
            ORDER BY id;
        """
        tacos_en_bd = connectToMySQL("esquema_tacos").query_db(query)
        tacos = []
        if tacos_en_bd:
            for taco in tacos_en_bd:
                tacos.append(cls(taco))
        return tacos

    @classmethod
    def get_one(cls, datos):
        """READ: Obtiene un taco por ID."""
        query = """
            SELECT id, tortilla, guiso, salsa, created_at, updated_at
            FROM tacos
            WHERE id = %(id)s;
        """
        taco_en_db = connectToMySQL("esquema_tacos").query_db(query, datos)
        if not taco_en_db:
            return None
        return cls(taco_en_db[0])

    @classmethod
    def update(cls, datos):
        """UPDATE: Actualiza un taco existente."""
        query = """
            UPDATE tacos
            SET
                tortilla = %(tortilla)s,
                guiso = %(guiso)s,
                salsa = %(salsa)s
            WHERE id = %(id)s;
        """
        return connectToMySQL("esquema_tacos").query_db(query, datos)

    @classmethod
    def delete(cls, datos):
        """DELETE: Elimina un taco por ID."""
        query = """
            DELETE FROM tacos
            WHERE id = %(id)s;
        """
        return connectToMySQL("esquema_tacos").query_db(query, datos)