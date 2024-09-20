# p46-numeros-1-100-v3 - Imprime numeros de 1 a n en incrementos de i usando for

import os; os.system("cls")

""" print("Imprime numeros de 1 a 100 usando for\n")
print(list(range(1,10)))
print(list(range(1,10,2)))
print(list(range(1,10,3)))
print(list(range(10, 0, -1))) """

n = int(input("¿Hasta donde? " ))

i = int(input("Incrementos de: " ))
for x in range(1, n+1, i):
    print(x, end=" ")