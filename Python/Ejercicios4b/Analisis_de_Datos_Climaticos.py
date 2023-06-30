'''Supongamos que tienes un conjunto de datos de clima que contiene información sobre la
temperatura, la humedad y la presión atmosférica en una ciudad durante un año. Quieres
analizar estos datos para determinar cuál fue la temperatura promedio de cada mes, cuál
fue la humedad promedio y la presión atmosférica promedio durante todo el año. Para
ello, puedes usar NumPy para cargar los datos en un array de 3 columnas y n filas, donde
n es el número de mediciones. Luego, puedes usar operaciones de NumPy para filtrar los
datos por mes y calcular las medias de temperatura, humedad y presión atmosférica
correspondientes.'''

# IMPORTAR MODULOS
import numpy as np

# DATOS DE CLIMA / INPUT
clima = np.array([
    [20, 70, 1009, 1],
    [21, 80, 1001, 1],
    [25, 70, 1002, 1],
    [30, 90, 1010, 2],
    [22, 85, 1009, 3],
    [29, 85, 1009, 3],
    [21, 70, 1005, 4],
    [21, 90, 1005, 4],
    [20, 70, 1009, 5],
    [21, 80, 1001, 5],
    [25, 70, 1002, 5],
    [30, 90, 1010, 6],
    [22, 85, 1009, 7],
    [29, 85, 1009, 7],
    [21, 70, 1005, 8],
    [21, 90, 1005, 8],
    [20, 70, 1009, 9],
    [21, 80, 1001, 9],
    [25, 70, 1002, 9],
    [30, 90, 1010, 10],
    [22, 85, 1009, 11],
    [29, 85, 1009, 11],
    [21, 70, 1005, 12],
    [21, 90, 1005, 12],
])

# FILTRAR LOS DATOS
meses = clima[:,3]

temperatura = clima[:,0]
mes_temp = np.zeros(12)

humedad = clima[:,1]
mes_humed = np.zeros(12)

presion = clima[:,2]
mes_pres = np.zeros(12)

# CALCULAR LA TEMPERATURA PROMEDIO
for i in range(12):
    mes_temp[i] = np.mean(temperatura[meses == i+1])
    mes_humed[i] = np.mean(humedad[meses == i+1])
    mes_pres[i] = np.mean(presion[meses == i+1])

    print("La temperatura promedio del mes", i+1, "es de", mes_temp[i], "grados")
    print("La humedad promedio del mes", i+1, "es de", mes_humed[i], )
    print("La presion promedio del mes", i+1, "es de", mes_pres[i], )
    print("-----------------------------------------------------------")


    

