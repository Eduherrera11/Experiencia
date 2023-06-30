"""Supongamos que tienes los resultados de una elección con los nombres
de los candidatos y la cantidad de votos obtenidos por cada uno.
Implementa un programa en Python que permita registrar los votos,
mostrar la lista completa de candidatos y sus votos, encontrar al
candidato ganador (con más votos) y calcular el porcentaje de votos que
obtuvo cada candidato."""

resultados = {}
continuar = True

while continuar:
    print("1. Registrar votos")
    print("2. Mostrar lista de candidatos y votos")
    print("3.  Encontrar candidato ganador")
    print("4. Calcular porcentaje de votos")
    print("5. Salir")
    opcion = str(input("Elige una opcion: "))

    if opcion == "1":
        candidato = input("Escribe el nombre del candidato: ")
        if candidato in resultados:
            resultados[candidato] = resultados[candidato] + 1
        else:
            resultados[candidato] = 1 
        print("Voto registrado satisfactoriamente")

    elif opcion == "2":
        if len(resultados) == 0:
                print("No hay candidatos registrados")
        else:
            for candidato, votos in resultados.items():
                print(f"El candidato {candidato.title()} tiene {votos} votos")
    
    elif opcion == "3":
        if len(resultados) == 0:
            print("No hay candidatos registrados")
        else:
            ganador = max(resultados, key = resultados.get)
            print(f"El candidato ganador es: {ganador}")

    elif opcion == "4":
        if len(resultados) == 0:
            print("No hay candidatos registrados")
        else:
            total_votos = sum(resultados.values())
            for candidato, votos in resultados.items():
                porcentaje = (votos/total_votos)*100
                print(f"El porcentaje de votos del candidato {candidato} es {porcentaje}%")

    elif opcion == "5":
        print("Saliendo del programa...")
        continuar = False
    
    else:
        print("Elije una opcion valida")





            



            
         

