print("Bienvenido al programa")

genero = str(input("Eres hombre o mujer: "))

name = str(input("Cual es su nombre? "))

if (genero == "mujer"):
    if (name[0].title() == "E") or (name[0].title() == "F") or (name[0].title() == "G") or (name[0].title() == "H")\
       or (name[0].title() == "I") or (name[0].title() == "J") or (name[0].title() == "K") or (name[0].title() == "L")\
        or (name[0].title() == "M"):
       print("Tu vas a la seccion A")
    else:
        print("Tu vas a la seccion B")
elif (genero == "hombre"):
    if (name[0].title() == "A") or (name[0].title() == "B") or (name[0].title() == "C") or (name[0].title() == "D")\
       or (name[0].title() == "E") or (name[0].title() == "F") or (name[0].title() == "G") or (name[0].title() == "H")\
        or (name[0].title() == "R")  or (name[0].title() == "S")  or (name[0].title() == "T")  or (name[0].title() == "U")\
             or (name[0].title() == "V")  or (name[0].title() == "W")  or (name[0].title() == "X")  or (name[0].title() == "Y")\
                 or (name[0].title() == "Z"):
       print("Tu vas a la seccion A")  
    else:
        print("Tu vas a la clase B")