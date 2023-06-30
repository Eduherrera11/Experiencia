''' 1. Escribe un programa que pida al usuario un número entero y muestre por pantalla una
estructura como la de más abajo, donde el valor de entrada es el número de estrellas en el
centro de la estructura.
*
**
***
****
*****
****
***
**
* '''

print('Bienvenido al programa')
num = int(input("Introduce un numero entero: "))

for i in range(num+1): 
    print("*"*i)
for i in range(num-1,0,-1):
    print("*"*i)



    
