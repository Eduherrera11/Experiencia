precio = float(input("Imprime el precio de producto: "))

if (precio<100):
    print("es buen momento para comprar")
elif ((precio >= 100) and (precio <= 150)):
    print("debemos mantener")
else:
    print("es hora de vender")