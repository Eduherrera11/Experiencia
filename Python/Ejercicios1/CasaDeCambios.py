
y = float()

print('Que cantidad de euros desea cambiar?')
print('')
y = float(input())

print('en dolares al cambio son: ', 1.2*y )
print('')
Casa = (1.2*y)*0.10

print('el porcentaje de la casa de cambios es: ', Casa)
print('')
y = (y*1.2) - Casa

print('el total a recibir por el cliente es: ', y)

