import numpy as np

print("Esto es un array lleno de ceros: ")
array_1 = np.zeros(8)
print(array_1)

print("Convertimos los ceros en 2:")
array_1[array_1 == 0] = 2
print(array_1)

print("Este array va del 1 al 10 y solo refleja numeros pares: ")
array_2 = np.arange(2,11,2)
print(array_2)


Resultado = 0
for i in array_2:
   Resultado = Resultado + i
print(Resultado)

print("Esta es la suma del array_2: ")
print(sum(array_2))
# "o"
Resultado2 = sum(array_2)
print(Resultado2)

print("Este es el array_2 invertido: ")
array_invertido = np.flip(array_2)
print(array_invertido)

print("Estos son los numeros comunes entre el array_1 y el array_2: ")
comunes_1 = np.intersect1d(array_1, array_2)
print(comunes_1)

print("Estos son los numeros comunes entre el array_2 y el array_invertido")
comunes_2 = np.intersect1d(array_2, array_invertido)
print(comunes_2)

print("Este es un array de unos el cual la longitud la da el usuario")
long = int(input("De que tamaño desea su array: "))
array_3 = np.ones(long)
print(array_3)