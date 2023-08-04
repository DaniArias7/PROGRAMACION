#Crear un programa que genere una lista de números pares entre 1 y 100
import random
def generar_numeros_pares(cantidad):
    numeros_pares = [num for num in range(1, 101) if num % 2 == 0]
    numeros_pares_aleatorios = random.sample(numeros_pares, cantidad)
    return numeros_pares_aleatorios

cantidad_pares_a_mostrar = 10
lista_pares = generar_numeros_pares(cantidad_pares_a_mostrar)
print(lista_pares)


