#Cree una clase Circulo que tenga las propiedades centro y radio, las cuales se inicializan con parámetros en el constructor. Defina métodos en la clase para calcular el área, el perímetro e indicar si un punto pertenece al círculo o no.
import math

class Circulo:
    def __init__(self, centro: float, radio: float):
        self.centro: float = centro
        self.radio: float = radio

    def calcular_area(self):
        return math.pi * self.radio ** 2

    def calcular_perimetro(self):
        return 2 * math.pi * self.radio

    def punto_pertenece(self, punto):
        distancia_al_centro = math.sqrt((punto[0] - self.centro[0]) ** 2 + (punto[1] - self.centro[1]) ** 2)
        return distancia_al_centro <= self.radio

centro_x = float(input("Ingrese la coordenada x del centro: "))
centro_y = float(input("Ingrese la coordenada y del centro: "))
radio = float(input("Ingrese el radio del círculo: "))

centro = (centro_x, centro_y)
circulo = Circulo(centro, radio)

print("Área:", circulo.calcular_area())
print("Perímetro:", circulo.calcular_perimetro())

punto_x = float(input("Ingrese la coordenada x del punto: "))
punto_y = float(input("Ingrese la coordenada y del punto: "))
punto = (punto_x, punto_y)

if circulo.punto_pertenece(punto):
    print("El punto pertenece al círculo.")
else:
    print("El punto no pertenece al círculo.")
