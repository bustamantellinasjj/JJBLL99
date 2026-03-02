#PEDIR SALFO INICIAL AL USUARIO
SaldoInicial = float(input("Ingrese su saldo inicial: "))

#PEDIR MONTO DE RETIRO AL USUARIO
RetirarSaldo = float(input("Ingrese el monto que desea retirar: "))

#VERIFICAR SI SE PUEDE RETIRAR EL SALDO
if RetirarSaldo <= SaldoInicial:
    SaldoInicial = SaldoInicial - RetirarSaldo
    print("Retiro exitoso")
    print("Su nuevo saldo es:", SaldoInicial)
else:
    print("Fondos insuficientes my bro")
