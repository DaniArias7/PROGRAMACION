#Crear un programa que calcule la suma de los números en una lista dada
def calculate_sum(lista):
    suma = sum(lista)
    return suma
def main():
    list = [int(x) for x in input("Ingresa los números de la lista separados por espacios: ").split()]
    suma = calculate_sum(list)
    print("La suma de los números en la lista es:", suma)

if __name__ == "__main__":
    main()