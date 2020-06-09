a = input("Ingrese el numero en a: ") #Leer texto que el usuario ingresa
if a.isdigit():
    a = int(a)

while a != 1: 
    if a%2 == 0:
        print("%d," % (a), end = "")
        a = a / 2 #Si el numero es par
    else:
        print("%d," % (a), end = "")
        a = (a * 3) + 1 #Si el numero es impar

    if a == 1:
        print("1")

       