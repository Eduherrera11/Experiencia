print('MENU DEL RESTAURANTE')
print('ensalada mixta-------12 euros')
print('sopa de pescado-------10 euros')
print('dorada al horno-------18 euros')
print('arroz al curry-------14 euros')
print('lazaña de carne-------15 euros')
print('brownie de chocolate-------8 euros')
print('helado-------6 euros')
print('refrescos-------5.5 euros')
print('cafe-------3.5 euros')

x = int(input('Cuantos platos desea ordenar del platillo numero 1: '))
x2 = int(input('Cuantos platos desea ordenar del platillo numero 2: '))
x3 = int(input('Cuantos platos desea ordenar del platillo numero 3: '))
x4 = int(input('Cuantos platos desea ordenar del platillo numero 4: '))
x5 = int(input('Cuantos platos desea ordenar del platillo numero 5: '))
x6 = int(input('Cuantos platos desea ordenar del postre numero 1: '))
x7 = int(input('Cuantos platos desea ordenar del postre numero 2: '))
x8 = int(input('Cuatas bebidas desea ordenar del bebida numero 1: '))
x9 = int(input('Cuantas bebidas desea ordenar del bebida numero 2: '))

x = x*12
x2 = x2*10
x3 = x3*18
x4 = x4*14
x5 = x5*15
x6 = x6*8
x7 = x7*6
x8 = x8*5.5
x9 = x9*3.5

total = (x + x2 + x3 + x4 + x5 + x6 + x7 + x8 + x9)

print('El monto total de su cuenta es: ', total)