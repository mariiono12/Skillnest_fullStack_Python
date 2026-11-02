# ==============================================================================
# ACTIVIDAD: REPASO DE FUNCIONES (PRÁCTICA PRUEBA)
# ==============================================================================

# 1. Función para determinar el número mayor y menor en una lista de enteros
def mostrar_mayor_menor(numeros):
    if not numeros:
        print("La lista está vacía.")
        return
    
    mayor = max(numeros)
    menor = min(numeros)
    print(f"\n[Ejercicio 1]")
    print(f"Lista de números: {numeros}")
    print(f"Número mayor: {mayor}")
    print(f"Número menor: {menor}")


# 2. Función para contar vocales en una cadena de texto
def contar_vocales(texto):
    vocales = "aeiouáéíóúAEIOUÁÉÍÓÚ"
    contador = 0
    
    for caracter in texto:
        if caracter in vocales:
            contador += 1
            
    print(f"\n[Ejercicio 2]")
    print(f"Texto: '{texto}'")
    print(f"Cantidad de vocales: {contador}")


# 3. Función para filtrar nombres con más de 5 letras
def filtrar_nombres_largos(nombres):
    print(f"\n[Ejercicio 3]")
    print(f"Lista completa de nombres: {nombres}")
    print("Nombres con más de 5 letras:")
    
    encontrados = False
    for nombre in nombres:
        if len(nombre) > 5:
            print(f"- {nombre}")
            encontrados = True
            
    if not encontrados:
        print("No se encontraron nombres con más de 5 letras.")


# 4. Función para calcular el promedio de notas y verificar aprobación
def evaluar_promedio(notas):
    if not notas:
        print("No hay notas registradas.")
        return
    
    suma = sum(notas)
    promedio = suma / len(notas)
    
    print(f"\n[Ejercicio 4]")
    print(f"Notas: {notas}")
    print(f"Promedio: {promedio:.2f}")
    
    if promedio >= 4.0:
        print("Estado: APROBADO")
    else:
        print("Estado: REPROBADO")


# 5. Función para aplicar 10% de descuento a una lista de precios
def aplicar_descuento(precios):
    print(f"\n[Ejercicio 5]")
    print("Calculando descuento del 10%:")
    
    for precio in precios:
        descuento = precio * 0.10
        nuevo_precio = precio - descuento
        print(f"Precio original: ${precio:,.0f} | Nuevo precio con 10% desc.: ${nuevo_precio:,.0f}")


# 6. Función para determinar si un número entero es par o impar
def es_par_o_impar(numero):
    print(f"\n[Ejercicio 6]")
    if numero % 2 == 0:
        print(f"El número {numero} es PAR.")
    else:
        print(f"El número {numero} es IMPAR.")


# 7. Función para contar mayores de edad (18 años o más)
def contar_mayores_edad(edades):
    contador = 0
    for edad in edades:
        if edad >= 18:
            contador += 1
            
    print(f"\n[Ejercicio 7]")
    print(f"Lista de edades: {edades}")
    print(f"Cantidad de personas mayores de edad (>= 18): {contador}")


# 8. Función para buscar la frecuencia de una palabra en una lista
def buscar_palabra(palabras, palabra_buscada):
    contador = 0
    palabra_buscada_lower = palabra_buscada.lower()
    
    for p in palabras:
        if p.lower() == palabra_buscada_lower:
            contador += 1
            
    print(f"\n[Ejercicio 8]")
    print(f"La palabra '{palabra_buscada}' aparece {contador} vez/veces en la lista.")


# 9. Función para filtrar solo los números positivos de una lista
def obtener_positivos(numeros):
    positivos = []
    for num in numeros:
        if num > 0:
            positivos.append(num)
            
    print(f"\n[Ejercicio 9]")
    print(f"Lista original: {numeros}")
    print(f"Nueva lista (solo números positivos): {positivos}")


# 10. Función para mostrar productos con stock menor a 5 unidades (usa diccionarios)
def revisar_stock_bajo(productos):
    print(f"\n[Ejercicio 10]")
    print("Productos con stock crítico (menor a 5 unidades):")
    
    alerta = False
    for prod in productos:
        if prod["stock"] < 5:
            print(f"- Producto: {prod['nombre']} | Stock actual: {prod['stock']} unidades")
            alerta = True
            
    if not alerta:
        print("Todos los productos tienen stock suficiente (>= 5).")


# ==============================================================================
# MENÚ INTERACTIVO Y FLUJO PRINCIPAL DEL PROGRAMA
# ==============================================================================

def menu():
    while True:
        print("\n" + "="*50)
        print("          SISTEMA DE REPASO DE FUNCIONES        ")
        print("="*50)
        print("1.  Mostrar número mayor y menor")
        print("2.  Contar vocales en un texto")
        print("3.  Filtrar nombres con más de 5 letras")
        print("4.  Calcular promedio de notas y aprobación")
        print("5.  Aplicar 10% de descuento a lista de precios")
        print("6.  Determinar si un número es par o impar")
        print("7.  Contar cuántas personas son mayores de edad")
        print("8.  Buscar cuántas veces aparece una palabra")
        print("9.  Generar lista con solo números positivos")
        print("10. Mostrar productos con stock menor a 5 unidades")
        print("0.  Salir")
        print("="*50)
        
        opcion = input("Seleccione una opción (0-10): ")
        
        if opcion == "1":
            numeros = [15, 3, 42, -8, 23, 100, 4]
            mostrar_mayor_menor(numeros)
            
        elif opcion == "2":
            texto = input("Ingrese un texto o frase: ")
            contar_vocales(texto)
            
        elif opcion == "3":
            nombres = ["Ana", "Cristóbal", "Valentina", "Pedro", "Guillermo", "Sonia"]
            filtrar_nombres_largos(nombres)
            
        elif opcion == "4":
            notas = [6.5, 3.8, 5.0, 4.2, 2.5]
            evaluar_promedio(notas)
            
        elif opcion == "5":
            precios = [10000, 25000, 5000, 1200, 45000]
            aplicar_descuento(precios)
            
        elif opcion == "6":
            try:
                num = int(input("Ingrese un número entero: "))
                es_par_o_impar(num)
            except ValueError:
                print("Error: Debe ingresar un número entero válido.")
                
        elif opcion == "7":
            edades = [12, 18, 25, 15, 30, 17, 65, 8]
            contar_mayores_edad(edades)
            
        elif opcion == "8":
            lista_palabras = ["python", "código", "variable", "python", "ciclo", "función", "python"]
            print(f"Lista de palabras disponibles: {lista_palabras}")
            palabra = input("Ingrese la palabra que desea buscar: ")
            buscar_palabra(lista_palabras, palabra)
            
        elif opcion == "9":
            lista_numeros = [-10, 15, -3, 0, 8, -1, 22, -45, 7]
            obtener_positivos(lista_numeros)
            
        elif opcion == "10":
            inventario = [
                {"nombre": "Arroz 1kg", "stock": 12},
                {"nombre": "Aceite 1L", "stock": 3},
                {"nombre": "Fideos 500g", "stock": 2},
                {"nombre": "Azúcar 1kg", "stock": 15},
                {"nombre": "Leche 1L", "stock": 4}
            ]
            revisar_stock_bajo(inventario)
            
        elif opcion == "0":
            print("\n¡Gracias por utilizar el sistema! Saliendo...")
            break
            
        else:
            print("\nOpción no válida. Intente ingresar un número del 0 al 10.")


# Ejecución del programa
if __name__ == "__main__":
    menu()