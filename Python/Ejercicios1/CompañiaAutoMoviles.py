print('CompañiaAutoMoviles')
print('')
num1 = float(input('Ingrese cuantos vehiculos modelo RBM Serie1 ha vendido este mes: '))
num2 = float(input('Ingrese cuantos vehiculos modelo RBM Serie Plus ha vendido este mes: '))
num3 = float(input('Ingrese cuantos vehiculos modelo RBM Serie TodoTerreno ha vendido este mes: '))
print()

num1 = (num1*20000)*0.03
num2 = (num2*35000)*0.05
num3 = (num3*60000)*0.07

print()
print('comisiones por venta en el primer coche son: ', num1)
print('comisiones por venta en el segundo coche son: ', num2)
print('comisiones por venta en el tercer coche son: ', num3)

Total = num1 + num2 + num3

print('El total a cobrar en comisiones es:', Total)