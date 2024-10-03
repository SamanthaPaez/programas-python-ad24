# p78-ciudades
# Leer n nombres de ciudades en una lista hasta introducir $
#    • Imprimir cuantos elementos son, y la lista completa
#    • Ordenar la lista en orden descendente y mostrar (sort)
#    • Imprimir cuantas ciudades inician con la letra consonante (startswith) y sus nombres

import os
os.system("cls")

ciudades = []

while True:
    ciudad = input("Ingresa el nombre de una ciudad (o '$' para terminar): ")
    if ciudad == '$':
        break
    ciudades.append(ciudad)

print(f"\nCantidad de ciudades: {len(ciudades)}")
print("Lista de ciudades:", ciudades)

ciudades = sorted(ciudades, key=str.lower, reverse=True)
print("Lista de ciudades en orden descendente:", ciudades)

consonantes = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
ciudades_consonante = []

for ciudad in ciudades:
    
    if any(ciudad.startswith(consonante) for consonante in consonantes):
        ciudades_consonante.append(ciudad)

print(f"Cantidad de ciudades que inician con consonante: {len(ciudades_consonante)}")
print("Ciudades que inician con consonante:", ciudades_consonante)
