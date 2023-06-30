'''PILLANDO SOLTURA: 
1. Escribe un programa en Python para encontrar los elementos duplicados de una lista, 
añadirlos a una nueva lista y borrarlos de la lista. Después imprime una lista con tan solo los 
elementos únicos. 
2. Escribe un programa en Python para unir dos listas y ordenarlas en orden ascendente. 
3. Escribe un script que encuentre el segundo número más grande de una lista. 
4. Crea un script que cuente el número de elementos más grandes que un determinado número 
dado por el usuario (supón una lista numérica). 
5. Crea un script dado un número introducido por el usuario o determinado al inicio del 
programa, realice la suma de aquellos números que sean divisibles por este. 
6. Escribe un script que pida un número al usuario y dada una lista encuentre el número más alto 
que es inferior al número introducido o determinado al inicio del programa. 
7. Crea un script que extraiga los elementos comunes entre dos listas. 
8. Crea un script que cuente el número de apariciones de un elemento de una lista en dicha lista 
(P.e. en la lista lista=[23, 65, 23] el número de apariciones de 23 es 2) 
9. Escribe un programa que lea una lista de enteros y cree una nueva lista que contenga solo 
números positivos de la lista original. 
10. Crea un script que tome una lista de strings y cree una nueva lista que contenga el tamaño de 
los strings de la lista original. 
11. Crea un programa que dada una lista de strings, devuelva otra lista con los strings en 
mayúscula.'''

lista = [1,2,3,4,5,6,3,7,8,9,8,10]
print("Lista original ", lista)
elementos_duplicados = []
elementos_unicos = []
for elemento in lista:
    if lista.count(elemento) > 1:
        if elemento not in elementos_duplicados:
           elementos_duplicados.append(elemento)
    else:
                 elementos_unicos.append(elemento)
print('Los elementos unicos son ', elementos_unicos)
print('Los elementos duplicados son ', elementos_duplicados)

lista_resultante = elementos_duplicados + elementos_unicos
lista_resultante.reverse()
print(lista_resultante)

maximo = max(lista_resultante)-1
print(maximo)
print(lista_resultante[1])
print(lista)

suma = 0
num = int(input('introduce un numero: '))
for elemento in lista:
    if num < elemento:
        suma = elemento + suma
print(suma)

x = 2
y = 0
for elemento in lista:
    if elemento % x == 0:
       y = elemento + y
print(y)

lista2 = []
num1 = int(input('introduce un numero: '))
for elemento in lista:
    if num1 > elemento:
        lista2.append(elemento)
print(max(lista2))

comunes = []
for elemento in lista:
   if elemento in elementos_unicos:
               comunes.append(elemento)
print(comunes)

lista3 = [23, 2, 3, 23, 23, 23]
repetido = 0
repetidos = 1
for elemento in lista3:
     if elemento == elemento:
          repetido = elemento
          repetidos = repetidos + 1 
print('el elemento ', repetido, ' se repite ', repetidos)

        

