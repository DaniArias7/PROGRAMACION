#A la clase del punto anterior, defínale los siguientes métodos:
#- Un método mostrar que imprima por consola las coordenadas del punto
#- Un método mover que cambie las coordenadas del punto
#- Un método calcular_distancia que calcule la distancia de la instancia actual con otro punto.
class Punto:
    def __init__(self, x: float, y: float):
        self.x: float = x
        self.y: float = y

    def mostrar(self):
        print("Coordenada x:", self.x)
        print("Coordenada y:", self.y)

    def mover(self, nueva_x: float, nueva_y: float):
        self.x = nueva_x
        self.y = nueva_y

    def calcular_distancia(self, otro_punto):
        distancia = ((self.x - otro_punto.x)**2 + (self.y - otro_punto.y)**2)**0.5
        return distancia

x_coordenada = float(input("Ingrese la coordenada x del punto: "))
y_coordenada = float(input("Ingrese la coordenada y del punto: "))

punto = Punto(x_coordenada, y_coordenada)

print("Valores de los puntos creados:")
punto.mostrar()

x_nueva = float(input("Ingrese la nueva coordenada x del punto: "))
y_nueva = float(input("Ingrese la nueva coordenada y del punto: "))
punto.mover(x_nueva, y_nueva)

print("Valores después de mover el punto:")
punto.mostrar()

x_otro = float(input("Ingrese la coordenada x del otro punto: "))
y_otro = float(input("Ingrese la coordenada y del otro punto: "))
otro_punto = Punto(x_otro, y_otro)

distancia = punto.calcular_distancia(otro_punto)
print("Distancia entre los dos puntos:", distancia)




#x_coordenada = float(input("Ingrese la coordenada x del punto: "))
#y_coordenada = float(input("Ingrese la coordenada y del punto: "))

#punto = Punto(x_coordenada, y_coordenada)
#punto2 = Punto(40, 5)



