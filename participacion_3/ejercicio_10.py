#Para la clase CuentaBancaria, cree un método aplicar_cuota_manejo que aplique un porcentaje del 2% sobre el balance de la cuenta
class CuentaBancaria:
    def __init__(self, numero_cuenta, propietarios, balance):
        self.numero_cuenta = numero_cuenta
        self.propietarios = propietarios
        self.balance = balance

    def depositar(self, monto):
        if monto > 0:
            self.balance += monto
            print(f"Se depositaron ${monto} en la cuenta {self.numero_cuenta}. Nuevo balance: ${self.balance}")
        else:
            print("El monto de depósito debe ser mayor que cero.")

    def retirar(self, monto):
        if 0 < monto <= self.balance:
            self.balance -= monto
            print(f"Se retiraron ${monto} de la cuenta {self.numero_cuenta}. Nuevo balance: ${self.balance}")
        else:
            print("Monto de retiro inválido. Verifica el monto o el saldo disponible.")

    def aplicar_cuota_manejo(self):
        cuota = self.balance * 0.02
        self.balance -= cuota
        print(f"Se aplicó una cuota de manejo del 2%. Nuevo balance: ${self.balance}")

# Ejemplo de uso
cuenta1 = CuentaBancaria("123456789", ["Sofia", "Pablo"], 1000.00)

# Depositar, retirar y aplicar cuota de manejo
cuenta1.depositar(500.00)
cuenta1.retirar(300.00)
cuenta1.aplicar_cuota_manejo()
