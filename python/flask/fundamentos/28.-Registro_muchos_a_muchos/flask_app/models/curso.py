from flask_app.config.mysqlconnection import connectToMySQL


class Curso:
    def __init__(self, data):
        self.id_curso = data["id_curso"]
        self.nombre_curso = data["nombre_curso"]
        self.descripcion = data["descripcion"]
        self.created_at = data["created_at"]

    @classmethod
    def get_all(cls):
        query = """
            SELECT id_curso, nombre_curso, descripcion, created_at
            FROM cursos
            ORDER BY nombre_curso;
        """
        resultados = connectToMySQL("esquema_educacion").query_db(query)
        cursos = []
        if resultados:
            for curso in resultados:
                cursos.append(cls(curso))
        return cursos