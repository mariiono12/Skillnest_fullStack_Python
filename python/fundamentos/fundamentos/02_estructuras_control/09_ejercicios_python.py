#1. Números Pares Dinámicos
#Desarrolla un programa que solicite al usuario cuántos números pares desea ver ($n$). El programa debe imprimir los primeros $n$ números pares positivos.
def numerosDinamicos(): 
    n = int(input("¿Cuántos números pares deseas ver?: "))
    pares = []
    for i in range(1, (n * 2) + 1):
        if i % 2 == 0:
            pares.append(i) 
        print(f"Mostrando pares: {pares}")

#2. Verificador de Edad y Acceso
#Pide al usuario su año de nacimiento. Calcula su edad y muestra si es mayor de edad (18+). Si tiene menos de 18, indica cuántos años le faltan para la mayoría de edad.
def verificador_edad():
    campo = input("Ingrese su eaño de nacimiento: ")
    edad = 2026 - int(campo)
    if campo == "":
        print("Error")
    elif edad >= 18:
        print(f"Tienes acceso ya que tu edad es: {edad}")
    elif edad > 0 and edad <18:
        print(f"No tiene acceso: te faltan {18 - edad} años.")
    else:
        print("Ingresa valores válidos")
        verificador_edad() 
#3. Calculadora de Descuentos
#Solicita el precio de un producto y la cantidad comprada. Si el total supera los $100, aplica un 15% de descuento. Muestra el subtotal, el descuento aplicado y el total final.
def aplicarDescuento():
    precio = float(input("Ingresa el precio del producto: "))
    cantidad = int(input("Ingresar cantidad: "))
    producto = precio * cantidad
    if producto >= 100:
        descuento = producto * 0.15
    else:
        descuento = 0
    total = producto - descuento 
    print(f"El subtotal es: {producto}. El descuento aplicado es: {descuento}")
#4. Clasificador de Números
#Pide un número al usuario e indica si es: Positivo-Par, Positivo-Impar, Negativo-Par, Negativo-Impar o Cero.
#II. Iteraciones y Bucles (Intermedio)
def clasificadorNum():
    num = int(input("Ingrese un número"))
    if num > 0:
        if num % 2 == 0:
            print("Positivo-Par")
        elif num % 2 == 1:
            print("Positivo-Impar")
        elif num < 0:
            if num % 2 == 0:
                print("Negativo-Par")
            elif num % 2 == 1:
                print("Negativo-Impar")
            else: 
                print("Es 0")
#5. Tabla de Multiplicar Personalizada
#Solicita un número entero y muestra su tabla de multiplicar del 1 al 12, pero solo muestra los resultados que sean múltiplos de 3.
def tablaMultiplicar():
    num = int(input("Ingresar Numero a trabajar: "))
    for i in range (1, 13):
        resultado = num * i
        if resultado % 3 == 0:
            print(f"Del {num} solo estos números son divisibles por 3: {resultado} ")
#6. Sumatoria con Centinela
#Crea un programa que pida números continuamente y los sume. El ciclo debe terminar cuando el usuario ingrese un número negativo. Al final, muestra la suma total (sin incluir el negativo).
def  sumatoriaCentinela():
     suma_total = 0
     while True:
       n = int(input("Ingresa un número(negativo para salir):"))
       if n < 0:
        break 
     suma_total += n
     print(f"La suma total es: {suma_total}")
#7. Contador de Vocales
#Pide al usuario una frase o palabra. Utiliza un bucle para recorrer la cadena y contar cuántas vocales tiene en total.
def contadorVocales():
    texto = input("Ingresa una palabra o frase: ").lower()
    vocales = 0
    for i in range(len(texto)):
        if texto[i] == "a" or texto [i] == "e" or texto[i] == "i" or texto[i] == "o" or texto[i] == "u":
            vocales += 1
        elif texto[i] == "á" or texto[i] == "é" or texto[i] == "í" or texto[i] or texto[i] == "ó" or texto[i] == "ú":
            vocales += 1
            print(f"La cadena {texto} tiene {vocales} vocales en total")
#8. Validación de Contraseña
#Define una contraseña en una variable. Pide al usuario que la intente adivinar. Tienes un máximo de 3 intentos; si falla los 3, bloquea el acceso.
#III. Manejo de Arreglos / Listas (Avanzado)
def validacion():
 con ="12345678"
 intentos = 1
 while True :
     ingresa = input("Ingresa la contraseña: ")
     if ingresa == con:
         print("acceso concedido")
         break
     else: 
         intentos += 1
         if intentos > 3:
             print("Acceso denegado")
             break
         else:
             print(f"Número de intentos: {intentos}")

#9. Registro de Nombres
#Crea un arreglo vacío. Pide al usuario que ingrese 5 nombres. Guárdalos en el arreglo y, al final, imprímelos en orden inverso al que fueron ingresados.
def registroNombres():
 nombres = []
 maxi = 0
 while maxi < 5:
     inp = input(f"Por favor ingresar nombre {maxi + 1}: ")
     if inp != "":
         nombres.append(inp)
     else:
         print("Tienes que ingresar un nombre")
         maxi += 1
         for i in range(4, -1, -1):
             print(nombres[i])

