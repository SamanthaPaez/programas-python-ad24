# p47-numeros-100-1-v2 - Imprime numeros de n a 1 en decrementos de 1 usando for

import os; os.system("cls")

""" print("Imprime numeros de 1 a 100 usando for\n")
print(list(range(1,10)))
print(list(range(1,10,2)))
print(list(range(1,10,3)))
print(list(range(10, 0, -1))) """

n = int(input("¿Desde donde deseas descender? "))

for x in range(n,0,-1):
    print(x, end=" ")