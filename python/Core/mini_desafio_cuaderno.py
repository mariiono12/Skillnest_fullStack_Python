datos = [
   {"nombre": "Carlos", "puntaje": 80},
   {"nombre": "María", "puntaje": 95},
   {"nombre": "Pedro", "puntaje": 70}
]


datos[2]["puntaje"] = 75


def mostrar():
    print(datos[0]["nombre"] + " obtuvo " + str(datos[0]["puntaje"]) + " puntos")


def ver(campo):
    for x in datos:
        print(x[campo])

# probando
mostrar()
ver("nombre")
ver("puntaje")