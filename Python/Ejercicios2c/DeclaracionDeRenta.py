print("Bienvenido a la fiscalia")
name = str(input("Indique su nombre: "))

print("Los impuestos por renta son los siguientes: \n\
    si gana menos de 15000 eu anual es del 5% \n\
        entre 15000 y 25000 es de 15% \n\
        entre 25000 y 35000 es de 20% \n\
        entre 35000 y 60000 es de 30% \n\
        mas de 60000 es de 45%")

sueldo = float(input("Cuanto ganas mensualmente? "))

sueldo = (sueldo*12)

if (sueldo <= 15000):
    print("Tu tipo de impositivo es del 5% ")
elif (sueldo > 15000) and (sueldo <= 25000):
    print("Tu tipo de impositivo es del 15% ")
elif (sueldo > 25000) and (sueldo <= 35000):
    print("Tu tipo de impositivo es del 20% ")
elif (sueldo > 35000) and (sueldo <= 60000):
    print("Tu tipo de impositivo es del 30% ")
elif (sueldo > 60000):
    print("Tu tipo de impositivo es del 45% ")
