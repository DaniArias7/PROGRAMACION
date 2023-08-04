#Crear un programa que genere una matriz de números y la imprima en pantalla.
import random

def generar_matriz(filas, columnas):
    matriz = [[random.randint(1, 100) for _ in range(columnas)] for _ in range(filas)]
    return matriz

def imprimir_matriz(matriz):
    for fila in matriz:
        print(' '.join(str(elemento) for elemento in fila))

def main():
    filas = 3
    columnas = 3

    matriz_generada = generar_matriz(filas, columnas)
    imprimir_matriz(matriz_generada)

if __name__ == "__main__":
    main()
