'''Crea un programa en el que se pregunte al usuario por una frase y una letra, y muestre por
pantalla el número de veces que aparece la letra en la frase.'''

frase = str(input("Ingrese una frase: "))
letra = str(input("Igrese una letra: "))
contador = 0

for caracter in frase:
    if letra == caracter:
      contador = contador + 1

print("Las veces que se repite ", letra, " son ", contador)