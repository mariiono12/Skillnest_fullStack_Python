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
        print(f"{titulo} agregado")

    def ver_contenido(self, titulo):
        if titulo in self.lista_reproduccion:
            print(f"Reproduciendo {titulo}")
        else:
            print(f"{titulo} no esta en tu lista")

    def cambiar_suscripcion(self, nueva_suscripcion):
        vieja = self.suscripcion
        self.suscripcion = nueva_suscripcion
        print(f"Suscripcion cambio de {vieja} a {nueva_suscripcion}")

    def mostrar_info_usuario(self):
        print(f"Nombre: {self.nombre}")
        print(f"Email: {self.email}")
        print(f"Suscripcion: {self.suscripcion}")
        print(f"Mi lista: {self.lista_reproduccion if self.lista_reproduccion else 'Vacia'}")



print("Crear 3 usuarios")

u1 = UsuarioStreaming(input("Usuario 1 - Nombre: "), input("Email: "), input("Suscripcion (Gratis/Estandar/Premium): "))
u2 = UsuarioStreaming(input("Usuario 2 - Nombre: "), input("Email: "), input("Suscripcion: "))
u3 = UsuarioStreaming(input("Usuario 3 - Nombre: "), input("Email: "), input("Suscripcion: "))

# Usuario 1
print(f"{u1.nombre}")
u1.agregar_a_lista(input("Titulo 1: "))
u1.agregar_a_lista(input("Titulo 2: "))
u1.ver_contenido(input("Que quieres ver?: "))
u1.ver_contenido(input("Que mas quieres ver?: "))
u1.mostrar_info_usuario()

# Usuario 2
print(f"{u2.nombre}")
u2.agregar_a_lista(input("Titulo: "))
u2.ver_contenido(input("Que quieres ver?: "))
u2.cambiar_suscripcion(input("Nueva suscripcion: "))
u2.mostrar_info_usuario()

# Usuario 3
print(f"{u3.nombre}")
u3.agregar_a_lista(input("Titulo 1: "))
u3.agregar_a_lista(input("Titulo 2: "))
u3.agregar_a_lista(input("Titulo 3: "))
u3.ver_contenido(input("Primer contenido a ver: "))
u3.ver_contenido(input("Segundo contenido: "))
u3.ver_contenido(input("Tercer contenido: "))
u3.cambiar_suscripcion(input("Primer cambio de suscripcion: "))
u3.cambiar_suscripcion(input("Segundo cambio: "))
u3.mostrar_info_usuario()