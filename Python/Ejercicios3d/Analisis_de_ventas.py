'''Supongamos que eres el propietario de una tienda en línea y tienes una lista de ventas de los
últimos 30 días. Quieres analizar las ventas por día de la semana para identificar los días de mayor
venta.
Pista 1: Puedes crear dos listas, una con las ventas por cada día del mes como por ejemplo…
ventas = [120, 80, 140, 200, 75, 100, 180, 220, 160, 110, 90, 120, 170, 190, 250, 300, 95, 110,
140, 180, 200, 160, 120, 80, 170, 150, 210, 190, 230, 250]
Y otra lista con los días de la semana:
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", „Domingo“]
Después puedes crear una nueva lista con una entrada por cada día de la semana y usar un bucle
para añadir a esta lista la suma de las ventas correspondientes a cada uno de los días de la
semana.
Pista 2: Puede que necesites una variable que lleve la cuenta del día de la semana actual y se
reinicie a cero cuando llegue al séptimo día. 
'''

#Creamos una lista con las ventas diarias y otra con los dias de la semana

ventas = [120, 80, 140, 200, 75, 100, 180, 220, 160, 110, 90, 120, 170, 
          190, 250, 300, 95, 110, 140, 180, 200, 160, 120, 80, 170, 150, 210, 190, 230, 250]
dias = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]

ventas_totales = [0, 0, 0, 0, 0, 0, 0]

#Creamos un bucle for para añadir los dias y las ventas
indice = 0
for venta in ventas:
    ventas_totales[indice] = ventas_totales[indice] + venta
    indice = indice + 1
    if indice == 7:
        indice = 0

for i in range(len(ventas_totales)):
    print(dias[i], ":", ventas_totales[i])
