# EJERCICIOS
"""1.-Crear una función que reciba una lista de números enterosy muestre cuál es el número
mayor y cuál es el menor."""
def listaNum(listado):
    menor = min(listado)
    mayor = max(listado)


def ejercicio1():
    limit = int(input("Ingresa un límite de valores: "))
    listNum = []
    i = 1
    while i <= limit:
        num = int(input(f"Ingresa un número entero {i} de {limit}: "))
        listNum.append(num)
        i += 1
    listaNum(listaNum)

"""2.-Crear una función que reciba una cadena de texto y cuente cuántas vocales contiene."""
def es_vocal(letra):
    vocales = "aeiuoAEIOU"
    return letra in vocales #Devuelve True si la letra está dentro de las vocales, si
   
def contar_vocales(texto):
    contador = 0

    for letra in texto:
        if es_vocal(letra):
            contador += 1
    print(f"La cadena contiene {contador} vocales.")

def ejercicio_contar_vocales():
    texto = input("Ingrese el texto: ")



"""3.-Crear una función que reciba una lista de nombres y muestre únicamente aquellos que
tengan más de 5 letras."""
def filtrar(lista):
    resultado = []
    for nombre in lista: 
        if len(nombre) > 5:
            resultado.append(nombre)
            return resultado
        
        def mostrar():
            nombres = []
            nombresLargos = []
            cantidad = int(input("¿Cuánto nombres quieres ingresar?"))

            for i in range(cantidad):
                nombre = input("Ingrese un nombre: ")
                print(f"{nombre} agregado con exito a la lista.")
                nombres.append(nombre)

            for nombre in filtrar(nombres):
                listaNombre = filtrar(nombres)
                print(f"Los nombres con más de 5 letras son: (.join{nombresLargos}) ") 
    mostrar()
"""4.-Crear una función que reciba una lista de notas (números decimales), calcule el promedio
e indique si el estudiante aprueba (promedio mayor o igual a 4.0)."""
def listaNotas(notas):
    lista = 0
    promedio = 0
    for i in range(len(notas)):
        lista += notas[i]
        promedio = lista / (len(notas))

    if promedio >= 4.0 and promedio <= 7.0:
        return f"El estudiante aprueba con {promedio}"
    elif promedio >= 1.0 and promedio <= 3.9:
        return f"El estudiante no aprueba con {promedio}"
    else: 
        return"Error"   

    def ejercicio4():
            largo = int(input("Cuantas notas va ingresar: "))
            nota = []
    for i in range(largo):
        inp = float(input(f"Ingrese nota {i + 1}: "))
    if inp != "":
            nota.append(inp)
            print(listaNotas(nota))

"""5.-Crear una función que reciba una lista de precios de productos y aplique un descuento del
10%, mostrando el valor original y el nuevo valor."""
def descuenta(valor):
    sumaLista = sum(valor)
    precioInicial = sumaLista
    descuento = sumaLista * 0.1
    precioFinal = precioInicial - descuento
    print(f"El precio inicial del producto es: {precioInicial} y con descuento {precioFinal}")

    def valores():
        cantidadProductos = int(input("Ingrese la cantidad de productos que quiera: "))
        listaPrecios = []
        for i in range(cantidadProductos):
            valorProducto = float(input("Ingrese el valor del producto: "))
            listaPrecios.append(valorProducto)
        descuento(listaPrecios)
        valores()

"""6.-Crear una función que reciba un número entero y determine si es par o impar."""
def parImpar(numero):
    if numero % 2 == 0:
        print(f"El número {numero} es Par")
    elif numero % 3 ==0:
        print(f"El número {numero} es Impar.")
    else: 
        print("Error")

def recibirNum():
    num = int(input("Ingrese un número: "))
    parImpar(num)
    recibirNum()

""""7.-Crear una función que reciba una lista de edades y muestre cuántas personas son mayores
de edad (18 años o más)."""
def edades(lista):
    num = 0
    for i in range(len(lista)):
        if lista[i] >= 18:
            num += 1
    return num

def personas():
    edad = []
    inp = int(input("Cuantas personas vas a ingresar hoy?: "))
    for i in range(inp):
        var = int(input(">>"))
        if var != "":
            edad.append(var)
        else:
            print("Por favor ingresar valor valido")
    resultado = edades(edad)
    print(f"Hay {resultado} personas mayores de edad")
    personas()



"""8.-Crear una función que reciba una lista de palabras y permita buscar cuántas veces aparece
una palabra específica ingresada por el usuario."""
def vecesqueAparece(palabras):
    buscar = input("ingrese la palabra que desea buscar: ")
    vecesqueAparece = 0
    for i in range(len(palabras)):
        if buscar == palabras[i]:
            vecesqueAparece += 1
    print(f"La palabra {buscar} aparece {vecesqueAparece} en la lista. ")

def recibirpalabras():
    cantidad = int(input("Ingresa la cantidad de palabras: "))
    listaPalabras = []
    for i in range(cantidad):
        palabras = input(f"{i+1}.")
        listaPalabras.append(palabras)
    vecesqueAparece(listaPalabras)    


"""9.-Crear una función que reciba una lista de números y genere una nueva lista que contenga
únicamente los números positivos."""
def listaPositivos()


"""10.-Crear una función que reciba una lista de productos (utilizando diccionarios con nombre
y stock) y muestre cuáles tienen un stock menor a 5 unidades."""
def productosDiccionario()


def limpiar_consola():
    os.system('cls')