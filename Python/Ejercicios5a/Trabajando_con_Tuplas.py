'''1. Crea una tupla con tres elementos y imprime por pantalla cada uno de ellos en una
nueva linea.
2. Crea una lista con tres elementos e intenta modificarla. Haz lo mismo con la tupla.
¿Cuáles son las diferencias?
3. Crea una tupla de enteros y devuelve la suma de los elementos.
4. Crea un script que dada una tupla que contiene strings cree una nueva tupla con el
primer caracter de cada string.
5. Crea un script que dada una tupla de números devuelva el producto de todos los
números pares.
6. Crea un script que dada una tupla de números, devuelva la tupla con los numeros
ordeandos en orden descendente.
7. Crea un script que dada una tupla con números enteros repetidos, elimine los
duplicados. (Puedes usar sets).
8. Crea un script que dada una tupla y un numero entero, devuelve verdadero si el
numero se encuentra en la tupla y falso en el caso contrario.
9. Crea un script que dadas dos tuplas cree una tupla resultante de la union de ambas.
10. Crea un script que dada una tupla de números devuelva e máximo y el mínimo.
11. Crea un script que dada una tupla con strings devuelva el string más largo y el más
corto. (Prueba añadiendo key=len a las funciones max y min).
12. Crea un script que dada una tupla devuelva el contenido en orden revertido.
13. Crea un script que dada una tupla de tuplas, donde cada tupla interna contiene dos
elementos, devuelva una nueva tupla en la que cada elemento sea la suma de los dos
elementos de la tupla interna correspondiente.'''

#1 Creando un tupla
tupla = (49 , 'carro', False)
for elemento in tupla:
    print(elemento)
print('---------------------------')

#2 Intentando modificar elementos de una tupla
lista = [58, 'perro', True]
lista[2] = False
print(lista)

##tupla[0] = 50
##print(tupla) la terminal arroja un error debido a que las tuplas no se modifican
print('------------------------------')

#3 Suma de los elementos de una tupla
tupla = (49, 50, 1, 1)
print(sum(tupla))
print('----------------------------')

#4 Crea un script que dada una tupla que contiene strings cree una nueva tupla con el primer caracter de cada string.
tupla = ('carro', 'perro', 'pelota')
lista = []
for palabra in tupla:
    lista.append(palabra[0])
nueva_tupla = tuple(lista)
print(nueva_tupla)

nueva_tupla2 = tuple(palabra[0] for palabra in tupla)
print(nueva_tupla2)
print('---------------------------------')

#5 Crea un script que dada una tupla de números devuelva el producto de todos los números pares
tupla = (10, 5, 2, 80, 7, 12)
producto = 1
for num in tupla:
    if num % 2 == 0:
       producto = producto * num
print(producto)
print('-----------------------------')

#6 Crea un script que dada una tupla de números, devuelva la tupla con los numeros ordeandos en orden descendente.
tupla = (10, 8, 4, 7, 5, 6, 2, 1, 3, 9)
tupla = sorted(tupla)
print(list(reversed(tupla)))
print('-----------------------------------')

#7 Crea un script que dada una tupla con números enteros repetidos, elimine los duplicados. (Puedes usar sets).
tupla = (1, 1, 1, 2, 2, 2, 3, 3, 3)
print(tuple(set(tupla)))
print('-------------------------------')

#8 Crea un script que dada una tupla y un numero entero, devuelve verdadero si el numero se encuentra en la tupla y falso en el caso contrario.
tupla = (1, 2, 3, 4, 5, 6)
print(1 in tupla)
print(10 in tupla)
print('-----------------------------')

#9 Crea un script que dadas dos tuplas cree una tupla resultante de la union de ambas.
tupla1 = (2, 'carro', False)
tupla2 = ('camioneta', 1, True)
tupla_resultante = tupla1 + tupla2
print(tupla_resultante)
print('------------------------------')

#10 Crea un script que dada una tupla de números devuelva e máximo y el mínimo.
tupla = (1, 5, 2, 8, 3, 10) 
print((max(tupla)), (min(tupla)))
print('------------------------------')

#11 Crea un script que dada una tupla con strings devuelva el string más largo y el más corto. (Prueba añadiendo key=len a las funciones max y min).
tupla = ('carro', 'camioneta', 'carretera', 'terrenator')
maximo = max(tupla, key = len)
minimo = min(tupla, key = len)
print(minimo, maximo)
print('-------------------------------')

#12 Crea un script que dada una tupla devuelva el contenido en orden revertido.
tupla = (1, 2, 3, 4, 5)
##print(tuple(list(reversed(tupla))))
print(tupla[::-1])
print("--------------------------------")

#13 Crea un script que dada una tupla de tuplas, donde cada tupla interna contiene dos
#elementos, devuelva una nueva tupla en la que cada elemento sea la suma de los dos
#elementos de la tupla interna correspondiente.

tupla = ((2, 8), (4, 6), (10, 0))
nueva_tupla = []
for elemento in tupla:
    suma = sum(elemento)
    nueva_tupla.append(suma)
print(tuple(nueva_tupla))

nueva_tupla = tuple(sum(elemento) for elemento in tupla)
print(nueva_tupla)



