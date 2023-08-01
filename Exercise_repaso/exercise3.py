#Crear un programa que genere una lista de números aleatorios y los imprima en pantalla.
import random

cantidad_numeros = 5

numeros_aleatorios = []
for _ in range(cantidad_numeros):
    numero = random.randint(1, 100)  # Genera un número aleatorio entre 1 y 100
    numeros_aleatorios.append(numero)

print(numeros_aleatorios)

