class SuscripcionStreaming:
   costos_suscripcion = {"Gratis": 0, "Estándar": 5.99, "Premium": 10.99}
   
   def __init__(self, usuario, costo_mensual, saldo_pendiente ,tipo_suscripcion="Gratis",):
       self.usuario = usuario
       self.saldo_pendiente = saldo_pendiente
       self.tipo_suscripcion = tipo_suscripcion
       self.costo_mensual = costo_mensual
       pass

   def realizar_pago(self, monto):
       if monto < 0:
          print("Monto invalido")
       elif monto > self.saldo_pendiente:
           print("Monto excede al saldo pendiente")
       else:
           self.saldo_pendiente = monto
           print(f"Pago realizado. Saldo pendiente: {self.saldo_pendiente}")
       """Reduce el saldo pendiente según el monto pagado."""
       pass

   def cambiar_suscripcion(self, nuevo_tipo):
       if nuevo_tipo in self.costos_suscripcion:
           self.tipo_suscripcion = nuevo_tipo
           self.saldo_pendiente = self.costos_suscripcion[nuevo_tipo]
           print(f"Suscripción cambiada a {nuevo_tipo}")
       else:
        print("Tipo de suscripción inválido")
       """Cambia el tipo de suscripción y actualiza el costo mensual."""
       pass

   def ver_contenido_exclusivo(self):
        if self.tipo_suscripcion in ["Estándar", "Premium"]:
         print("Contenido exclusivo disponible")
        else:
         print("No tienes acceso a contenido exclusivo")
"""Permite ver contenido exclusivo según el tipo de suscripción."""
pass

def mostrar_info_suscripcion(self):
         print(f"Usuario: {self.usuario}")
         print(f"Tipo de suscripción: {self.tipo_suscripcion}")
         print(f"Costo mensual: {self.costos_suscripcion[self.tipo_suscripcion]}")
         print(f"Saldo pendiente: {self.saldo_pendiente}")
"""Muestra la información de la suscripción del usuario."""
pass  

