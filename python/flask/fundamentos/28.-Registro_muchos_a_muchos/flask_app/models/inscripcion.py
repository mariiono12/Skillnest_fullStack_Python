from flask_app.config.mysqlconnection import connectToMySQL


class Inscripcion:

    @classmethod
    def inscribir_estudiante_en_curso(cls, datos):
        query = """
            INSERT INTO inscripciones (estudiante_id, curso_id)
            VALUES (%(estudiante_id)s, %(curso_id)s);
        """
        return connectToMySQL("esquema_educacion").query_db(query, datos)

    @classmethod
    def existe(cls, datos):
        query = """
            SELECT estudiante_id, curso_id
            FROM inscripciones
            WHERE estudiante_id = %(estudiante_id)s
              AND curso_id = %(curso_id)s;
        """
        resultado = connectToMySQL("esquema_educacion").query_db(query, datos)
        return bool(resultado)

    @classmethod
    def get_all(cls):
        query = """
            SELECT
                estudiantes.nombre AS estudiante,
                cursos.nombre_curso AS curso
            FROM inscripciones
            INNER JOIN estudiantes
                ON inscripciones.estudiante_id = estudiantes.id_estudiante
            INNER JOIN cursos
                ON inscripciones.curso_id = cursos.id_curso;
        """
        return connectToMySQL("esquema_educacion").query_db(query)