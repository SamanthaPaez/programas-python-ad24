# p63-secuencia-terminos-1 - Imprimir la secuencia de terminos armonicos y su suma

import os
os.system("cls")
print("Imprime la secuencia de terminos armonicos y su suma")
num_terminos = int(input("\n¿Cuantos terminos?: "))

suma = 0

salida = ""

for i in range(1, num_terminos + 1):
    factorial = 1
    for j in range(1, i + 1):
        factorial *= j
    termino = 1 / factorial
    if i == 1:
        salida += "1" 
    else:
        salida += f" + 1/{i}!"
    suma += termino

print(f"Salida: {salida}, suma: {suma}")
