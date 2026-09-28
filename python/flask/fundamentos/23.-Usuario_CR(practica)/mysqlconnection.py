import pymysql
import pymysql.cursors


class MySQLConnection:

    def __init__(self, db):
        connection = pymysql.connect(
            host="localhost",
            user="root",
            password="1234",
            database=db,
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True
        )

        self.connection = connection

    def query_db(self, query, data=None):
        cursor = self.connection.cursor()

        try:
            if data:
                cursor.execute(query, data)
            else:
                cursor.execute(query)

            if query.strip().lower().startswith("select"):
                result = cursor.fetchall()
            else:
                result = cursor.lastrowid

            return result

        except Exception as e:
            print("Something went wrong:", e)
            return False

        finally:
            cursor.close()
            self.connection.close()


def connectToMySQL(db):
    return MySQLConnection(db)