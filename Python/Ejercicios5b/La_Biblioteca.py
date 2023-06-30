'''Una biblioteca tiene una lista de libros y sus autores. Crea un programa que tome la lista
de libros y sus autores como una lista de tuplas, donde cada tupla contiene el título del
libro y el nombre del autor, y devuelva una nueva lista de tuplas que contenga el título del
libro y el apellido del autor.
Pista: Tus datos de entrada podrían ser así —> lista_libros = [(‘El aleph', ‘Jorge Luis
Borges'), ('Cien años de soledad', ‘Garbriel Garcia Márquez'), ('La ciudad y los perros',
‘Mario Vargas Llosa')] '''

lista_libros = [('El aleph', 'Jorge Luis Borges'), ('Cien años de soledad', 'Gabriel Garcia Marquez'), ('La ciudad y los perros', 'Maria Vargas Llosa')]

lista_nueva = []
for tupla in lista_libros:
    titulo,autor = tupla
    apellido = autor.split()[-1]
    lista_nueva.append((titulo,apellido))
print(lista_nueva)