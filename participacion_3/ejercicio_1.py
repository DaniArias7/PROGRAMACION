#Cree una clase Vehículo que contenga los atributos de instancia velocidad_maxima y kilometraje.
class Vehiculo:
    def __init__(self, velocidad_maxima: float, kilometraje: float):
        self.velocidad_maxima: float = velocidad_maxima
        self.kilometraje: float = kilometraje

velocidad = float(input("Ingrese la velocidad máxima del vehículo: "))
kilometraje = float(input("Ingrese el kilometraje del vehículo: "))

vehiculo = Vehiculo(velocidad, kilometraje)

print("Velocidad Máxima:", vehiculo.velocidad_maxima)
print("Kilometraje:", vehiculo.kilometraje)
