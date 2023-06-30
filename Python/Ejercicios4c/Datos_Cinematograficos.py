'''Supongamos que tienes un conjunto de datos de películas que contiene información
sobre su título, género, duración, año de lanzamiento y calificación. Quieres analizar
estos datos para determinar cuál es el género de película más popular, cuántas películas
se lanzaron en cada década y cuál es la duración promedio de cada género de película.'''

# IMPORTAR MODULOS
import numpy as np

# Datos
peliculas = np.array([
    ['Peli 1', 'Comedia', 120, 1990, 8.5],
    ['Peli 2', 'Accion', 110, 2005, 7.8],
    ['Peli 3', 'Drama', 95, 2010, 6.9],
    ['Peli 4', 'Comedia', 100, 1985, 7.5],
    ['Peli 5', 'Accion', 130, 2015, 8.1],
    ['Peli 6', 'Drama', 115, 2000, 6.7],
    ['Peli 7', 'Comedia', 90, 1995, 8.2],
    ['Peli 8', 'Accion', 105, 2010, 7.4],
    ['Peli 9', 'Drama', 125, 1980, 6.8],
    ['Peli 10', 'Comedia', 95, 2000, 8.0]
])  

# FILTRAR DATOS
genero = peliculas[:,1]
decada = peliculas[:,3]

elementos_unicos, conteos = np.unique(genero , return_counts = True)
#print(elementos_unicos)
#print(conteos)

genero_comedia = np.array([])
genero_accion = np.array([])
genero_drama = np.array([])
for i in range(10):
    if genero[i] == genero[0]:
        genero_comedia = np.append(genero_comedia, peliculas[i])
    elif genero[i] == genero[1]:
        genero_accion = np.append(genero_accion, peliculas[i])
    elif genero[i] == genero[2]:
        genero_drama = np.append(genero_drama, peliculas[i])

# CALCULAR DURACION PROMEDIO
genero_comedia1 = genero_comedia.reshape((4, 5))
genero_accion1 = genero_accion.reshape((3, 5))
genero_drama1 = genero_drama.reshape((3, 5))
#print(genero_comedia1)

duracion = genero_comedia1[:,2]
duracion2 = genero_accion1[:,2]
duracion3 = genero_drama1[:,2]
#print(duracion)

duracion = duracion.astype(int)
duracion2 = duracion2.astype(int)
duracion3 = duracion3.astype(int)
#print(duracion)

promedio = np.mean(duracion)
promedio2 = np.mean(duracion2)
promedio3 = np.mean(duracion3)

# IMPRIMIMOS EL PROMEDIO 
print("El promedio de la duracion del genero ", elementos_unicos[0], "es", promedio)
print("El promedio de la duracion del genero ", elementos_unicos[1], "es", promedio2)
print("El promedio de la duracion del genero ", elementos_unicos[2], "es", promedio3)
print('--------------------------------------------------------------------')

decada = decada.astype(int)
#print(decada)


decada1 = 0
decada2 = 0
decada3 = 0
decada4 = 0
for j in decada:
    if (j >= 1980 and j < 1990):
        decada1 = decada1 + 1
    if (j >= 1990 and j < 2000):
        decada2 = decada2 + 1
    if (j >= 2000 and j < 2010):
        decada3 = decada3 + 1
    if (j >= 2010 and j < 2020):
        decada4 = decada4 + 1

# IMPRIMIMOS PELICULAS POR DECADA
print("Las peliculas lanzadas en la decada de los 80's son:", decada1)
print("Las peliculas lanzadas en la decada de los 90's son:", decada2)
print("Las peliculas lanzadas en la decada de los 00's son:", decada3)
print("Las peliculas lanzadas en la decada de los 10's son:", decada4)
print("-----------------------------------------------------")

valoracionC = genero_comedia1[:,4]
valoracion2A = genero_accion1[:,4]
valoracion3D = genero_drama1[:,4]

valoracionC = valoracionC.astype(float)
valoracion2A = valoracion2A.astype(float)
valoracion3D = valoracion3D.astype(float)

valoracion_comedia = np.mean(valoracionC)
valoracion_accion = np.mean(valoracion2A)
valoracion_drama = np.mean(valoracion3D)

if (valoracion_comedia > valoracion_accion and valoracion_comedia > valoracion_drama):
    print("El mejor genero de peliculas es ", genero[0], "con ", valoracion_comedia, " puntos")
elif (valoracion_accion > valoracion_comedia and valoracion_accion > valoracion_drama):
    print("El mejor genero de peliculas es ", genero[1], "con ", valoracion_accion, " puntos")
elif (valoracion_drama > valoracion_accion and valoracion_drama > valoracion_comedia):
    print("El mejor genero de peliculas es ", genero[2], "con ", valoracion_drama, " puntos")
print('-----------------------------------------------------------------------------')
