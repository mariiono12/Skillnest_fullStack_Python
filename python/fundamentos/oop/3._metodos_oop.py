class Usuario:
   def __init__(self, nombre, apellido, email):
       self.nombre = nombre
       self.apellido = apellido
       self.email = email
       self.limite_credito = 30000
       self.saldo_pagar = 0

   def hacer_compra(self, monto):  #recibe como argumento el monto de la compra
       self.saldo_pagar += monto   #el saldo a pagar del usuario aumenta en la cantidad del valor recibido

   def aumentarCredito(self, aumento):
       self.limite_credito += aumento
   def cambiarCorreo(self, cambiarCorreo):
        self.email = cambiarCorreo
#Instancias de la clase
miyagi = Usuario("Nariyoshi", "Miyagi", "miyagi@codingdojo.la")
daniel = Usuario("Daniel", "Larusso", "daniel@codingdojo.la")

print("---------------Compras de Miyagi----------------")
miyagi.hacer_compra(2000)
print(f"Primera compra de {miyagi.nombre}: ${miyagi.saldo_pagar}")
segundacompra = 300
miyagi.hacer_compra(segundacompra)
print(f"Segunda compra: ${segundacompra}")
#Imprimir cuanto credito le queda a Miyagi
print(f"Credito disponible ${miyagi.limite_credito - miyagi.saldo_pagar}")

#Compras de Daniel 2 compras y muestra saldo a pagar
print("---------------Compras de Daniel----------------")
daniel.hacer_compra(45)
print(f"Primera compra de {daniel.nombre}: ${daniel.saldo_pagar}")
segundacompra = 300
miyagi.hacer_compra(segundacompra)
print(f"Segunda compra: ${segundacompra}")
#Imprimir cuanto credito le queda a Miyagi
print(f"Credito disponible ${daniel.limite_credito - daniel.saldo_pagar}")
print(daniel.saldo_pagar) #Imprime: 45

#Tarea
'''
1.-Crear un nuevo método que permita aumentar el limite de crédito.
Imprimir el nuevo límite de crédito

2.-Crear un método que permite cambiar el correo de la instancia.
Mostrar el nuevo correo.
'''
miyagi.aumentarCredito(2000)
print(f"El nuevo crédito de {miyagi.nombre} es: {miyagi.limite_credito}")

miyagi.cambiarCorreo("miyagilpolon@gmail.com")
print(f"El nuevo correo es: {miyagi.email}")
