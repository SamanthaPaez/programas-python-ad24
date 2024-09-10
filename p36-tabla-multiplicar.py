# p36-tabla-multiplicar - Imprime la tabla de multiplicar que el ususario pida hasta donde la pida

import os

while(True):
    os.system("cls")
    print("\nImprime la tabla de multiplicar que el ususario pida hasta donde la pida")
    t = int(input("\n¿Qué tabla quieres? "))
    n= int(input("¿Hasta donde? "))

    c=1
    while c <= n:
        print(f"{t} x {c} = {t*c}")
        c+=1 

    if input("¿Deseas continuar? ").upper().startswith("N"): break

print("\nProceso terminado")