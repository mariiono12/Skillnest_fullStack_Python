from conexion import Conexion

class usuario: 
    def __init__(self, nombre_usuario, contrasena, tipo_usuario):
        self.nombre_usuario = nombre_usuario
        self.contrasena = contrasena
        self.tipo_usuario = tipo_usuario
        
        @classmethod
        def validad_inicio_sesion(cls, username, contrasena):
            obj_con = Conexion()
            db = obj_con.conectar()
            cursor = db.cursor()

        sql = "SELECT * FROM usuarios WHERE usuario = %s AND contrasena = %s AND deleted = 0"
        cursor.execute(sql, (username, contrasena))
        resultado = cursor.fetchone()

        obj_con.cerrar