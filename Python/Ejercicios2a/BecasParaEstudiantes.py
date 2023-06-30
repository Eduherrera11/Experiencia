print("Bienvenido al programa para optar a una beca")

name = input("indique su nombre: ")
edad = float(input("indique su edad: "))
nota = float(input("cual es el promedio de sus notas: "))

if (edad < 22) and (edad > 16):
    print("tienes la edad requerida para optar a la beca")
    if (nota > 7):
       print("Tienes los requisitos necesarios... FELICIDADES", name.title()," OBTIENES UNA BECA")
    else:
        print("No tienes la nota requerida, lo sentimos")
else:
    print("No tienes la edad requerida, lo sentimos")