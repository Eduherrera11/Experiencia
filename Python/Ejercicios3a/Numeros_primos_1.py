'''Crea un programa que imprima todos los números primos entre el 2 y el 100. Un numero primo es
un numero positivo y entero mayor que uno que no tiene un divisor positivo y entero que no sea 1
o sí mismo. '''

print("Bienvenido al programa")

for num in range(2,101):
    primo = True 
    
    for i in range(2,num):
      if num % i == 0:
       primo = False
       
    if primo:
     print(num)
