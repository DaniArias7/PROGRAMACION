#Cree una clase Carta que contenga dos propiedades valor y pinta, las cuales son asignadas solo al momento de la construcción del objeto (se pasan como parámetros en el constructor). Defina 4 constantes que representan los nombres de las 4 pintas que puede tener una carta.
class Carta:
    def __init__(self, valor, pinta):
        self.valor = valor
        self.pinta = pinta

# Definir constantes para las pintas
PINTA_CORAZON = "Corazón"
PINTA_DIAMANTE = "Diamante"
PINTA_TREBOL = "Trébol"
PINTA_PICA = "Pica"

carta1 = Carta(10, PINTA_CORAZON)
carta2 = Carta(3, PINTA_TREBOL)

print(f"Carta 1: Valor = {carta1.valor}, Pinta = {carta1.pinta}")
print(f"Carta 2: Valor = {carta2.valor}, Pinta = {carta2.pinta}")
