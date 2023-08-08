#Cree una clase Punto que represente un punto en el plano cartesiano.
class Punto:
    def __init__(self, x: float, y: float):
        self.x: float = x
        self.y: float = y

x_coordenada = float(input("Ingrese la coordenada x del punto: "))
y_coordenada = float(input("Ingrese la coordenada y del punto: "))

punto = Punto(x_coordenada, y_coordenada)

print("valores de los puntos creados:")
print("Coordenada x:", punto.x)
print("Coordenada y:", punto.y)


