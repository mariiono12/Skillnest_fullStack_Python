import pymysql.cursors

class MySQLConnection:
    """Administra la conexión entre Python y MySQL."""

    def __init__(self, db):
        self.connection = pymysql.connect(
            host="localhost",
            user="root",
            password="1234",  # <-- Cambia según tu clave
            database=db,
            charset="utf8mb4",
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True
        )

    def query_db(self, query, data=None):
        """Ejecuta una consulta SQL."""
        with self.connection.cursor() as cursor:
            try:
                cursor.execute(query, data)

                if query.strip().lower().startswith("select"):
                    return cursor.fetchall()

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
    return MySQLConnection(db)