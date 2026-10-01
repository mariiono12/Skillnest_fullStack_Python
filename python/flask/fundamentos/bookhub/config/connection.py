import pymysql
import os
from dotenv import load_dotenv

load_dotenv()

class MySQLConnection:
    def __init__(self, db):
        connection = pymysql.connect(
            host=os.getenv('MYSQL_HOST', 'localhost'),
            user=os.getenv('MYSQL_USER', 'root'),
            password=os.getenv('MYSQL_PASSWORD', ''),
            db=db,
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True
        )
        self.connection = connection

    def query_db(self, query, data=None):
        with self.connection.cursor() as cursor:
            try:
                # Se ejecuta directamente pasándole la consulta y el diccionario de datos
                cursor.execute(query, data)
                
                query_lower = query.strip().lower()
                if query_lower.startswith("insert"):
                    return cursor.lastrowid
                elif query_lower.startswith("select"):
                    return cursor.fetchall()
                else:
                    return cursor.rowcount
            except Exception as e:
                print("Ocurrió un error en la BD:", e)
                return False

def connectToMySQL(db=None):
    if db is None:
        db = os.getenv('MYSQL_DB', 'bookhub_db')
    return MySQLConnection(db)