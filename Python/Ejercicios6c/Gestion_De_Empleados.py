'''Imagina que eres el gerente de recursos humanos de una empresa y
necesitas gestionar la información de los empleados. Cada empleado
tiene un nombre, salario y departamento al que pertenece. Implementa
un programa en Python que permita agregar nuevos empleados,
actualizar el salario de un empleado existente, mostrar la lista completa
de empleados y calcular el promedio salarial por departamento.'''

sistema = {}
continuar = True

# Menu de opciones
while continuar == True:
    opcion = input("1. Agregar empleado\n2. Actualizar datos del empleado\n3. Mostrar lista de empleados\n4. Calcular promedio de salarios por departamento\n5. Salir\nElige una opcion: ")

# Agregar empleado
    if opcion == "1":
        nombre = str(input("Escirbe el nombre: "))
        departamento = str(input("Cual es su departamento: "))
        salario = int(input("Cuanto gana: "))
        sistema[nombre] = {"departamento" : departamento, "salario" : salario}
    
# Actualizar datos de empleado
    elif opcion == "2":
        nombre_act = str(input("Escribe el nombre del empleado: "))
        if nombre_act in sistema.keys():
            departamento = str(input("Cual es su departamento: "))
            salario = int(input("Cuanto gana: "))
            sistema[nombre] = {"departamento" : departamento, "salario" : salario}
        else:
            print("El empleado no esta registrado")

# Imprimir la lista completa de usuarios y datos   
    elif opcion == "3":
        for empleado, datos in sistema.items():
            departamento = datos["departamento"]
            salario = datos["salario"]
            print("EL empleado", empleado.title(), "pertenece al departamento de", departamento, "y gana", salario,"Dolares")
            print("")

# Imprimir promedio de salarios en departamentos
    elif opcion == "4":
        departamento = input("Ingrese un departamento: ")
        total_salarios = 0
        contador = 0
        for dato in sistema.values():
            if dato["departamento"] == departamento:
                total_salarios = total_salarios + dato["salario"]
                contador = contador + 1
        if contador > 0:
             promedio = total_salarios/contador
             print(promedio)
        else:
            print("No hay empleados en el departamento")

# Salida del programa
    elif opcion == "5":
        print("Cerrando el programa...")
        continuar = False
    
    else:
        print("Opcion invalida")