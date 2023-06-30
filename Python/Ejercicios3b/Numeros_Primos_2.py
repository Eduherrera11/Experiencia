'''NUMEROS PRIMOS 2: 
Dado una lista de números enteros, escribe un script en Python que devuelva una nueva lista con 
los números primos de la lista original. Además, el script debe devolver el número total de 
números primos encontrados y la suma de los números primos encontrados'''

print('Bienvenido al programa')

list = [1,2,3,4,5,6,7,8,9,10,11,47,11]
lista = []

for num in list:
    primo = True 
    
    for i in range(2,num):
      if num % i == 0:
       primo = False
       
    if primo:
     lista.append(num)
print(lista)