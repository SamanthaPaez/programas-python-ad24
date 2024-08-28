# p11-convertir-temperatura - Dada una temperatura en grados celsius, obtiene su equivalente en grados farenheit

import os
os.system("cls")

print("Convierte una temperatura de grados Celsius a grados Farenheit \n")

celsius = float(input("Ingresa los grados Celsius que deseas convertir: "))

farenheit = (celsius * (9/5)) + 32

print(f"{celsius} grados Celsius equivalen a {farenheit:.2f} grados Farenheit")