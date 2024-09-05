# p30-numeros-100-1-v2 - #Imprime numeros de n a 1 usando while

import os; os.system("cls")

print("Imprime numeros de n a 1 usando while\n")

n = int(input("¿Desde donde?: "))
c = n

while c >= 1 :
    print(c, end=" ")
    c = c - 1

print("\nCiclo terminado")