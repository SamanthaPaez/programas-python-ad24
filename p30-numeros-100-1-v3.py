# p30-numeros-100-1-v3 - #Imprime numeros de n a 1 en decrementos de p usando while

import os; os.system("cls")

print("Imprime numeros de n a 1, en decrementos de p usando while\n")

n = int(input("¿Desde donde?: "))
p = int(input("En decrementos de: "))
c = n

while c >= 1 :
    print(c, end=" ")
    c = c - p

print("\nCiclo terminado")