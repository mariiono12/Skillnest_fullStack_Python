import pymysql.cursors

class MySQLConnection:
    """Administra la conexión entre Python y MySQL."""

    def __init__(self, db):
        self.connection = pymysql.connect(
            host="localhost",
            user="root",          # Modifica si tu usuario es distinto
            password="1234",      # Modifica si tu contraseña es distinta
            database=db,
            charset="utf8mb4",
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True
        )

    def query_db(self, query, data=None):
        """Ejecuta una consulta SQL y retorna el resultado correspondiente."""
        with self.connection.cursor() as cursor:
            try:
                cursor.execute(query, data)

                if query.strip().lower().startswith("select"):
                    resultados = cursor.fetchall()
                    return resultados

                elif query.strip().lower().startswith("insert"):
                    return cursor.lastrowid

                else:
                    return None

            except Exception as e:
                print("Ocurrió un error al ejecutar la consulta:")
                print(e)
                return False

            finally:
                self.connection.close()


def connectToMySQL(db):
    """Crea y devuelve una instancia de MySQLConnection."""
    return MySQLConnection(db)