x = float(input("Ingrese 1 numero: "))
y = float(input("Ingrese 1 numero: "))
z = float(input("Ingrese 1 numero: "))

if ((x + y == z)):
    print("La suma de ",x," + ",y," = ",z)
elif ((x + z == y)):
    print("La suma de ",x," + ",z," = ",y)
elif ((y + z == x)):
    print("La suma de ",y," + ",z," = ",x)