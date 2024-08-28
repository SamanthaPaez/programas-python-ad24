# p10-tercer-angulo - Calcula el tercer ángulo dados dos ángulos de un triángulo

import os
os.system("cls")

print("Calcula el tercer angulo de un triangulo \n")

angulo1 = float(input("Dame la medida del primer angulo: "))
angulo2 = float(input("Dame la medida del segundo angulo: "))

angulo3 = 180 - (angulo1 + angulo2)

print("Medidas de los tres angulos de un triangulo ")
print(f"Primer angulo: {angulo1}")
print(f"Segundo angulo: {angulo2}")
print(f"Tercer angulo: {angulo3:.2f}")