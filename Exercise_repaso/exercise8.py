#Crear una función que invierta el orden de los elementos en una lista dada.
def invertir_lista():
    numeros = input("Ingresa los números separados por espacios: ").split()
    try:
        lista_numeros = [int(num) for num in numeros]
        lista_invertida = lista_numeros[::-1]
        return lista_invertida
    except ValueError:
        print("Error: Ingresa solo números separados por espacios.")
        return []

lista_invertida = invertir_lista()
print("Lista invertida:", lista_invertida)
