'''Trabajas en colegio y estas encargado de mantener un seguimiento de las notas de los 
estudiantes de un clase. En tu base de datos tienes una lista con los nombres de los estudiantes y 
para cada estudiante debes guardar sus notas provenientes de deberes, exámenes y proyectos. 
También necesitas calcular a nota media de cada estudiante y la nota media de la clase al 
completo. 
Pista: Para resolver este problema puedes usar una lista anidada donde guardes las notas para 
cada estudiante. Entonces puedes usar un bucle para recorrer la lista de listas y calcular la nota 
media de cada estudiante. También puedes usar otro bucle para calcular la nota media de toda la 
clase.'''

print("Bienvenido al programa")

estudiantes = ["Eduardo", "Carlos", "Jesus"]
lista = []
lista2 = []
lista3 = []
data_base = [["Eduardo" , [10, 9, 9]],
             ["Carlos" , [7, 8, 6]],
             ["Jesus" , [8.5 ,10 ,9]]]

for data in data_base:
    nombre = data[0]
    notas = data[1]
    nota_total = sum(notas)
    lista.append(nota_total)

for media in lista:
    nota_media = media/len(lista)
    lista2.append(nota_media)

lista3 = sum(lista2)/len(lista2)

print("")
print(f"La nota media de cada estudiante es {estudiantes[0]} : {lista2[0]} \
{estudiantes[1]} : {lista2[1]} \
{estudiantes[2]} : {lista2[2]}")
print("")
print(f"La media de la clase es {lista3}")