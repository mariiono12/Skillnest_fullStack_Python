'''Actividad: Gestor de inventario'''

'''#1.- Creación: Crear una lista llamada inventario que contenga los siguientes
# articulos: "laptop", "ratón", "monitor", "cable hdmi"
'''
inventario = ["laptop", "raton", "monitor", "cable hdmi"]
print(inventario)
'''2.- Expansión: Utiliza el método correspondiente para agregar "impresora"
al final de la lista 
'''
inventario.append("impresora")
inventario.append("teclado")


'''3.-Conteo: Utiliza la función integrada para mostrar cuantos elementos 
totales hay en la lista'''
print(len(inventario))
print(inventario)
'''4.- Acceso y modificación: Modifica "teclado" por "teclado mecánico"'''
inventario[5]= "teclado mecanico"
print(inventario[5])
'''5.- Slicing: Crea una nueva lista llamada "promoción", debe contener
solo los 3 primeros elementos de la lista "articulos".'''
promoción = ["laptop", "raton", "monitor"]

'''6.- Mostrar la lista de inventario ordenado alfabeticamente.'''
inventario.sort()
print(inventario)

'''7.-Elimina el último elemento de la lista inventario mostrando el elemento eliminado y la lista final'''

eliminado = inventario.pop()
print(eliminado)
print(inventario)






