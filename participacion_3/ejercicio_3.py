#A la clase del punto anterior, defínale los siguientes métodos:
#- Un método mostrar que imprima por consola las coordenadas del punto
#- Un método mover que cambie las coordenadas del punto
#- Un método calcular_distancia que calcule la distancia de la instancia actual con otro punto.
class Punto:
    def __init__(self, x: float, y: float):
        self.x: float = x
        self.y: float = y

    def mostrar(self,):
        print(self.x, self.y)

coord = Punto(2,8)
coord.mostrar()




#x_coordenada = float(input("Ingrese la coordenada x del punto: "))
#y_coordenada = float(input("Ingrese la coordenada y del punto: "))

#punto = Punto(x_coordenada, y_coordenada)
#punto2 = Punto(40, 5)



