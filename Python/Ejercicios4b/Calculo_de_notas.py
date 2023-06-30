'''Supongamos que tienes un conjunto de calificaciones de un grupo de estudiantes en un
curso. Cada estudiante tiene cuatro calificaciones: dos exámenes, un trabajo final y una
participación en clase. Quieres calcular la nota final de cada estudiante, donde los
exámenes valen un 30% cada uno, el trabajo final vale un 30% y la participación en clase
vale un 10%. Para ello, puedes usar NumPy para crear un array de 4 columnas y n filas,
donde n es el número de estudiantes. Cada columna representa una de las calificaciones
y cada fila representa un estudiante. Luego, puedes usar operaciones de NumPy para
calcular la nota final de cada estudiante y almacenarla en un nuevo array de una sola
columna.'''

# IMPORTAR MODULOS
import numpy as np

# CALIFICACIONES DE LOS ESTUDIANTES / INPUT
calificaciones = np.array([
    [8, 9, 9, 6],
    [9, 9, 9, 9],
    [5, 4, 7, 4],
    [10, 9, 9, 9],
    [10, 10, 10, 10]
])

# CALCULAR LA NOTA FINAL DE CADA ESTUDIANTE
examen1 = calificaciones[:,0]
examen2 = calificaciones[:,1]
trabajo_final = calificaciones[:,2]
participacion = calificaciones[:,3]

nota_final = examen1*0.3 + examen2*0.3 + trabajo_final*0.3 + participacion*0.1

#IMPRIMIR LAS NOTAS FINALES DE CADA ESTUDIANTES
for i in range(len(nota_final)):
    print("La nota final del estudiante ", i+1, " es ", nota_final[i])
