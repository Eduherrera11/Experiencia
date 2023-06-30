'''Supongamos que trabajas en una empresa que fabrica dispositivos electrónicos y quieres
analizar los datos de calidad de los componentes utilizados en la producción de dichos
dispositivos. Tienes un conjunto de datos que contiene información sobre la fecha de
producción, el tipo de componente, el lote al que pertenece el componente y la
puntuación de calidad del componente (un número entre 0 y 100). Quieres analizar estos
datos para determinar cuál es el tipo de componente con la puntuación de calidad más
alta, cuántos componentes se produjeron en cada mes y cuál es la puntuación de calidad
promedio de cada tipo de componente.'''

#IMPORTAR MODULOS
import numpy as np

#DATOS
datos = np.array([['2022-01-01', 'Componente 1', 'Lote A', 80],
                  ['2022-01-15', 'Componente 1', 'Lote B', 90],
                  ['2022-02-01', 'Componente 2', 'Lote C', 85],
                  ['2022-02-15', 'Componente 2', 'Lote D', 95],
                  ['2022-03-01', 'Componente 1', 'Lote E', 75],
                  ['2022-03-15', 'Componente 2', 'Lote F', 90],
                  ['2022-02-10', 'Componente 2', 'Lote B', 90]])

# FILTRAR DATOS
# COMPONENTE CON LA PUNTUACION MAS ALTA
tipos_de_componentes = datos[:,1]
componentes_unicos = np.unique(tipos_de_componentes)
#print(componentes_unicos)
calidad = datos[:,3].astype(float)
promedios = np.zeros(len(componentes_unicos))
i = 0
for tipo in componentes_unicos:
    ##print(tipo)
    ##print(calidad[tipos_de_componentes == tipo])
    promedios[i] = np.mean(calidad[tipos_de_componentes == tipo ])
    i = i + 1

##print(promedios)
indice_max = np.argmax(promedios)
tipo_mejor_calidad = componentes_unicos[indice_max]

print("El componente con la puntuacion mas alta es: ", tipo_mejor_calidad)

# CUANTOS SE PRODUJERON POR MES
fechas = datos[:,0]
meses, conteos = np.unique([fecha[0:7] for fecha in fechas], return_counts = True)

for i in range(len(meses)):
    print("Los componentes vendidos en el mes ", meses[i], "son ", conteos[i])

# PUNTUACION PROMEDIO
promedio_por_tipo = np.zeros(len(componentes_unicos))
for i in range(len(componentes_unicos)):
    promedio_por_tipo[i] = np.mean(calidad[componentes_unicos[i] == tipos_de_componentes])
    print("La puntuacion del ", componentes_unicos[i], "es ", promedio_por_tipo[i])




