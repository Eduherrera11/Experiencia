"""GESTIÓN DE VENTAS
Crea un programa que permita gestionar las ventas de una tienda. Utiliza una
estructura de datos adecuada para almacenar la información de las ventas
(por ejemplo, una lista de diccionarios). Implementa dos funciones, una para
agregar el producto vendido con su precio y otro para mostrar las ventas de
productos con sus respectivos precios.
(La base de datos puede tener la forma [{“Producto”: producto1, “Precio”:
precio1}, {“Producto”: producto2, “Precio”: precio2}…])
"""

ventas = []

def agregar_venta(producto, precio):
    # Producto: nombre del producto vendido
    # Precio: precio del producto

    venta = {"Producto" : producto, "Precio" : precio}

    ventas.append(venta)

def mostrar_ventas():
    for venta in ventas:
        print("Producto vendido:", venta["Producto"])
        print("Precio:", venta["Precio"] )
        print("---------")


agregar_venta("KIt de tiempo", 150)
agregar_venta("Sensor de oxigeno", 80)
agregar_venta("Tapa Cadena", 750)

mostrar_ventas()
