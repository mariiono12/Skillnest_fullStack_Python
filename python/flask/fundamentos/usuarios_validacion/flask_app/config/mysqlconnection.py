import pymysql.cursors

class MySQLConnection:
    def __init__(self, db):
        self.connection = pymysql.connect(
            host="localhost",
            user="root",        -- Modifica si usas un usuario diferente en tu MySQL
            password="",        -- Modifica si tu MySQL tiene contraseña
            database=db,
            charset="utf8mb4",
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True
        )

    def query_db(self, query, data=None):
        with self.connection.cursor() as cursor:
            try:
                cursor.execute(query, data)
                tipo_consulta = query.strip().lower()

                if tipo_consulta.startswith("select"):
                    return cursor.fetchall()
                if tipo_consulta.startswith("insert"):
                    return cursor.lastrowid
                return cursor.rowcount

            except Exception as e:
                print("Error en MySQL:", e)
                return False
            finally:
                self.connection.close()

def connectToMySQL(db):
    return MySQLConnection(db)