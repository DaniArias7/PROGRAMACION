#Crear un programa que pida al usuario ingresar dos números y calcule su suma, resta, multiplicación y division.
def suma(a, b):
    return a + b


def resta(a, b):
    return a - b


def multiplicacion(a, b):
    return a * b


def division(a, b):
    if b == 0:
        return "Error: No es posible dividir entre cero."
    return a / b


def obtener_operacion():
    while True:
        operacion = input("Ingrese la operación que desea realizar (+, -, *, /): ")
        if operacion in ('+', '-', '*', '/'):
            return operacion
        print("Operación inválida. Intente nuevamente.")


def main():
    try:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))

        operacion = obtener_operacion()

        if operacion == '+':
            resultado = suma(num1, num2)
        elif operacion == '-':
            resultado = resta(num1, num2)
        elif operacion == '*':
            resultado = multiplicacion(num1, num2)
        else:
            resultado = division(num1, num2)

        print("Resultado:", resultado)

        continuar = input("¿Desea realizar otra operación? (s/n): ")
        if continuar.lower() == 's':
            main()
    except ValueError:
        print("Error: Ingrese números válidos.")
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
