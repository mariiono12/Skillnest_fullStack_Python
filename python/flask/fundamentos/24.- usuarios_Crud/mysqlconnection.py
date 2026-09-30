import pymysql.cursors

class MySQLConnection:
    """Administra la conexión entre Python y MySQL."""

    def __init__(self, db):
        self.connection = pymysql.connect(
            host="localhost",
            user="root",
            password="1234",  # <-- Modifica según tu contraseña local
            database=db,
            charset="utf8mb4",
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True
        )

    def query_db(self, query, data=None):
        """Ejecuta consultas SQL en la base de datos."""
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
                print("Something went wrong:")
                print(e)
                return False

            finally:
                self.connection.close()


def connectToMySQL(db):
    """Crea y devuelve una instancia de MySQLConnection."""
    return MySQLConnection(db)