x = float(input("Ingrese el lado a del triangulo: "))
y = float(input("Ingrese el lado b del triangulo: "))
z = float(input("Ingrese el lado c del triangulo: "))

if (((x + y)>z) and ((z + y)>x) and ((x + z)>y)):
    print("Si es posible hacer un triangulo")
else:
    print("No es posible hacer el triangulo")