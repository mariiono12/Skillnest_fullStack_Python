import os
#Funciones básicas
#Ejercicio 1
# Calcula experiencia
def multiplica_por_2(n):
    result = []
    for i in range (n +1):
     result.append(i * 2)
    return result
def ejercicio1():
    
    result1 = (multiplica_por_2(5))
    print(result1)

# Debe retornar: [0, 2, 4, 6, 8, 10]

#Ejercicio 2
# Analiza publicaciones
def suma_y_resta(publicaciones):
       suma = suma[0] + suma[1]
       resta = resta[0] - resta[1]
       print(f"")
       return resta 
def ejercicio2():
       resultado = suma_y_resta([120, 115])

# Imprime: 235 y retorna: 5

#Ejercicio 3
# Puntaje ajustado
def sumatoria_menos_longitud(puntaje):
    suma_total = sum(puntaje)
    longitud = len(puntaje)
    resultado = suma_total - longitud
    return resultado
print(sumatoria_menos_longitud([10, 5, 3, 7]))
# Suma total = 25, longitud = 4, debe retornar: 21

#Ejercicio 4
# Ajusta visualizaciones
def valores_multiplicados_segundo(lista):
    if len(lista) < 2:
       print(len(lista))
       return []
    else:
       segEle = lista[1]
       nuevaLista = []
       for i in lista:
          nuevaLista.append(i * segEle)
          long = len(nuevaLista)
          print(long)
          return nuevaLista 
    valores_multiplicados_segundo([100, 3, 50, 20])
# Imprime: 4 y retorna: [300, 9, 150, 60]

#Ejercicio 5
def valores_multiplicados_segundo():
    valores_multiplicados_segundo([[100]])
# Imprime: 1 y retorna: []

#Ejercicio 6
# Genera precio fijo
def valor_multiplicado_longitud():
    valor_multiplicado_longitud([5, 2])
# Debe retornar: [10, 10]

#Ejercicio 7
def valor_multiplicado_longitud():
    valor_multiplicado_longitud([7, 5])
# Debe retornar: [35, 35, 35, 35, 35]



def limpiar_consola():
    os.system('cls')
    #Menu de navegación para ejercicios
continuar = True
while continuar:
    print("---Ejercicios Python---")
    print("---1.-Ejercicio 1---")
    print("---2.-Ejercicio 2---")
    print("---3.-Ejercicio 3---")
    print("---4.-Ejercicio 4---")
    print("---5.-Ejercicio 5---")
    print("---6.-Ejercicio 6---")
    print("---7.-Ejercicio 7---")
    
    opcion = input("---Elige una opción: (1-15) (0 para salir) =")
    if opcion =="1":  
        limpiar_consola()
        print("Ejecutando ejercicio 1: ")
        ejercicio1()
    elif opcion == "1":
     print("Ejecutando ejercicio 1: ")
     ()
    elif opcion == "2":
     print("Ejecutando ejercicio 2: ")
     ejercicio2()
    elif opcion == "3":
     print("Ejecutando ejercicio 3: ")
     aplicarDescuento()
    elif opcion == "4":
     print("Ejecutando ejercicio 4: ")
     clasificadorNum()
    elif opcion == "5":
     print("Ejecutando ejercicio 5: ")
     tablaMultiplicar()
    elif opcion == "6":
     print("Ejecutando ejercicio 6: ")
     sumatoriaCentinela()
    elif opcion == "6":
     print("Ejecutando ejercicio 6: ")
     sumatoriaCentinela()
    elif opcion == "0":
     limpiar_consola()
     print("Saliendo...")
     continuar = False
    else:
       limpiar_consola()
       print("Opción no válida, intenta otra vez")