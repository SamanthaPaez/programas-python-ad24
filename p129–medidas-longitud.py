# p129–medidas-longitud

import os

def pulgadas_a_centimetros(pulgadas):
    return pulgadas * 2.54

def metros_a_pies(metros):
    return metros * 3.281

# Programa principal
os.system("Cls")

print("[ 1 ] Convertir pulgadas a centimetros")
print("[ 2 ] Convertir metros a pies")

opcion = int(input("Elige una opcion: "))

if opcion == 1:
    pulgadas = float(input("Ingresa la medida en pulgadas: "))
    print(f"{pulgadas} pulgadas son {pulgadas_a_centimetros(pulgadas)} centimetros")
elif opcion == 2:
    metros = float(input("Ingresa la medida en metros: "))
    print(f"{metros} metros son {metros_a_pies(metros)} pies")
else:
    print("Opcion invalida. Elige 1 o 2")
