'''TRABAJANDO CON DICCIONARIOS:
1. Crea un diccionario vacío llamado “mi_diccionario”.
2. Agrega un par clave-valor a "mi_diccionario" donde la clave sea "nombre" y el valor
sea tu nombre.
3. Accede e imprime el valor asociado con la clave "nombre" en “mi_diccionario".
4. Verifica si la clave "edad" existe en "mi_diccionario". Imprime "True" si existe y "False"
en caso contrario.
5. Crea un diccionario llamado "estudiante" con los siguientes pares clave-valor:
"nombre" con el nombre del alumno, "edad" con su edad y "materia" con su materia
favorita.
6. Actualiza el valor de la clave "edad" en el diccionario "estudiante" para reflejar la edad
actual de tu amigo.
7. Elimina el par clave-valor con la clave "materia" del diccionario “estudiante".
8. Imprime todas las claves en el diccionario “estudiante".
9. Crea un diccionario llamado "agenda" con tres entradas: "Juan" con el valor
"1234567890", "Joana" con el valor "9876543210" y "Jimena" con el valor
“5555555555”.
10.Agrega una nueva entrada al diccionario "agenda" con la clave "Julio" y el valor
“9998887777".
11.Imprime el número de entradas (pares clave-valor) en el diccionario “agenda".
12.Crea una lista llamada "claves" que contenga todas las claves del diccionario
“agenda".
13.Verifica si la clave "Juan" existe en el diccionario "agenda". Imprime "True" si existe y
"False" en caso contrario.
14.Elimina la entrada con la clave “Jimena”.
15.Utiliza un bucle for para iterar sobre todas las claves en el diccionario "agenda" e
imprime cada par clave-valor en el formato "Nombre: Número”.
16.Utiliza el método "get()" para obtener el valor asociado con la clave "Juan" en el
diccionario "agenda". Si la clave no existe, imprime "Clave no encontrada”.
17.Borra todas las entradas del diccionario “agenda”.
LISTAS DE DICCIONARIOS:
18.Crea una lista llamada "estudiantes" que contenga dos diccionarios. Cada diccionario
representa a un estudiante y tiene las claves "nombre" y "edad" con sus respectivos
valores. Recorre la lista e imprime el nombre y edad de cada estudiante.
19.Agrega un nuevo estudiante a la lista "estudiantes" utilizando un diccionario con las
mismas claves "nombre" y "edad". Imprime la lista actualizada.
20.Elimina el segundo estudiante de la lista "estudiantes". Imprime la lista actualizada.
21.Actualiza la edad del primer estudiante en la lista "estudiantes" a un nuevo valor.
Imprime la lista actualizada.
ANIDAMIENTO DE DICCIONARIOS:
22. Crea un diccionario llamado "productos" que contenga dos entradas. Cada entrada
representa un producto y tiene a su vez las claves "nombre" y "precio" con sus
respectivos valores. Recorre el diccionario e imprime el nombre y precio de cada
producto.
23. Agrega un nuevo producto al diccionario "productos" utilizando una nueva clave y
valor. Imprime el diccionario actualizado.
24.Crea un diccionario llamado "equipos" que contenga tres entradas. Cada entrada
representa un equipo deportivo y tiene las claves "nombre" y "jugadores" con sus
respectivos valores. Los valores de "jugadores" deben ser listas con los nombres de
los jugadores. Recorre el diccionario e imprime el nombre del equipo y la lista de
jugadores.
25.Agrega un nuevo equipo al diccionario "equipos" utilizando una nueva clave y valor.
La lista de jugadores debe contener al menos tres nombres. Imprime el diccionario
actualizado.
26.Actualiza la lista de jugadores de uno de los equipos existentes en el diccionario
"equipos". Agrega un nuevo jugador a la lista. Imprime el diccionario actualizado.'''

#1
mi_diccionario = {}
print(type(mi_diccionario))
print("")

#2
mi_diccionario["nombre"] = "eduardo"
print(mi_diccionario)
print("")

#3
print(mi_diccionario["nombre"])
print("")

#4
print("edad" in mi_diccionario)
print("")

#5
estudiante = {"nombre" : "eduardo", "edad" : 19, "materia" : "quimica"}
print(estudiante)
print("")

#6
estudiante["edad"] = 18
print(estudiante)
print("")

#7
del estudiante["materia"]
print(estudiante)
print("")

#8
print(estudiante.keys())
print("")

#9
agenda = {"juan" : 1234567890, "joana" : 9876543210, "jimena" : 5555555555}
print(agenda)
print("")

#10
agenda["julio"] = 9998887777
print(agenda)
print("")

#11
print(len(agenda))
print("")

#12
claves = list(agenda.keys())
print(claves)
print("")

#13
print("Juan" in agenda)
print("")

#14
del claves[3]
print(claves)
print("")

#15
for nombre, numero in agenda.items():
    print("Nombre: ", nombre, " Numero: ", numero)
print("")

#16
if "juan" in agenda:
    print(agenda.get("juan"))
else:
    print("Clave no encontrada")

valor_juan = agenda.get("juan", "Clave no encontrada")
print(valor_juan)
print("")

#17
del agenda

#18
estudiantes = [{"Nombre" : "Eduardo", "Edad": 19},
               {"Nombre" : "Carlos", "Edad" : 11}]
for estudiante in estudiantes:
    nombre = estudiante["Nombre"]
    edad = estudiante["Edad"]
    print("Nombre ", nombre, "Edad ", edad)
print("")

#19
estudiantes.append({"Jesus" : 19})
print(estudiantes)
print(type(estudiantes[2]))
print("")

#20
estudiantes.remove(estudiantes[1])
print(estudiantes)
print("")

#21
estudiante1 = estudiantes[0]
estudiante1["Eduardo"] = 20
print(estudiantes)
print("")

#22
productos = {"Soportes" : {"Corolla 2011" : 180}, 
             "Conjunto" : {"Fortuner" : 220}}
print(productos)
print("")

#23
productos["Sensor maf"] = {"4Runner" : 60}
print(productos)
print("")

#24
equipos = {"Mostoles" : ["Juanma", "Chichero", "Guti"],
           "Porcinos" : ["Ibai", "DJMario", "Spursito"],
           "EL barrio" : ["Ewa", "Romero", "Mbappe"]}
for equipo, jugadores in equipos.items():
    print(equipo)
    print(jugadores)
    print("")
print("")

#25
equipos["Aniquiladores"] = ["Ewita", "Yusu", "Chaifro"]
for equipo, jugadores in equipos.items():
    print(equipo)
    print(jugadores)
    print("")
print("")

#26
equipos["Aniquiladores"].append("Lois")
for equipo, jugadores in equipos.items():
    print(equipo)
    print(jugadores)
    print("")
print("")