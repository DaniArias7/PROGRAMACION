#Para la clase CuentaBancaria, cree un método depositar que maneje las acciones de depósito en la cuenta.
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

# Ejemplo de uso
cuenta1 = CuentaBancaria("123456789", ["Sofia", "Pablo"], 1000.00)
cuenta1.depositar(500.00)
cuenta1.depositar(-100.00)
