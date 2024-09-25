# p60-suma-pares-2-n - Imprimir los pares de 2 a n y su suma

import os; os.system("cls")
print("Imprime los numeros pares de 2 a n y su suma ")

n = int(input("\nDame numero: "))

suma = 0

for i in range(2, n+1, 2):
    print(i, end=" ")
    suma += i

print(f", La suma es = {suma}")
