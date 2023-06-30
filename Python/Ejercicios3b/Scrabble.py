'''SCRABBLE: 
Supongamos una lista de de caracteres llamada “palabras“ que representa una mano de 
Scrabble. Cada string contiene dos caracteres: el primer carácter es la letra de una ficha y el 
segundo el numero que representa los puntos de la ficha. Por ejemplo, el string "A5" representa la 
ficha con la letra A y un valor de 5 puntos. Crea un script que calcule el valor total de los puntos 
en una mano de scrabble. El valor total será la suma de los puntos de todas las fichas de la mano.'''

palabra = [['a',2], ['v',4], ['e',3], ['i',5],['m',4], ['l',5], ['o',3], ['u',5], ['x',10]]
suma = 0
usuario = str(input('Escribe una palabra con las siguientes letras \n\
                    a2 v4 e3 i5 m4 l5 o3 u5 x10: '))
if palabra[0][0] in usuario:
    suma = suma + palabra[0][1]
if palabra[1][0] in usuario:
    suma = suma + palabra[1][1]
if palabra[2][0] in usuario:
    suma = suma + palabra[2][1]
if palabra[3][0] in usuario:
    suma = suma + palabra[3][1]
if palabra[4][0] in usuario:
    suma = suma + palabra[4][1]
if palabra[5][0] in usuario:
    suma = suma + palabra[5][1]
if palabra[6][0] in usuario:
    suma = suma + palabra[6][1]
if palabra[7][0] in usuario:
    suma = suma + palabra[7][1]
if palabra[8][0] in usuario:
    suma = suma + palabra[8][1]
print("Los puntos por la palabra", usuario, " son ", suma)


"""ASI LO HIZO ELENA"""

mano_scrabble = ['A5', 'B3', 'C4', 'H8', 'D10'] 
puntos = 0

for ficha in mano_scrabble:
    puntos = puntos + int(ficha[1:])

print('Los puntos de la mano son ', puntos)