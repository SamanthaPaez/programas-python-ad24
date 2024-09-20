# p47-numeros-100-1-v3 - Imprime numeros de n a 1 en decrementos de i

import os; os.system("cls")

""" print("Imprime numeros de 1 a 100 usando for\n")
print(list(range(1,10)))
print(list(range(1,10,2)))
print(list(range(1,10,3)))
print(list(range(10, 0, -1))) """

n=int(input("¿Desde donde deseas descender? "))
i=int(input("Decrementos de: "))
for x in range(n, 0, -i):
    print(x, end=" ")