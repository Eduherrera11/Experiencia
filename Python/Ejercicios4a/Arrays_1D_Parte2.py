import numpy as np

print("----------------------------------------------")
print("Array de 15 espacios con numeros aletorios de 1 al 100")
array = np.random.randint(1, 100, 15)
print(array)

print("------------------------------------------------")
print("Multiplicamos todos los elementos del array anterior")
array_multi = array*10
print(array_multi)
#"o"
for i in range(len(array)):
    array_multi[i] *= 10
print(array_multi)

print("--------------------------------------------------")
print("Array con 15 numeros aleatorios entre el 0 y el 1")
array_1 = np.random.rand(15)
print(array_1)

print("---------------------------------------------------")
print("Suma de elementos de ambos arrays")
array_2 = (array + array_1)
print(array_2)

print("----------------------------------------------------")
print("Resta de elementos de ambos arrays")
array_3 = (array_2 - array_1)
print(array_3)

print("-------------------------------------------------------")
print("Multiplicamos un array con otro")
array_4 = array*array_3
print(array_4)

print("-------------------------------------------------------")
print("Valor mas alto del primer array")
Max_Valor = (max(array))
print(Max_Valor)

print("---------------------------------------------------------")
print("Media del primer array")
Media = np.mean(array)
print(Media)

print("---------------------------------------------------------")
print("Mediana del primer array")
Mediana = np.median(array)
print(Mediana)

print("---------------------------------------------------------")
print("Desviacion estandar del primer array")
Desviacion = np.std(array)
print(Desviacion)