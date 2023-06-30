"""Tienes una tienda y deseas realizar un seguimiento de las ventas diarias
de tus productos. Cada producto tiene un nombre y una cantidad
vendida. Implementa un programa en Python que utilice un diccionario
para almacenar la información de las ventas. El programa debe permitir
registrar las ventas de productos, actualizar la cantidad vendida de un
producto existente y calcular el total de ventas diarias.
(Pista: puedes comenzar con un diccionario vacío e ir añadiendo cada
producto) """

# Base de datos de ventas
ventas_diarias = {}
continuar = True

while continuar == True:
    opcion = input("1. Registrar venta\n2. Actualizar cantidad vendida\n3. Total de ventas\n4. Salir\nElige una opcion: ")

# Registro de ventas
    if opcion == "1":
        producto = input("Ingrese el producto: ")
        cantidad = int(input("Ingrese la cantidad: "))
        if producto in ventas_diarias:
            ventas_diarias[producto] += cantidad
        else:
            ventas_diarias[producto] = cantidad
    
# Actualizar las ventas
    elif opcion == "2":
        producto = input("Ingrese el producto: ")
        if producto in ventas_diarias:
            nueva_cantidad = int(input("Ingrese la nueva cantidad: "))
            ventas_diarias[producto] = nueva_cantidad
        else:
            print("El producto ingresado no esta en el registro")

# Total de ventas  
    elif opcion == "3":
        total_ventas = sum(ventas_diarias.values())
        print("El total de las ventas es: ", total_ventas)

# Salir del programa
    elif opcion == "4":
        print("Saliendo del programa...")
        continuar = False

    else:
        print("opcion invalida por favor elija una opcion valida")
