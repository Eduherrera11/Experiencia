x = int(input("Ingrese 1 numero: "))
y = int(input("Ingrese 1 numero: "))
z = int(input("Ingrese 1 numero: "))
o = int(input("Ingrese 1 numero: "))

if ((x > y) and (x > z) and (x > o)):
    print("El numero mayor es: ", x)
elif ((y > x) and (y > z) and (y > o)):
    print("El numero mayor es: ", y)
elif ((z > x) and (z > y) and (z > o)):
    print("El numero mayor es: ", z)
else:
    print("El numero mayor es: ", o)

