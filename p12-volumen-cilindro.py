# p12-volumen-cilindro - Calcula el volumen de un cilindro dados su radio y altura

import math as mt
import os
os.system("cls")


print("Calcula el volumen de un cilindro dados su radio y altura \n")

altura = float(input("Ingresa la altura del cilindro: "))
radio = float(input("Ingresa el radio del cilindro: "))

volumen = mt.pi * (radio * radio) * altura

print(f"Altura: {altura}")
print(f"Radio: {radio}")
print(f"Volumen: {volumen:.2f}")

print(f"Un cilindro con una altura de {altura} y con un radio de {radio} tiene un volumen de {volumen:.2f} ")