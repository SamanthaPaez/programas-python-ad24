# p37-tabla-multiplicar-v2 - Imprime las tablas de multiplicar de 1 a n hasta donde el usuario quiera

import os

while(True):
    os.system("cls")
    print("\nImprime tablas de 1 a n")
    n=int(input("Tabla de 1 a n: "))
    m=int(input("¿Hasta donde?: "))
    
    t=1
    while t <= n:
        print(f"\nTabla del {t}")
       
        c = 1
        while c <= m:
            print(f"{t} x {c} = {t*c}")
            c+=1
        t += 1

    if input("¿Deseas continuar (S/N)? ").upper().startswith("N"): break

print("\nProceso terminado")