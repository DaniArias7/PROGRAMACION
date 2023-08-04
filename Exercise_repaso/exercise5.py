#Crear una función que convierta grados Fahrenheit a grados Celsius
def main():
    farenheit = float(input("Ingrese el valor en grados farenheit que quiera convertir a celsius"))
    celsius = (farenheit - 32) * (5/9)
    print("El equivalente de: ", farenheit, "grados farenheit en grados celsius es: ", celsius)

if __name__ == "__main__":
    main()