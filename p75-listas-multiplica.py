# p75-listas-multiplica
# Leer dos listas con 5 elementos
#   • Multiplica las listas y guárdalos en una tercera lista
#   • Imprime las tres listas

import os
os.system("cls")

lista1 = []
lista2 = []
lista3 = []

print("Ingresa 5 numeros para la primera lista:")
for i in range(5):
    num = float(input(f"Elemento {i+1}: "))
    lista1.append(num)

print("\nIngresa 5 numeros para la segunda lista:")
for i in range(5):
    num = float(input(f"Elemento {i+1}: "))
    lista2.append(num)

for i in range(5):
    lista3.append(lista1[i] * lista2[i])

print(f"\nLista 1: {lista1}")
print(f"Lista 2: {lista2}")
print(f"Lista 3 (multiplicación): {lista3}")
