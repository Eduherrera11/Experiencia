import numpy as np

print("-------------------------------------")
print("Este array estara lleno de 1s y el usuario sera quien determine su longitud")
long = int(input("Determine la longitud del array: "))
array = np.ones(long)
print(array)

print("----------------------------------------")
print("Cambiaremos la dimension del array")
filas = int(input("Seleccione las filas que tendra el array: "))
columnas = int(input("Seleccione las columnas que tendra el array: "))
if filas * columnas == long:
   nuevo_array = np.reshape(array, (filas,columnas))
   print("Array con nueva forma \n", nuevo_array)
   matriz_identidad = np.eye(filas,columnas)
   print("La matriz identidad es:\n", matriz_identidad)
else: 
   print("La cantidad de filas y columnas no es igual a la longitud")


