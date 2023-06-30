'''Escribir un programa que almacene la cadena de caracteres contraseña en una variable,
pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta. 
'''

print("La contraseña es Caramelo.1")
contraseña = 'Caramelo.1'

usuario = ""

while (contraseña != usuario.title()):
  usuario = str(input("introduzca la contraseña: "))
print("La contraseña es correcta")