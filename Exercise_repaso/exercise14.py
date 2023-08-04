#Escribir una función que calcule la media aritmética de una lista de números.
def calcular_media(lista):
    if len(lista) == 0:
        return None
    suma = sum(lista)
    media = suma / len(lista)
    return media

def main():
    lista = [float(x) for x in input("Ingresa los números de la lista separados por espacios: ").split()]
    media = calcular_media(lista)
    if media is not None:
        print("La media aritmética es:", media)
    else:
        print("La lista está vacía, no se puede calcular la media.")

if __name__ == "__main__":
    main()
