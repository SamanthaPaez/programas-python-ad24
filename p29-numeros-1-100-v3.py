# p29-numeros-1-100-v3 - #Imprime numeros del 1 a n en incrementos de p usando while

import os; os.system("cls")

print("Imprime numeros del 1 a n, en incrementos de p usando while\n")

c = 1

n = int(input("¿Hasta donde deseas llegar?: "))
p = int(input("En incrementos de: "))

while c <= n :
    print(c, end=" ")
    c = c + p

print("\nCiclo terminado")