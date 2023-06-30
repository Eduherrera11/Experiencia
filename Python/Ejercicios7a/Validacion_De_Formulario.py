"""Crea un programa que valide un formulario de registro. Crea una función
llamada validar_formulario que reciba diferentes campos de un formulario
(nombre, correo electrónico y número de teléfono) y verifique si los valores
ingresados cumplen con los requisitos especificados, siendo estos:
1. Que el nombre tenga una longitud minima de 3 caracteres
2. Que el teléfono este conformado por dígitos y tenga una longitud de 9
caracteres
3. Que el email contenga un “@“ y un “.”
"""

def registro(name, account, number):
    "Devuelve un diccionario con la informacion"
    info = {"Nombre" : name, "Correo" : account, "Numero" : number}
    
    if len(name) > 3:
        print(f"Nombre:", name)
    else:
        print("Name: Error")

    if "." and "@" in account:
        print(f"Correo:", account)
    else:
        print("Correo : Error")
    
    if len(number) == 9:
        print(f"Numero: ", number)
    else:
        print("Numero : Error")


print("Iniciando Programa...")

name = input("Coloque su nombre: ")
account = input("Ingrese su correo: ")
number = (input("Ingrese su numero telefonico: "))

registro(name, account, number)