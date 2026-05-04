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

Revisar()