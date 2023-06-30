print("Bienvenido a Ewa Buger's")

name = str(input("Indique su nombre por favor: "))
orden = float(input("Que hambuergesa desea:\n\
                     hamburguesa clasica marque 1\n\
                     hamburguesa vegana marque 2 \n\
                        "))

if orden == 1:
   print("Ha seleccionado la hamburguesa clasica")
elif orden == 2:
    print("Ha seleccionado la hamburguesa vegana")
else:
    print("Hay un error en la seleccion")

num1 = str(input("Desea agregar ingredientes extras? "))

if (num1.title() == "Si") and (orden == 1):
    ingredientes = str(input("Desea agregarle queso pasteurizado? "))
    if (num1.title() == "Si") and (orden == 1):
       ingredientes1 = str(input("Desea agregarle Bacon? "))
       if (num1.title() == "Si") and (orden == 1):
           ingredientes2 = str(input("Desea agregarle Huevo? "))
elif (num1.title() == "Si") and (orden == 2):
    ingredientes3 = str(input("Desea agregarle Tofu? "))
    if (num1.title() == "Si") and (orden == 2):
       ingredientes4 = str(input("Desea agregarle Cebolla Caramelizada? "))
elif(num1.title() == "No"):
    print("No desea ingredientes extra")

if (num1.title() == "Si") and (orden == 1):
    print("Su pedido es: \n\
           Una Hamburguesa Clasia\n\
           Ingredientes extras selecionados son: \n\
           Queso Pasteurizado", ingredientes, " \n\
           Bacon", ingredientes1, " \n\
           HUevo", ingredientes2)

elif (num1.title() == "Si") and (orden == 2):
    print("Su pedido es: \n\
           Una Hamburguesa Vegana\n\
           Ingredientes extras selecionados son: \n\
           Tofu", ingredientes3, " \n\
           Cebolla Caramelizada", ingredientes4)
elif(num1.title() == "No"):
    print("No desea ingredientes extra")

print("Buen apetito ", name.title())


