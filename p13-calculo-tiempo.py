# p13-calculo-tiempo - Dada una cantidad en horas, calcula su equivalente en días, minutos y segundos

import os
os.system("cls")

print("Dada una cantidad en horas, calcula su equivalente en días, minutos y segundos\n")
horas = float(input("Introduce la cantidad de horas: "))

dias = horas / 24
minutos = horas * 60
segundos = horas * 3600

print(f"{horas} horas son equivalentes a:")
print(f"{dias:.2f} días")
print(f"{horas} horas")
print(f"{minutos:.2f} minutos")
print(f"{segundos:.2f} segundos")

