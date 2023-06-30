print("Inventario De Repuestos Eduardo")

inventario = {}
continuar = True

while continuar:
    print("1. Agregar compra")
    print("2. Registrar venta")
    print("3. Mostrar inventario")
    print("4. Total ganancias")
    print("5. Salir")
    opcion = str(input("Elige una opcion: "))

    if opcion == "1":
        print("Agregando repuesto...")
        codigo = str(input("Escribe el codigo del repuesto: "))
        descripcion = str(input("Coloca una descripcion para el repuesto: "))
        precio = int(input("Pon el precio del repuesto: "))
        marca = str(input("Marca del repuesto: "))
        cantidad = int(input("Cantidad: "))
        inventario[codigo] = {"descripcion" : descripcion, "precio" : precio, "marca" : marca, "cantidad" : cantidad}
        print("Se ha registrado la compra exitosamente")

    elif opcion == "2":
        codigo = str(input("Ingrese el codigo del repuesto vendido: "))
        nueva_cantidad = int(input("Ingrese la cantidad vendida: "))
        total_ganancias_brutas = 0
        if codigo in inventario:
            inventario[codigo][cantidad] =- nueva_cantidad
            print("Se ha registrado la venta exitosamente")
        else:
            print("El codigo no esta en el inventario")
    
    elif opcion == "3":
        if len(inventario) != 0:
            print(inventario)
        else: 
            print("No hay ningun repuesto registrado")

    elif opcion == "4":
        print(f"Las ganancias brutas de las ventas registradas son: {total_ganancias_brutas}")


    elif opcion == "5":
        print("Saliendo del programa...")
        continuar = False
    
    else:
        print("Selecciona una opcion correcta")

print("El programa ha terminado")



