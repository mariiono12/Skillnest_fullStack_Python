import os
def limpiar_consola():
    os.system('cls')

class SuscripcionStreaming:
    costos_suscripcion = {"Gratis": 0, "Estándar": 5000, "Premium": 10000}
    
    # metodo constructor
    def __init__(self, usuario, saldo_pendiente, tipo_suscripcion="Gratis", puede_ver = True):
        self.usuario = usuario
        self.saldo_pendiente = saldo_pendiente
        self.tipo_suscripcion = tipo_suscripcion
        self.puede_ver = puede_ver
        self.costo_mensual = self.costos_suscripcion[tipo_suscripcion] # <-- Importante

    def realizar_pago(self, monto):
        if self.tipo_suscripcion == "Gratis":
                print(f"Que quieres pagar si tu suscripcion es gratis?!")
                print(f"Tu sueldo: ${monto} fue recuperado...")
        
        if self.saldo_pendiente == 0 or monto >= self.costo_mensual:
            print(f"Muchas gracias por mantenerte en nuestra plataforma!!")
            self.puede_ver = True
        elif monto < self.costo_mensual:
            print(f"Pagaste: ${monto} pero debes de pagar: ${self.costo_mensual} minimo...")
            self.puede_ver = False
            self.saldo_pendiente -= monto
    
    def cambiar_suscripcion(self, nuevo_tipo):
        self.tipo_suscripcion = nuevo_tipo
        self.costo_mensual = self.costos_suscripcion[nuevo_tipo]

    def ver_contenido_exclusivo(self):
        if self.tipo_suscripcion != "Gratis" and self.puede_ver:
            print("Por favor disfruta de nuestro contenido exclusivo como tu quieras!!")
        elif not self.puede_ver:
            print(f"Lo sentimos pero debes de pagar tu suscripcion...")
        elif self.tipo_suscripcion == "Gratis":
            print(f"Lo sentimos tu suscripcion es de tipo {self.tipo_suscripcion}")

    def mostrar_info_suscripcion(self):
        print(f"\nuser ⧽ {self.usuario}")
        print(f"tipo de suscripcion ⧽ {self.tipo_suscripcion}")
        print(f"costo mensual ⧽ ${self.costo_mensual}")
        print(f"saldo pendiente ⧽ ${self.saldo_pendiente}")

def ejercicio_1():
    inp = int(input("Por favor ingresar monto a pagar:\n"))
    if inp != "":
        usuarios[user - 1].realizar_pago(inp)

def ejercicio_2():
    sus = input("Por favor ingresar nueva suscripción:\n")
    if sus != "":
        usuarios[user - 1].cambiar_suscripcion(sus)


user1 = SuscripcionStreaming("Isidora", 27000, "Estándar")
user2 = SuscripcionStreaming("Martin", 0,)
user3 = SuscripcionStreaming("Sergio", 300000, "Premium")

usuarios = [user1, user2, user3]

print("Hello again, what you wanna do today?!")
sueño = True


user = int(input("Podrias ingresar tu llave de usuario por favor?(1-3):_"))
while sueño:
    print("1-. Pagar")
    print("2-. Cambiar suscripción")
    print("3-. Contenido exclusivo")
    print("4-. Info")
    print("0-. Salir")
    
    hacer = int(input("Por favor ingresar actividad:_"))
    if hacer == 1:
        limpiar_consola()
        ejercicio_1()
    elif hacer == 2:
        limpiar_consola()
        ejercicio_2()
    elif hacer == 3:
        limpiar_consola()
        usuarios[user - 1].ver_contenido_exclusivo()
    elif hacer == 4:
        limpiar_consola()
        usuarios[user - 1].mostrar_info_suscripcion()
    elif hacer == 0:
        limpiar_consola()
        print("^._.^ฅ")
        sueño = False
    else:
        print("Opción no válida")