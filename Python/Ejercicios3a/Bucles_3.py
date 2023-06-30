'''Crea un script que pida al usuario una palabra y luego muestre por pantalla una a una las letras
de la palabra introducida empezando por la última. 
'''

print("Bienvenido al programa")
palabra = str(input("Introduzca una palabra: "))
longitud = len(palabra)

for i in range(longitud-1,-1,-1 ):
    print(palabra[i])

print("Bienvenido al programa")
palabra = str(input("Introduzca una palabra: "))

for i in palabra[::-1]:
    print(i)