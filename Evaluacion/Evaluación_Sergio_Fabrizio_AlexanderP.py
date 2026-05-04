import os
#Evaluación Python funciones

'''Crear una función que reciba una lista de números y determine si todos los números son positivos.
 Si encuentra al menos un número negativo, debe indicarlo y detener el recorrido.
 (Sergio Bustos)
 '''
def positivo(lista):
 for i in range(len(lista)):
    if lista[i] <= 0:
        print(f"Se encontro un numero negativo: {lista[i]}")
        return
    print("El numero es positivo")

 
def Revisar():
    cantidad = int(input("Ingrese una cantidad de números: "))
    lista1 = []
    for i in range(cantidad):
        numeros = int(input("Ingrese un numero: "))
        lista1.append(numeros)
     
    print(positivo(lista1))


''' 6- Crear una función que reciba una lista de edades y clasifique a las personas en tres grupos: menores de edad, adultos y adultos mayores (60+).
 Debe mostrar la cantidad de personas en cada grupo. '''

''' 6- Crear una función que reciba una lista de edades y clasifique a las personas en tres grupos: menores de edad, adultos y adultos mayores (60+).
 Debe mostrar la cantidad de personas en cada grupo. '''

def solicitar_edad(cantidad):
    menores = 0
    adultos = 0
    adultos_mayores = 0

    for i in range(cantidad):
        edad = int(input("Ingrese su edad: "))
        if edad < 18:
            menores += 1
        elif edad < 60:
            adultos += 1
        else:
            adultos_mayores += 1
    return menores, adultos, adultos_mayores

def resultado_ejercicio():
    cantidad = int(input("Ingrese la cantidad de edades: "))
    menores, adultos, adultos_mayores = solicitar_edad(cantidad)
    print(f"Menores: {menores}")
    print(f"Adultos: {adultos}")
    print(f"Adultos mayores: {adultos_mayores}")



# 3. Crear una función que reciba una lista de notas (decimales) y genere dos listas: una con aprobados (≥ 4.0) y otra con reprobados (< 4.0).
# Debe mostrar ambas listas y la cantidad de estudiantes en cada grupo.
# (Fabrizio Ortiz Mendieta)

def alumnosnotas(notas):
    aprobados = []
    reprobados = []
    for nota in notas:
        if nota >= 4.0:
            aprobados.append(nota)
        else:
            reprobados.append(nota)
    print("aprobados: ", aprobados)
    print("reprobados ", reprobados)
    print("Cantidad de alumnos aprobados:", len(aprobados))
    print("Cantidad de alumnos reprobados:", len(reprobados))

def aprobadosreprobados():
    cantidad_notas = int(input("Ingrese la cantidad de notas finales: "))
    notas = []
    for i in range(cantidad_notas):
        while True:
            try:
                nota = float(input(f"Ingrese la nota final del estudiante {i+1} (del 1.0 al 7.0): "))
                if 1.0 <= nota <= 7.0:
                    notas.append(nota)
                    break
                else:
                    print("Ingrese una nota en el rango del 1.0 al 7.0")
            except ValueError:
                print("Ingrese un número decimal del 1.0 al 7.0")
    alumnosnotas(notas)

def limpiar_consola():
    os.system('cls')

continuar = True
while continuar:
    print("\n--- Ejercicos Python---")
    print("--- 1.- Ejercicio 1 ---")
    print("--- 2.- Ejercicio 2 ---")
    print("--- 3.- Ejercicio 3 ---")
    opcion = input("\n---- Elige una opción: (1-3) (0 para salir) =")
    if opcion == "1":
        print("\nEjecutando ejercicio 1: ")
        Revisar()
    elif opcion == "2":
        print("\nEjecutando ejercicio 2: ")
        resultado_ejercicio()
    elif opcion == "3":
        print("\nEjecutando ejercicio 3: ")
        aprobadosreprobados()
    elif opcion == "0":
        print("Saliendo...")
        continuar = False
    else:
        print("Opcion no valida, intenta otra vez")


