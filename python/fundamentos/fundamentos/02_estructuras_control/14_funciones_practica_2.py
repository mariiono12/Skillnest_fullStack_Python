import os
# Funciones

# Ejercicio 1
# Calcula experiencia
def multiplica_por_2(num):
    resultado = []
    for i in range(num + 1):
        resultado.append(i * 2)
    return resultado
# Debe retornar: [0, 2, 4, 6, 8, 10]


# Ejercicio 2
# Analiza publicaciones
def suma_y_resta(a):
   print(a[0] + a[1])
   return a[0] - a[1]
# Imprime: 235 y retorna: 5


# Ejercicio 3
# Puntaje ajustado
def sumatoria_menos_longitud(b):
    total = 0
    largo = len(b)
    for i in range(largo):
        total += b[i]
    print(f"Suma total = {total}, longitud = {largo}")
    return total - largo
# Suma total = 25, longitud = 4, debe retornar: 21


# Ejercicio 4
# Ajusta visualizaciones
def valores_multiplicados_segundo(c):
    n = []
    print(len(c))
    for i in range(len(c)):
        n.append(c[i] * (len(c) - 1))
    return n
# Imprime: 4 y retorna: [300, 9, 150, 60]
# Imprime: 1 y retorna: []


# Ejercicio 5
# Genera precio fijo
def valor_multiplicado_longitud(d, e):
    l = []
    for i in range(e) :
        l.append(d*e)
    return l
# Debe retornar: [10, 10]
# Debe retornar: [35, 35, 35, 35, 35]

def limpiar_consola():
    os.system('cls')

# Menu de navegacion para ejercicios
continuar = True
while continuar:
    print("\n---Ejercicios Python---")
    print("--- 1.- Ejercicio 1 ---")
    print("--- 2.- Ejercicio 2 ---")
    print("--- 3.- Ejercicio 3 ---")
    print("--- 4.- Ejercicio 4 ---")
    print("--- 5.- Ejercicio 5 ---")

    opcion = input("\n----Elige una opcion: (1 - 5) (0 para salir) =")
    if opcion == "1":
        limpiar_consola()
        print("\nEjecutando ejercicio 1: ")
        print(multiplica_por_2(5))
    elif opcion == "2":
        limpiar_consola()
        print("\nEjecutando ejercicio 2: ")
        print(suma_y_resta([120, 115]))
    elif opcion == "3":
        limpiar_consola()
        print("\nEjecutando ejercicio 3: ")
        print(sumatoria_menos_longitud([10, 5, 3, 7]))
    elif opcion == "4":
        limpiar_consola()
        print("\nEjecutando ejercicio 4: ")
        print(valores_multiplicados_segundo([100, 3, 50, 20]))
        print(valores_multiplicados_segundo([100]))
    elif opcion == "5":
        limpiar_consola()
        print("\nEjecutando ejercicio 5: ")
        print(valor_multiplicado_longitud(5, 2))
        print(valor_multiplicado_longitud(7, 5))
    elif opcion == "0":
        limpiar_consola()
        print("Saliendo...")
        continuar = False
    else:
        limpiar_consola()
        print("Opcion no valida, intenta otra vez")