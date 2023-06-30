'''LISTAS NUMERICAS: 
1. Crea una lista llamada “numeros“ que contenga los siguientes numeros enteros: 
[1,2,3,4,5,6,7,8,9,10]. 
2. Crea una nueva lista con los números pares de la lista anterior en orden inverso 
3. Escribe un bucle que recorra la lista “numeros“ e imprima el cuadrado de cada numero por 
consola. 
4. Intenta rehacer los pasos 2 y 3 con el menor número de lineas posible (método de 
compresión). 
5. Usa un método que te devuelva el número más pequeño de la lista e imprímelo por pantalla 
6. Haz lo mismo con el número más alto 
7. Suma todos los elementos de la lista con y sin un bucle. 
8. Encuentra el índice correspondiente al número 8 en la lista original y en la lista resultante tras 
el punto 2. '''

numeros = list(range(1,11))
print(numeros)

pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
numeros_pares_invertidos = pares[::-1]
print(numeros_pares_invertidos)

for numero in numeros:
    print(numero**2)

numeros_pares_invertidos = [numero for numero in numeros if numero % 2 == 0][::-1]
numeros_cuadrados = [numero**2 for numero in numeros]
print(numeros_pares_invertidos)
print(numeros_cuadrados)

minimo = min(numeros)
print("El numero mas pequeno es : ", minimo)

maximo = max(numeros)
print("El numero mas grande es : ", maximo)

suma = sum(numeros)
print('La suma de todos los digitos es: ', suma)

print(numeros[7])
print(numeros_pares_invertidos[1])