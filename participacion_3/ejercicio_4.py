#Cree una clase Rectángulo la cual contiene dos atributos de instancia que representan los puntos que definen sus esquinas. Agregue métodos a la clase Rectángulo para calcular su perímetro, calcular su área e indicar si el rectángulo es un cuadrado.
class Rectangulo:
    def __init__(self, esquina_sup_izq, esquina_inf_der):
        self.esquina_sup_izq = esquina_sup_izq
        self.esquina_inf_der = esquina_inf_der

    def calcular_perimetro(self):
        base = abs(self.esquina_inf_der[0] - self.esquina_sup_izq[0])
        altura = abs(self.esquina_inf_der[1] - self.esquina_sup_izq[1])
        return 2 * (base + altura)

    def calcular_area(self):
        base = abs(self.esquina_inf_der[0] - self.esquina_sup_izq[0])
        altura = abs(self.esquina_inf_der[1] - self.esquina_sup_izq[1])
        return base * altura

    def es_cuadrado(self):
        base = abs(self.esquina_inf_der[0] - self.esquina_sup_izq[0])
        altura = abs(self.esquina_inf_der[1] - self.esquina_sup_izq[1])
        return base == altura


# Solicitar al usuario ingresar valores
x1 = int(input("Ingrese la coordenada x de la esquina superior izquierda: "))
y1 = int(input("Ingrese la coordenada y de la esquina superior izquierda: "))
x2 = int(input("Ingrese la coordenada x de la esquina inferior derecha: "))
y2 = int(input("Ingrese la coordenada y de la esquina inferior derecha: "))

# Crear instancia de la clase Rectangulo
rectangulo = Rectangulo((x1, y1), (x2, y2))

# Calcular y mostrar resultados
print("Perímetro:", rectangulo.calcular_perimetro())
print("Área:", rectangulo.calcular_area())
print("¿Es cuadrado?", rectangulo.es_cuadrado())
