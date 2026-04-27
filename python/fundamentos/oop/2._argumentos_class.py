#➡️ Pasar argumentos 
#Para poder personalizar nuestras instancia vamos a pasar 
#algunos argumentos al método __init__ y que de esta manera 
#podamos asignarle a los atributos los valores correspondientes.
class Usuario:
   def __init__(self, nombre, apellido, email, limite_credito, saldo_pagar):
       self.nombre = nombre
       self.apellido = apellido
       self.email = email
       self.limite_credito = limite_credito
       self.saldo_pagar = saldo_pagar
#Creación de instancias
miyagi = Usuario("Nariyoshi", "Miyagi", "miyagi@codingdojo.la", 10000, 0)
daniel = Usuario("Daniel", "Larusso", "daniel@codingdojo.la", 50000, 20000)
ian = Usuario("ian", "Bustos", "ian@codingdojo.la", 4, 2)
#Imprimimos valores
print(miyagi.nombre) #Imprime: Nariyoshi
print(daniel.nombre) #Imprime: Daniel

#-----------------------------
#--- Tarea rápida
'''
Crear una clase Estudiante, y asignarle los siguientes atributos:
(rut, nombre, apellido, especialidad, fecha_nacimiento)
Crear 3 instancias para la clase con distintos estudiantes
Imprimir el nombre y apellido concatenado + especialidad.
'''

class Estudiante: 
    def __init__(self, rut, nombre, apellido, especialidad, fecha_nacimiento):
        self.rut = rut
        self.nombre = nombre
        self.apellido = apellido
        self.especialidad = especialidad
        self.fecha_nacimiento = fecha_nacimiento

nigari = Estudiante(22756332-4, "nigari",  "tanaka", "Programation" , 10/4/2007)
mario = Estudiante(22776224-4, "mario",  "bustos","Contability" , 20/2/2009)
yan = Estudiante(22756224-4, "yan",  "lefiqueo", "Programation" ,  10/3/2008)

print(nigari.nombre + " " + nigari.apellido + " " + nigari.especialidad) 
print(mario.nombre + " " + mario.apellido + " " + mario.especialidad) 
print(yan.nombre + " " + yan.apellido + " " + yan.especialidad)
