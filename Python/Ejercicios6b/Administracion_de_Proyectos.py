"""Eres un gerente de proyectos y necesitas un programa para administrar
las tareas y responsabilidades de tu equipo. Cada tarea tiene un nombre,
una descripción y un responsable asignado. Implementa un programa en
Python que utilice un diccionario para almacenar la información de las
tareas. El programa debe permitir agregar nuevas tareas, asignar
responsables a las tareas existentes, actualizar las descripciones de las
tareas y mostrar la lista completa de tareas y responsables.
(Pista: puedes comenzar con un diccionario vacío y construir un
diccionario de diccionarios) """

Tareas = {}

# Registrar tareas
Tareas["Tarea1"] = {"Descripcion" : "Desarrollar un programa web", "Responsable" : "Eduardo"}
Tareas["Tarea2"] = {"Descripcion" : "Aprender python", "Responsable" : "Herrera"}
Tareas["Tarea3"] = {"Descripcion" : "Ser el mejor desarrollador full-stack del mundo", "Responsable" : "Ewa"}

# Cambiar responsables
Tareas["Tarea1"]["Responsable"] = "Ewa"
Tareas["Tarea3"]["Responsable"] = "Eduardo"

# Cmabiar Descripciones
Tareas["Tarea2"]["Descripcion"] = "Graduarte como programador"
Tareas["Tarea3"]["Descripcion"] = "Ganar mas de 100 mil dolares netos anualmente"

# Lista de responsables
for tarea, detalles in Tareas.items():
    print("Tarea: ", tarea)
    print("Descripcion: ", detalles["Descripcion"])
    print("Responsable: ", detalles["Responsable"])
    print()
