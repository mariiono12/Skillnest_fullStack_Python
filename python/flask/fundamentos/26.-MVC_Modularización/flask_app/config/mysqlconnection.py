import pymysql.cursors

class MySQLConnection:
    """Administra una conexión con MySQL."""

    def __init__(self, db):
        self.connection = pymysql.connect(
            host="localhost",
            user="root",
            password="1234",  # <-- Cambia 'root' por tu contraseña local
            database=db,
            charset="utf8mb4",
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True
        )

    def query_db(self, query, data=None):
        """Ejecuta una consulta SQL."""
        with self.connection.cursor() as cursor:
            try:
                query_debug = cursor.mogrify(query, data)
                print("Running Query:", query_debug)

                cursor.execute(query, data)

                if query.lower().find("insert") >= 0:
                    self.connection.commit()
                    return cursor.lastrowid

                elif query.lower().find("select") >= 0:
                    return cursor.fetchall()

                else:
                    self.connection.commit()

            except Exception as e:
                print("Something went wrong:", e)
                return False

            finally:
                self.connection.close()


def connectToMySQL(db):
    return MySQLConnection(db)