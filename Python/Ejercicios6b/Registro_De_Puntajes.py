"""Implementa un programa en Python que permita registrar y mantener un
seguimiento de los puntajes de un juego. El programa debe permitir a los
jugadores ingresar sus nombres y puntajes, almacenarlos en un
diccionario y proporcionar funcionalidades para mostrar el puntaje más
alto, el promedio de puntajes y la cantidad total de jugadores."""

# Base de datos de puntajes
registro = {}
continuar = True

# Seguimiento de los puntajes actualizados
while continuar:
    # Pedir al usuario su nombre
    nombre = input("Ingrese nombre del jugador (o salir para terminar): ")
    if nombre.lower() == "salir":
        continuar = False
    else:
        puntaje = int(input("Ingrese el puntaje del jugador: "))
        registro[nombre] = puntaje
print(registro)

# Obtener puntaje mas alto
jugador_mas_alto = max(registro, key=registro.get)
puntaje_mas_alto = registro[jugador_mas_alto]
print("El jugador con el puntaje mas alto es: ", jugador_mas_alto)
print("El puntaje es:", puntaje_mas_alto)

# Obtener el promedio de puntajes
total_puntajes = sum(registro.values())
cantidad_de_jugadores = len(registro)
promedio = total_puntajes/cantidad_de_jugadores
print("El promedio de los puntajes es: ", promedio)

# Obtener la cantidad de jugadores
print("La cantidad de jugadores es: ", cantidad_de_jugadores)