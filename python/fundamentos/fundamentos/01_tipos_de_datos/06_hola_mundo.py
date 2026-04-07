# hola_mundo.py (Versión SIN respuestas)


# 1. Imprime "Hola, mundo"
#    Reemplaza el comentario con el código necesario para que, al ejecutar,
#    aparezca en pantalla la frase "Hola, mundo".
#    Ejemplo de uso: print("Mensaje")
# ---------------------------------------------------------------
# (tu código aquí)
print("hola, mundo")

# 2. Imprime "Hola, Valeria" con el nombre en una variable
#    a) Concatenación usando comas
#    b) Concatenación usando +
# ---------------------------------------------------------------
nombre = "Valeria"
# a) Usando comas
# (tu código aquí)
print(f"hola, {nombre}")

# b) Usando +
# (tu código aquí)
print(f"hola + {nombre}")



# 3. Imprime "Hola 156!" con el número en una variable
#    a) Usando comas
#    b) Usando + (esto podría dar error si no conviertes el número a str)
# ---------------------------------------------------------------
numero = 156


# a) Usando comas
# (tu código aquí)
print(f"Hola, {numero}")

# b) Usando +
# (tu código aquí)
print("hola " + str(numero) + "!")
# BONUS: Corrige el error con conversión de tipos si aparece.




# 4. Imprime "Me encanta comer X e Y" con dos de tus comidas favoritas
#    a) Usando .format()
#    b) Usando f-strings
# ---------------------------------------------------------------
comida1 = "Arroz"
comida2 = "Huevos revueltos"


# a) Con .format()
# (tu código aquí)
print("Me encanta comer {} y {}".format(comida1, comida2))

# b) Con f-string
# (tu código aquí)
print(f"Me encanta comer {comida1} y {comida2}.")



# Desafío bonus: Usa al menos un método de cadena adicional.
# Ejemplo: .upper(), .lower(), .replace(), etc.
# ---------------------------------------------------------------
# (tu código aquí)
nombre = input("Ingresa tu nombre :")
nombre_mayusculas = nombre.upper()
print(nombre_mayusculas)