#PEDIR SALDOS INICIALES AL USUARIO
SaldoCuenta1 = float(input("Ingrese saldo inicial de la Cuenta 1: ").replace(",", "."))
SaldoCuenta2 = float(input("Ingrese saldo inicial de la Cuenta 2: ").replace(",", "."))
op = "" #VARIABLE

while op != "5":

    print("\n=== MENU JJBANK ===")
    print("1. Ver saldos")
    print("2. Retirar dinero")
    print("3. Depositar dinero")
    print("4. Enviar dinero entre cuentas")
    print("5. Salir")
    op = input("Seleccione una opción: ")

    # OPCCION 1 (VER SALDO).    
    if op == "1":
        print("Saldo Cuenta 1:", SaldoCuenta1)
        print("Saldo Cuenta 2:", SaldoCuenta2)

    # OPCCION 2 (RETIRO).
    elif op == "2":
        cuenta = input("¿De qué cuenta desea retirar? (1 o 2): ")
        monto = float(input("Ingrese el monto a retirar: ").replace(",", "."))

        impuesto = monto * 0.004
        total = monto + impuesto

        if cuenta == "1":
            if total <= SaldoCuenta1:
                SaldoCuenta1 -= total
                print("Retiro exitoso")
                print("Impuesto 4x1000:", impuesto)
                print("Total descontado:", total)
                print("ahora su saldo es", SaldoCuenta1)
            elif SaldoCuenta1 >= monto and SaldoCuenta2 >= impuesto:
                SaldoCuenta1 -= monto
                SaldoCuenta2 -= impuesto
                print("Retiro exitoso")
                print("El 4x1000 fue descontado de la Cuenta 2:", impuesto)
                print("Total descontado:", total)
                print("ahora su saldo es", SaldoCuenta1)

            else:
                print("Fondos insuficientes.")

        elif cuenta == "2":
            if total <= SaldoCuenta2:
                SaldoCuenta2 -= total
                print("Retiro exitoso")
                print("Impuesto 4x1000:", impuesto)
                print("Total descontado:", total)
                print("ahora su saldo es", SaldoCuenta2)
            elif SaldoCuenta2 >= monto and SaldoCuenta1 >= impuesto:
                SaldoCuenta2 -= monto
                SaldoCuenta1 -= impuesto
                print("Retiro exitoso")
                print("El 4x1000 fue descontado de la Cuenta 1:", impuesto)
                print("Total descontado:", total)
                print("ahora su saldo es", SaldoCuenta2)
            else:
                print("Fondos insuficientes.")
        else:
            print("Cuenta inválida")

    # OPCCION 3 (DEPOSITO).
    elif op == "3":
        cuenta = input("¿En qué cuenta desea depositar? (1 o 2): ")
        monto = float(input("Ingrese el monto a depositar: ").replace(",", "."))

        if monto > 0:
            if cuenta == "1":
                SaldoCuenta1 += monto
            elif cuenta == "2":
                SaldoCuenta2 += monto
            else:
                print("Cuenta inválida")
                continue
            print("Depósito exitoso")
        else:
            print("Monto inválido")

    # OPCCION 4 (ENVIAR ENTRE CUENTAS)
    elif op == "4":
        origen = input("Cuenta origen (1 o 2): ")
        destino = input("Cuenta destino (1 o 2): ")
        monto = float(input("Monto a enviar: ").replace(",", "."))

        if origen == "1" and destino == "2":
            if monto <= saldo_cuenta1:
                saldo_cuenta1 -= monto
                saldo_cuenta2 += monto
                print("Transferencia exitosa")
            else:
                print("Fondos insuficientes")
        elif origen == "2" and destino == "1":
            if monto <= saldo_cuenta2:
                saldo_cuenta2 -= monto
                saldo_cuenta1 += monto
                print("Transferencia exitosa")
            else:
                print("Fondos insuficientes")
        else:
            print("Cuentas inválidas o iguales")

    elif op == "5": # OPCCION 5 (SALIR).
        print("Gracias por usar JJBANK 👋")

    else:
        print("Opción inválida")