'''MATRIZ:
Crea un script que dada una lista de listas M (numérica), identifique si se trata de una matriz y en
ese caso imprima dos listas correspondientes a:
1. La fila cuyos elementos suman el máximo
2. La columna cuyos elementos suman el máximo
Si no se trata de una matriz devolverá dos listas vacías.
Por ejemplo:
M1=[[2,5,3],[6,1,8],[7,5,4]] devolverá: L1 = [7,5,4] y L2 = [2,6,7]
M2 = [[4,2,3],[4,5],[6,8,2]] devolverá: L1 = [] y L2 = []
(Nota: Definimos matriz como una lista de listas donde todas las listas internas tienen el mismo
numero de objetos)'''

M = [[2,5,3],[6,1,8],[7,5,4]]
L1 = []
L2 = []
m1 = M[0]
m2 = M[1]
m3 = M[2]
if (len(m1) == len(m2)) and (len(m2) == len(m3)):
    if sum(m1) > sum(m2) and sum(m1) > sum(m3):
        L1 = m1
    elif sum(m2) > sum(m1) and sum(m2) > sum(m3):
        L1 = m2
    else: 
         L1 = m3
else:
     print("La lista no es una matrix")
print(L1) 

if (len(m1) == len(m2)) and (len(m2) == len(m3)):
    m1.remove(0,2)
print(m1)

    




    