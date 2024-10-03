# p77-listas-aleatorios-suma
# Generar 2 listas de 10 números aleatorios
# • Suma ambas listas en una tercera, suma solo los elementos de cada lista si ambos son impares
# • Imprime las 3 listas

import os
import random

os.system("cls")

lista1 = []
lista2 = []
lista_suma = []

for _ in range(10):
    lista1.append(random.randint(1, 10))
    lista2.append(random.randint(1, 10))

for i in range(10):
    num1 = lista1[i]
    num2 = lista2[i]
    if num1 % 2 != 0 and num2 % 2 != 0:
        lista_suma.append(num1 + num2)
    else:
        lista_suma.append(0)  

print(f"Lista 1: {lista1}")
print(f"Lista 2: {lista2}")
print(f"Suma (solo impares): {lista_suma}")
