'''Una red social tiene una base de datos de usuarios y sus correspondientes amistades.
Crea un programa que tome una base de datos de una red social como una lista de
tuplas, donde cada tupla contiene el nombre del usuario y una lista de sus amigos. Los
nombres repetidos en la lista de amigos corresponden a usuarios con varias cuentas
diferentes. Deberas eliminar las cuentas duplicadas y después devolver una tupla de
tuplas que contiene el número real de amigos por usuario y el usuario con más amigos.
Pista 1: Tus datos de entrada podrían ser así —> red_social = [("Juan", ["Maria", "Pedro",
"Luis"]), ("Maria", ["Juan", “Pedro”,”Juan”]), ("Pedro", ["Juan", "Maria"]), ("Luis", [“Juan”])]
Pista 2: Para eliminar duplicidades puedes usar sets '''

red_social = [('Juan', ['Maria', 'Pedro', 'Luis']), ('Maria', ['Juan', 'Pedro', 'Juan']), ('Pedro', ['Juan', 'Maria']), ('Luis', ['Juan'])]

red_social_sin_duplicados = []
for usuario, amigos in red_social:
    amigos_sin_duplicados = list(set(amigos))
    red_social_sin_duplicados.append((usuario, amigos_sin_duplicados))
print(red_social_sin_duplicados)

amigos_por_usuario = []
for usuario, amigos in red_social_sin_duplicados:
    amigos_por_usuario.append((usuario, len(amigos)))
print(amigos_por_usuario)

lista_usuario = [tupla[0] for tupla in amigos_por_usuario]
numeros_amigos = [tupla[1] for tupla in amigos_por_usuario]

maximo = max(numeros_amigos)
print(maximo)

   