#10. Promedio de Notas
#Solicita al usuario cuántas notas desea ingresar. Almacena cada nota en un arreglo. Al finalizar, calcula y muestra el promedio, la nota más alta y la más baja.
def promedioNotas():
 cantidad = int(input("Cuantas notas deseas ingresar?"))
 notas = []
 for i in range (cantidad):
  nota = float(input(f"Nota {i+1}: "))
 notas.append(nota)

 promedio = sum(notas) / len(notas)
 print(f"Promedio: {promedio}")
 print(f"Nota más alta: {max(notas)}")
 print(f"Nota más baja: {min(notas)}")
   
#11. Filtro de Arreglos
#Dado un arreglo de números generado por el usuario, crea un nuevo arreglo que contenga solo los números que sean mayores a 50. Muestra ambos arreglos.
def filtroArreglos():
 cantidad = int(input("Ingresa número: "))
 mayor50 = []
 nUser = []
 for i in range(1, cantidad + 1):
    arrayUsuario = int(input("Ingresa un número: "))
    if arrayUsuario > 50:
       mayor50.append(arrayUsuario)
    else:
       nUser.append(arrayUsuario)
    print(f"Valores ingresados por el usuario: {nUser} \nValores mayor a 50: {mayor50}")
#12. Buscador de Elementos
#Crea una lista de 10 ciudades. Pide al usuario que ingrese el nombre de una ciudad y el programa debe decir si la ciudad se encuentra en la lista y en qué índice (posición) está.
#IV. Retos de Lógica Combinada
def buscadorElemento():
    ciudades = ["Nairobi", "Tokio", "Santiago", "Lima", "Caracas", "Rio", "Berlin", "Seul", "Buenos Aires"]
    ciudad = input("Ingresar ciudad (con mayuscula al principio)")
    esta = ciudades.index(ciudad)
    if esta < len(ciudades):
       print(f"Tu ciudad está en el arreglo, en la posicion {esta}")
    else:
       print("Tu ciudad no está en el arreglo")
#13. Simulación de Inventario
#Crea dos arreglos: uno para nombres_productos y otro para precios. Permite al usuario ingresar 3 productos con sus precios. Luego, muestra una lista formateada: Producto: [Nombre] - Precio: $[Valor].
def inventario():
   nombres_productos = []
   precios = []
   for  i in range(3):
      nombre = input("Nombre del producto:")
      precio = float(input("Precio: "))
      nombres_productos.append(nombre)
      precios.append(precio)
      print("\nInventario:")
      for i in range(3):
         print(f"Producto: {nombres_productos[i]} - Precio {precios[i]}")

#14. Generador de Lista de Compras
#Usa un bucle while para que el usuario agregue artículos a una lista de compras. El proceso termina cuando el usuario escribe "terminar". Al final, muestra la lista ordenada alfabéticamente.
def listaCompra():
   lista = []
   while True:
      item = input("Articulo (o 'terminar')")
      if item.lower() == "terminar":
         break
      lista.append(item)
      print(f"Ordenada: {sorted(lista)}")

#15. Análisis de Temperaturas
#Solicita las temperaturas de los 7 días de la semana y guárdalas en un arreglo. Muestra:
#El promedio semanal.
#Cuántos días la temperatura fue superior a 25 grados.
#El día con la temperatura más baja (asumiendo que el índice 0 es Lunes).

def analisisTemperatura():
   dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabádo", "Domingo"]
   diaSuperior = []
   total = 0
   baja = 100
   diaBaja = ""
   cant = 0
   
   while cant < 7:
      temps = float(input(f"Ingrese temperatura del dia {dias[cant]}: "))
      total += temps

      if temps < baja and temps < 25:
         baja = temps 
         diaBaja = dias[cant]
      elif temps >25:
         diaSuperior.append(dias[cant])
         cant += 1 
         print(f"El promedio de las temperaturas fue de {total / 7}")
         print(f"El dia con la temperatura mas baja fue el dia {diaBaja} con {baja}°")
         print(f"Los dias mas calurosos fueron {diaSuperior}")


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
    print("---8.-Ejercicio 8---")
    print("---9.-Ejercicio 9---")
    print("---10.-Ejercicio 10---")
    print("---11.-Ejercicio 11---")
    print("---12.-Ejercicio 12---")
    print("---13.-Ejercicio 13---")
    print("---14.-Ejercicio 14---")
    print("---15.-Ejercicio 15---")
    opcion = input("---Elige una opción: (1-15) (0 para salir) =")
    if opcion =="1":  
        print("Ejecutando ejercicio 1: ")
        numerosDinamicos()
    elif opcion == "2":
     print("Ejecutando ejercicio 2: ")
     verificador_edad()
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
    elif opcion == "7":
     print("Ejecutando ejercicio 7: ")
     contadorVocales()
    elif opcion == "8":
     print("Ejecutando ejercicio 8: ")
     validacion()
    elif opcion == "9":
     print("Ejecutando ejercicio 9: ")
     registroNombres()
    elif opcion == "10":
     print("Ejecutando ejercicio 10: ")
     promedioNotas()
    elif opcion == "11":
     print("Ejecutando ejercicio 11: ")
     filtroArreglos()
    elif opcion == "12":
     print("Ejecutando ejercicio 12: ")
     buscadorElemento()
    elif opcion == "13":
     print("Ejecutando ejercicio 13: ")
     inventario()
    elif opcion == "14":
     print("Ejecutando ejercicio 14: ")
     listaCompra()
    elif opcion == "15":
     print("Ejecutando ejercicio 15: ")
     analisisTemperatura()
    elif opcion == "0":
     print("Saliendo...")
    continuar = False







else: 
    print("Opción no válida, intenta otra vez")