# PEDIR SALDO INICIAL AL USUARIO
SaldoInicial = float(input("Ingrese su saldo inicial: "))

op = "" #

while op != "5": # MIENTRAS LA OPCCION NO SEA IGUAL A 5 ....

    print("\n=== MENU JJBANK ===")
    print("1. Ver saldo")
    print("2. Retirar dinero")
    print("3. Depositar dinero")
    print("4. Enviar")
    print("5. Salir")
    
    op = input("Seleccione una opción: ")

    if op == "1": # OPCCION 1 (VER SALDO).
        print("Tu saldo es", SaldoInicial)
    

    elif op =="2": # OPCCION 2 (RETIRO).
        Retiro = float(input("Ingrese el monto a retirar: ").replace (",","."))
        
        if Retiro <= 0:
            print("El monto debe ser mayor que cero")
        elif Retiro <= SaldoInicial:
            SaldoInicial -= Retiro
            print("Retiro exitoso")
        else:
            print("Fondos insuficientes")
        
    
    elif op =="3": # OPCCION 3 (DEPOSITO).
        Deposito = float(input("Ingrese saldo a depositar:").replace (",","."))
        if Deposito > 0:
            SaldoInicial = SaldoInicial + Deposito
            print("El deposito se ha generado exitosamente, ahora su saldo es", SaldoInicial)