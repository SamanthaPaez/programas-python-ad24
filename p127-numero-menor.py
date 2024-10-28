# p127–numero-menor

import os

def menor(n1, n2, n3):
    m = n1
    if n2 < m:
        m = n2
    if n3 < m:
        m = n3
    return m

# Programa principal
os.system("Cls")
n1 = int(input("Numero 1: "))
n2 = int(input("Numero 2: "))
n3 = int(input("Numero 3: "))

resultado = menor(n1, n2, n3)
print(f"El menor de los tres numeros es: {resultado}")
