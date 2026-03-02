# PEDIR SALDO INICIAL AL USUARIO
while True:
    try:
        SaldoInicial = float(input("Ingrese su saldo inicial: ").replace(",", "."))
        if SaldoInicial < 0:
            print("El saldo no puede ser negativo")
        else:
            break
    except:
        print("Ingrese un valor numérico válido")

op = "" # VARIABLE PARA GUARDAR LA OPCCION DEL USUARIO, INICIALIZADA COMO VACIA.

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

        try:
            Retiro = float(input("Ingrese el monto a retirar: ").replace(",", "."))
            if Retiro <= 0:
                print("El monto debe ser mayor que cero")
            else:
                impuesto = Retiro * 0.004
                total_descuento = Retiro + impuesto
                if total_descuento <= SaldoInicial:
                    SaldoInicial -= total_descuento
                    print("Retiro exitoso")
                    print("Impuesto 4x1000:", impuesto)
                    print("Total descontado:", total_descuento)
                    print("ahora su saldo es", SaldoInicial)
                else:
                    print("Fondos insuficientes")
        except:
            print("Ingrese un valor numérico válido")
        

    elif op =="3": # OPCCION 3 (DEPOSITO).
        try:
            Deposito = float(input("Ingrese saldo a depositar:").replace (",","."))
            if Deposito > 0:
                SaldoInicial += Deposito
                print("Deposito exitoso, ahora su saldo es", SaldoInicial)
            else:
                print("El monto debe ser mayor que cero")
        except:
            print("Ingrese un valor numérico válido")


    elif op =="4": # OPCCION 4 (ENVIAR).
        try:
            Enviar = float(input("Ingrese el monto a enviar:").replace (",","."))
            if Enviar <= 0:
                print("El monto debe ser mayor que cero")
            elif Enviar <= SaldoInicial:
                SaldoInicial -= Enviar
                print("Envio exitoso, ahora su saldo es", SaldoInicial)
            else:
                print("Fondos insuficientes")
        except:
            print("Ingrese un valor numérico válido")

    elif op == "5": # OPCCION 5 (SALIR).
        print("Gracias por usar JJBANK, hasta luego!") 