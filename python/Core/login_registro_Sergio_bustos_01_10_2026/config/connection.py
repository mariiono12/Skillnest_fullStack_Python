import pymysql

class MySQLConnection:
    def __init__(self, db):
        connection = pymysql.connect(
            host='localhost',
            user='root',
            password='1234',  # Agrega tu contraseña de MySQL si la utilizas
            db=db,
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True
        )
        self.connection = connection

    def query_db(self, query, data=None):
        with self.connection.cursor() as cursor:
            try:
                cursor.execute(query, data)
                query_lower = query.strip().lower()
                if query_lower.startswith("insert"):
                    return cursor.lastrowid
                elif query_lower.startswith("select"):
                    return cursor.fetchall()
                else:
                    return cursor.rowcount
            except Exception as e:
                print("Error en BD:", e)
                return False

def connectToMySQL(db='login_registro_db'):
    return MySQLConnection(db)