"""14.Crea un set y elimina uno de sus elementos.
15.Crea un set vacío.
16.Crea dos sets y encuentra su union, su intersección y su diferencia.
17.Crea un script que dados dos sets cree uno nuevo que contenga solo los elementos
comunes de ambos.
18.Crea un script que dado un set con números devuelva el numero máximo y mínimo.
19.Crea un script que dados dos sets cree uno nuevo solo con los elementos únicos de
cada uno de los sets.
20.Crea un set con colores y comprueba si cierto color se encuentra en el set.
21.Crea un script que dados dos sets cree un nuevo set con los elementos que están en
el primer set pero no en el segundo.
22.Crea un script que dado un set de enteros devuelva el producto de todos los números
dentro del set."""

#1 Crea un set y elimina uno de sus elementos.
mi_set = {10, 2, 8}
mi_set.discard(2)
print(mi_set)
print('--------------------')

#2 Crea un set vacío.
mi_set = set()
print(type(mi_set))
print('-------------------------')

#3 Crea dos sets y encuentra su union, su intersección y su diferencia.
mi_set = {1, 2, 3}
mi_set2 = {3, 4, 5}
print(mi_set | mi_set2)
print(mi_set.union(mi_set2))
print(mi_set.intersection(mi_set2))
print(mi_set2.difference(mi_set))
print(mi_set.difference(mi_set2))
print('-----------------------')

#4 Crea un script que dados dos sets cree uno nuevo que contenga solo los elementos comunes de ambos.
mi_set = {1, 2, 3}
mi_set2 = {1, 2, 4}

mi_set3 = mi_set.intersection(mi_set2)
mi_set4 = mi_set & mi_set2
print(mi_set3)
print(mi_set4)
print('--------------------------')

#5 Crea un script que dado un set con números devuelva el numero máximo y mínimo.
mi_set = {1, 2, 3, 4, 5}
mi_set2 = {max(mi_set)}
mi_set3 = {min(mi_set)}
print(mi_set2)
print(mi_set3)
print('------------------------')

#6 Crea un script que dados dos sets cree uno nuevo solo con los elementos únicos de cada uno de los sets.
mi_set = {1, 2, 3, 4, 5}
mi_set2 = {4, 5, 6, 7, 8}
mi_set3 = mi_set.symmetric_difference(mi_set2)
print(mi_set)
print('---------------------')

#7 Crea un set con colores y comprueba si cierto color se encuentra en el set.
mi_set = {'azul', 'verde', 'rojo'}
print('rojo' in mi_set)
print('---------------------------')

#8 Crea un script que dados dos sets cree un nuevo set con los elementos que están en el primer set pero no en el segundo.

