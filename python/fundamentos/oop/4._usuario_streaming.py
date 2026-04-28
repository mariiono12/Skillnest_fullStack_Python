#Crea un archivo de Python llamado usuario_streaming.py.
#Atributos:
#nombre
#email
#suscripcion (Gratis, Estándar o Premium)
#lista_reproduccion (lista de títulos agregados por el usuario).
#Métodos:
#agregar_a_lista(self, titulo) agrega un contenido a la lista de reproducción.
#ver_contenido(self, titulo) simula que el usuario reproduce un contenido.
#cambiar_suscripcion(self, nueva_suscripcion) modifica el tipo de suscripción del usuario.
#mostrar_info_usuario(self) muestra los datos del usuario y su lista de reproducción.
#🧪 Realizar las siguientes pruebas con instancias:
#Crea 3 usuarios de la plataforma de streaming.
#Haz que el primer usuario agregue dos títulos a su lista y los vea.
#Haz que el segundo usuario agregue un título, lo vea y cambie su suscripción.
#Haz que el tercer usuario agregue tres títulos, los vea y cambie su suscripción dos veces.

class UsuarioStreaming:
   def __init__(self, nombre, email, suscripcion="Gratis"):
       self.nombre = nombre
       self.email = email
       self.suscripcion = suscripcion
       self.lista_reproduccion = []


def agregar_a_lista(self, titulo):
       self.lista_reproduccion.append(titulo)
       input(f"Titulo '{titulo}' agregado")
       """Agrega un contenido a la lista de reproducción del usuario."""
       pass


def ver_contenido(self, titulo):
       print(f"reproduciendo: {titulo} ")
       """Simula que el usuario reproduce un contenido."""
       pass


def cambiar_suscripcion(self, nueva_suscripcion):
       self.suscripcion = nueva_suscripcion
       print(f"Suscripcion cambiada a: {nueva_suscripcion}")
       """Cambia el tipo de suscripción del usuario."""
       pass


def mostrar_info_usuario(self):
       print(f"Usuario: {self.nombre} {self.email} {self.suscripcion}")
       print(f"Lista: {self.lista_reproduccion}")
       """Muestra la información del usuario y su lista de reproducción."""
       pass
   
   #Todos los valores que se deban registrar debe ser con input
   #Añadir un menu while para llamar a los métodos. 
   #(Menú de selección)

Usuarios = []
for i in range(3):
      print(f"Registro de usuario {i+1}")
      nombre = input("Nombre: ")
      correo = input("Email: ")
      plan = input("Suscripción (Gratis, Estándar, Premium): ")

      Usuarios.append(UsuarioStreaming(nombre, correo, plan))
      

u1 = UsuarioStreaming(input("Nombre U1: "), input("Email U1: "), input("Suscripción: "))
u2 = UsuarioStreaming(input("Nombre U2: "), input("Email U2: "), input("Suscripción: "))
u3 = UsuarioStreaming(input("Nombre U3: "), input("Email U3: "), input("Suscripción: "))


print(f"{u1.nombre}")
u1.agregar_a_lista(input("título para agregar: "))
u1.ver_contenido(input("Título a ver: "))
u1.ver_contenido(input("Otro título a ver: "))

print(f"{u2.nombre}")
u2.agregar_a_lista(input("Título para agregar: "))
u2.ver_contenido(input("Título a ver: "))
u2.cambiar_suscripcion(input("Nueva suscripción: "))

print(f"{u3.nombre}")
u3.agregar_a_lista(input("Título 1 para agregar: "))

u3.ver_contenido(input("Ver título 1: "))

u3.cambiar_suscripcion(input("Primer cambio de suscripción: "))
u3.cambiar_suscripcion(input("Segundo cambio de suscripción: "))

u1.mostrar_info_usuario()
u2.mostrar_info_usuario()
u3.mostrar_info_usuario()