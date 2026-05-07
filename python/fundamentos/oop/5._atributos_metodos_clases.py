# Atributos- Métodos de clase, Métodos estáticos

#DEFINICIÓN DE LA CLASE
class Estudiante:
    #Atributo de Clase
    colegio = "Liceo Vate Vicente Huidobro"
    #Lista en donde estén todos los estudiantes
    estudiantes = []

    #Método CONSTRUCTOR
    def __init__(self, nombre, nota):
        #Atributos de instancia
        self.nombre = nombre
        self.nota = nota

        #Agregar elementos a la lista Estudiante
        Estudiante.estudiantes.append(self)

    #Método de instancia
    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Nota: {self.nota}")

    #Método de CLASE
    # Usa "CLS" porque trabaja con la información de la clase
    @classmethod
    def cambiar_colegio(cls, nuevo_nombre):
        cls.colegio = nuevo_nombre

    @classmethod #Contar la cantidad de estudiantes existentes
    def cantidad_estudiantes(cls):
        return len(cls.estudiantes)
    
    #Método estático
    #Este no usa CLS ni SELF, solo parámetros.
    @staticmethod
    def aprobar(nota):
        if nota >= 4.0:
            return True
        else:
            return False
    
#Creación de Objetos (Instancias)
e1 = Estudiante("Donovan", 4.0)
e2 = Estudiante("Randy", 7.0)
e3 = Estudiante("Martin", 3.9)
#Uso de métodos de instancia
print("== MÉTODO DE INSTANCIA==")
#Mostrar datos de estudiantes
e1.mostrar_info()
print()
e2.mostrar_info()
print()
e3.mostrar_info()
print()

# Usar atributo de clase
print("=== ATRIBUTO DE CLASE===")
print(e1.colegio)
print(e2.colegio)
print()

#Uso de método de clase
print("=== MéTODO DE CLASE ===")

Estudiante.cambiar_colegio("Purkuyen")
e1.colegio = "VVH" ##Modifica elm atributo de la instancia en la clase
print(e1.colegio)
print(e2.colegio)
print()

#Contar Estudiantes
print("=== CONTAR ESTUDIANTES ===")
print(f"Total estudiantes: {Estudiante.cantidad_estudiantes()}")

#Método estático
print("=== MÉTODO ESTÁTICO ===")

print(f"¿{e1.nombre} aprueba?")
print(Estudiante.aprobar(e1.nota))
print()

print(f"¿{e2.nombre} aprueba?")
print(Estudiante.aprobar(e2.nota))
print()

print(f"¿{e3.nombre} aprueba?")
print(Estudiante.aprobar(e3.nota))
print()

## Función repaso.
## Crea una función que valide usuario y contraseña

def validador(user, password):
     if user == "matias123" and password == "matias123":
        print(f"Bienvenido, {user}!")
        return True
     else:
        print(f"Acceso Denegado")
        return False
    
def enviarDatos():
    username = input("Ingrese su nombre usuario: ")
    password = input("Ingrese su contraseña: ")
    validador = validador(username, password)

    enviarDatos() 