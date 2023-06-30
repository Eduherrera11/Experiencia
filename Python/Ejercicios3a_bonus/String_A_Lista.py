'''STRING A LISTA: 
Desarrolla un script en Python que dado una cadena de caracteres con la siguiente información: 
nombre, apellido, DNI, código_asignatura, convocatoria, nota1, nota2, nota3 … Por ejemplo: 
David Fernandez 12311267A 43527 2 2.1 4.6 3.4. El script debe crear una lista con esos datos, 
introducirlo en una lista de listas donde se encuentra la información de todos los alumnos e 
imprimir la nota media de los alumnos junto con el DNI. 
Supón ahora que tu input es un string como este: 
‘’'David Fernandez 12311267A 43527 2 9.1 7.6 2.4\n 
Maria Garcia 12316487A 43527 2 7.1 8.6 5.4\n 
Juan Perez 647829236A 43527 2 8.1 8.5 8.4\n ‚’’ 
Reescribe el script para que procese ese input adecuadamente e imprima la nota media y el DNI 
de todos los alumnos en ese string.'''

print("Bienvenido al programa")
name = str(input('Escriba su nombre: '))
apellido = str(input('Escriba su apellido: '))
dni = int(input('Escriba si DNI: '))
codigo_asignatura = int(input("Cual es el codigo de su asignatura: "))
nota1 = int(input('Nota 1: '))
nota2 = int(input('Nota 2: '))
nota3 = int(input('Nota 3: '))

list = []
list.append(name.title())
list.append(apellido.title())
list.append(dni)
list.append(codigo_asignatura)
list.append(nota1)
list.append(nota2)
list.append(nota3)

Gran_list = []
Gran_list.append(list)

name = str(input('Escriba su nombre: '))
apellido = str(input('Escriba su apellido: '))
dni = int(input('Escriba si DNI: '))
codigo_asignatura = int(input("Cual es el codigo de su asignatura: "))
nota1 = int(input('Nota 1: '))
nota2 = int(input('Nota 2: '))
nota3 = int(input('Nota 3: '))

list = []
list.append(name.title())
list.append(apellido.title())
list.append(dni)
list.append(codigo_asignatura)
list.append(nota1)
list.append(nota2)
list.append(nota3)

Gran_list.append(list)

name = str(input('Escriba su nombre: '))
apellido = str(input('Escriba su apellido: '))
dni = int(input('Escriba si DNI: '))
codigo_asignatura = int(input("Cual es el codigo de su asignatura: "))
nota1 = int(input('Nota 1: '))
nota2 = int(input('Nota 2: '))
nota3 = int(input('Nota 3: '))

list = []
list.append(name.title())
list.append(apellido.title())
list.append(dni)
list.append(codigo_asignatura)
list.append(nota1)
list.append(nota2)
list.append(nota3)

Gran_list.append(list)
print(Gran_list)

DNI_Total = []
DNI_Total.append(Gran_list[0][2])
DNI_Total.append(Gran_list[1][2])
DNI_Total.append(Gran_list[2][2])

print('Los DNI de los estudiantes ingresados son: ', DNI_Total)

Nota_Total = []
Nota_Total.append(Gran_list[0][4])
Nota_Total.append(Gran_list[0][5])
Nota_Total.append(Gran_list[0][6])
Nota_Total1 = sum(Nota_Total)/3

Nota_Total = []
Nota_Total.append(Gran_list[1][4])
Nota_Total.append(Gran_list[1][5])
Nota_Total.append(Gran_list[1][6])
Nota_Total2 = sum(Nota_Total)/3

Nota_Total = []
Nota_Total.append(Gran_list[2][4])
Nota_Total.append(Gran_list[2][5])
Nota_Total.append(Gran_list[2][6])
Nota_Total3 = sum(Nota_Total)/3

Promedio = []
Promedio.append(Nota_Total1)
Promedio.append(Nota_Total2)
Promedio.append(Nota_Total3)

print('El promedio de las notas de los es tudiantes es: \n\
      ', Gran_list[0][0], ' = ', Nota_Total1, \
        Gran_list[1][0], ' = ', Nota_Total2, \
          Gran_list[2][0], ' = ', Nota_Total3)

