#Escribir un programa que encuentre el número más grande y el más pequeño en una lista dada.

numeros_str = input("Ingresa una lista de números separados por espacios: ")
numeros_lista = [float(numero) for numero in numeros_str.split()]

# Encontrar el número más grande y el más pequeño
maximo = max(numeros_lista)
minimo = min(numeros_lista)

print("El número más grande en la lista es:", maximo)
print("El número más pequeño en la lista es:", minimo)
