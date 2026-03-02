Intento1 = input("Ingrese su contraseña: ")
Restriccion = ("La contraseña debe tener entre 8-16 caracteres")
password = ("stockholm")

while Intento1 != password:
    print("Contraseña incorrecta")
    if len(Intento1) < 8 or len(Intento1) > 16:
        print(Restriccion)
    else:
        diferencias = 0
        contador = 0
        min_length = min(len(Intento1), len(password))
        for i in range(min_length):
            if Intento1[i] != password[i]:
                diferencias += 1
        diferencias += abs(len(Intento1) - len(password))
        print(f"Tu contraseña tiene {diferencias} caracteres diferentes a la contraseña correcta.") 
    Intento1 = input("Ingrese su contraseña: ") 
else: 
    print("Contraseña correcta, bienvenido!")