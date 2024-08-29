# p18-paga-trabajdor-v2 - Calcula la paga de un trabajador considerando las horas extra

import os
os.system("cls")

print("Calcula la paga de un trabajador considerando las horas extra\n")

nombre = input("Ingresa tu nombre: ")
horas = int(input("Horas trabajadas: "))
paga = float(input("Paga x hora: "))

tasa = 0.03
hextra = paganormal = pagaextra = pagabruta = 0

if horas > 40:
    hextra = horas - 40
    paganormal = 40 * paga
    pagaextra = hextra * paga * 2 
    pagabruta = paganormal + pagaextra
else:
    pagabruta = horas * paga

impuesto = pagabruta * tasa
paganeta = pagabruta - impuesto


print (f"\nEl trabajador {nombre}, trabaja {horas} horas, a una paga de {paga:.2f}")
print(f"\nHoras Extra   : {hextra}, Paga normal: {paganormal}, Paga extra: {pagaextra}")
print(f"\nPaga Bruta    : {pagabruta:.2f}")
print(f"\nImpuesto      : {impuesto:.2f}")
print(f"\nPaga Neta     : {paganeta:.2f}")
