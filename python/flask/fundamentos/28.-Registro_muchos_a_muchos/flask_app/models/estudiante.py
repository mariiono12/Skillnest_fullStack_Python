from flask_app.config.mysqlconnection import connectToMySQL


class Estudiante:
    def __init__(self, data):
        self.id_estudiante = data["id_estudiante"]
        self.nombre = data["nombre"]
        self.email = data["email"]
        self.created_at = data["created_at"]

    @classmethod
    def delete(cls, id_estudiante):
            query = """
            DELETE FROM estudiantes
            WHERE id_estudiante = %(id_estudiante)s;
            """
            data = {"id_estudiante": id_estudiante}
            return connectToMySQL("esquema_educacion").query_db(query, data)


    @classmethod
    def get_all(cls):
        query = """
            SELECT id_estudiante, nombre, email, created_at
            FROM estudiantes
            ORDER BY nombre;
        """
        resultados = connectToMySQL("esquema_educacion").query_db(query)
        estudiantes = []
        if resultados:
            for estudiante in resultados:
                estudiantes.append(cls(estudiante))
        return estudiantes

        