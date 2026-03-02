passwordcorrect = "stockholm"
ent = input("Enter the password: ") 

array1 = list(passwordcorrect)
array2 = list(ent)

if len(array1) != len(array2):
    print("Incorrect password")

else:
    com = 0 #contador de caracteres que coinciden
    for i in range(len(array1)):
        if array1[i] == array2[i]:
            com += 1

    print(f"coincidieron {com} caracteres")
    

            