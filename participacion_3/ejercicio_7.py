#Cree una clase CuentaBancaria que contenga los siguientes atributos: numero_cuenta, propietarios y balance. Los tres atributos se deben inicializar en el constructor con valores recibidos como parámetros.
class CuentaBancaria:
    def __init__(self, numero_cuenta, propietarios, balance):
        self.numero_cuenta = numero_cuenta
        self.propietarios = propietarios
        self.balance = balance

# Ejemplo de uso
cuenta1 = CuentaBancaria("123456789", ["Juan", "María"], 1000.00)
cuenta2 = CuentaBancaria("987654321", ["Ana"], 500.00)

class CuentaBancaria:
    def __init__(self, numero_cuenta, propietarios, balance):
        self.numero_cuenta = numero_cuenta
        self.propietarios = propietarios
        self.balance = balance


cuenta1 = CuentaBancaria("123456789", ["Sofia", "Pablo"], 1000.00)
cuenta2 = CuentaBancaria("987654321", ["Mariel"], 500.00)

print(cuenta1.numero_cuenta)
print(cuenta1.propietarios)
print(cuenta1.balance)

print(cuenta2.numero_cuenta)
print(cuenta2.propietarios)
print(cuenta2.balance)


