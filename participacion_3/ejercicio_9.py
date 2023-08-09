#Para la clase CuentaBancaria, cree un método retirar que maneje las acciones de retiro de la cuenta.
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

# Ejemplo de uso
cuenta1 = CuentaBancaria("123456789", ["Sofia", "Pablo"], 1000.00)

# Depositar y retirar
cuenta1.depositar(500.00)
cuenta1.retirar(300.00)
cuenta1.retirar(800.00)

