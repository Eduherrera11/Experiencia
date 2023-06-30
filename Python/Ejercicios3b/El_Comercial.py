'''Eres un comercial trabajando para una compañía que vende diversos productos. Quieres crear un 
programa para realizar un seguimiento de los productos que has vendido y el valor total de las 
ventas. Supongamos que hay un total de 10 productos. 
Tú has vendido 5 de estos productos en las siguientes cantidades: 
Producto 1: 3 unidades 
Producto 2: 1 unidad 
Producto 5: 7 unidades 
Producto 6: 2 unidades 
Producto 9 : 4 unidades 
Los precios de cada uno de estos productos son como siguen: 
Producto 1: 30.0 EU	 	 Producto 6: 44.0 EU
Producto 2: 9.8 EU	 	 Producto 7: 21.2 EU 
Producto 3: 42.5 EU	 	 Producto 8: 53.2 EU 
Producto 4: 32.6 EU	 	 Producto 9: 25.3 EU 
Producto 5: 71.5 EU	 	 Producto 10: 57.8 EU 
Crea un script que dada una lista con los productos, sus precios y las unidades vendidas, imprima 
la cantidad total de ventas, el dinero facturado por producto y el dinero total.'''

lista = [["Producto1",30],["Producto2",9.8],["Producto3",42.5],["Producto4",32.6],["Producto5",71.5],["Producto6",44],["Producto7",21.2],["Producto8",53.2],["Producto9",25.3],["Producto10",57.8]]
x = 0
y = 0
z = 0

p1 = int(input("Cuantas unidades se vendieron del producto 1: "))
p2 = int(input("Cuantas unidades se vendieron del producto 2: "))
p3 = int(input("Cuantas unidades se vendieron del producto 3: "))
p4 = int(input("Cuantas unidades se vendieron del producto 4: "))
p5 = int(input("Cuantas unidades se vendieron del producto 5: "))
p6 = int(input("Cuantas unidades se vendieron del producto 6: "))
p7 = int(input("Cuantas unidades se vendieron del producto 7: "))
p8 = int(input("Cuantas unidades se vendieron del producto 8: "))
p9 = int(input("Cuantas unidades se vendieron del producto 9: "))
p10 = int(input("Cuantas unidades se vendieron del producto 10: "))
print("")
if p1 != 0:
    x = x + p1
if p2 != 0:
    x = x + p2
if p3 != 0:
    x = x + p3
if p4 != 0:
    x = x + p4
if p5 != 0:
    x = x + p5
if p6 != 0:
    x = x + p6
if p7 != 0:
    x = x + p7
if p8 != 0:
    x = x + p8
if p9 != 0:
    x = x + p9
if p10 != 0:
    x = x + p10

p1 = p1*(lista[0][1])
p2 = p2*(lista[1][1])
p3 = p3*(lista[2][1])
p4 = p4*(lista[3][1])
p5 = p5*(lista[4][1])
p6 = p6*(lista[5][1])
p7 = p7*(lista[6][1])
p8 = p8*(lista[7][1])
p9 = p9*(lista[8][1])
p10 = p10*(lista[9][1])

print("El total de unidades vendidas ", x)
print("")
print("Se vendieron del Producto 1: ", p1,"$")
print("Se vendieron del Producto 2: ", p2,"$")
print("Se vendieron del Producto 3: ", p3,"$")
print("Se vendieron del Producto 4: ", p4,"$")
print("Se vendieron del Producto 5: ", p5,"$")
print("Se vendieron del Producto 6: ", p6,"$")
print("Se vendieron del Producto 7: ", p7,"$")
print("Se vendieron del Producto 8: ", p8,"$")
print("Se vendieron del Producto 9: ", p9,"$")
print("Se vendieron del Producto 10: ", p10,"$")
print("")
z = p1+p2+p3+p4+p5+p6+p7+p8+p9+p10

print("El dinero total de ventas es ", z)


