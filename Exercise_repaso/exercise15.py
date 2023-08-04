#Crear un programa que pida al usuario ingresar una cadena de texto y determine si es un palíndromo o no
def es_palindromo(cadena):
    # Eliminamos los espacios y convertimos la cadena a minúsculas para evitar problemas de caso
    cadena = cadena.replace(" ", "").lower()

    # Comparamos la cadena con su inversa
    return cadena == cadena[::-1]
def main():
    # Pedimos al usuario que ingrese una cadena de texto
    cadena = input("Ingresa una cadena de texto: ")

    if es_palindromo(cadena):
        print("Es un palíndromo.")
    else:
        print("No es un palíndromo.")


if __name__ == "__main__":
    main()
