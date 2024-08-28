# p09-hipotenusa-triangulo - Calcula la hipotenusa de un triángulo rectángulo dadas las longitudes de sus lados

import os
import math as mt

os.system("cls")

print("Calcula la hipotenusa de un triangulo rectangulo dadas las longitudes de sus lados \n")
longlado1 = float(input("Dame la longitud del primer lado: "))
longlado2 = float(input("Dame la longitud del segundo lado: "))

hipotenusa =  mt.sqrt(longlado1 * longlado1 + longlado2 * longlado2)

print ("Longitudes de los lados de un triangulo rectangulo")

print(f"Primer lado: {longlado1}")
print(f"Segundo lado: {longlado2}")
print(f"Hipotenusa: {hipotenusa:.3f}")

