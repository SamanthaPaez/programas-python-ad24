# p47-numeros-100-1 - Imprime numeros de 100 a 1 en decrementos de 1 usando for

import os; os.system("cls")

""" print("Imprime numeros de 1 a 100 usando for\n")
print(list(range(1,10)))
print(list(range(1,10,2)))
print(list(range(1,10,3)))
print(list(range(10, 0, -1))) """

for x in range(100,0,-1):
    print(x, end=" ")