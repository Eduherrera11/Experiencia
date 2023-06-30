'''Define una lista de 5 palabras aleatorias y una lista de letras prohibidas que contenga tres letras. 
Filtra las palabras en tu lista original crea una nueva lista de palabras filtradas que solo contenga 
aquellas palabras que no tienen ninguna letra prohibida.'''

list = ['casa', 'lana', 'corazon', 'estereo', 'pelo']
carac = ['e', 'o', 'r']
lista = []


for palabra in list:
    incluir = True
    
    for letra in carac:
        if letra in palabra:
            incluir = False

    if incluir:
        lista.append(palabra)
print(lista)

    