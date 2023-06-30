"""Eres un profesor y deseas realizar un seguimiento de la asistencia de tus
estudiantes a lo largo del semestre. Cada estudiante tiene un nombre y
una lista de fechas en las que asistió a clases. Implementa un programa
en Python que utilice un diccionario para almacenar la información de las
asistencias. El programa debe permitir registrar la asistencia de los
estudiantes, agregar nuevas fechas de asistencia y mostrar la lista de
estudiantes y las fechas en las que asistieron.
(Pista: puedes comenzar con un diccionario vacío y construir un
diccionario de listas) """

asistencias = {}

# Registrar asistencias
asistencias["Eduardo"] = ["01-01-2023", "02-01-2023", "03-01-2023"]
asistencias["Carlos"] = ["01-01-2023", "02-01-2023", "03-01-2023"]
asistencias["Ewa"] = ["01-01-2023", "02-01-2023", "03-01-2023"]

# Agregar nuevas asistencias a estudiantes
asistencias["Eduardo"].append("01-02-2023")

# Mostrar la lista de estudiantes y las fechas
for estudiante, fechas in asistencias.items():
    print("El estudiante: ", estudiante)
    print("Asistio los siguientes dias: ", fechas)
    print()