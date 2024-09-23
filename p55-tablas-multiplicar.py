# p55-tablas-multiplicar - Imprime las tablas del 1 a tabla n, desde 1 hasta m

import os;

while True:
    os.system("cls")

    n = int(input("¿Hasta que tabla quieres?: ")) 
    m = int(input("¿Hasta donde deseas la tabla?: "))

    for i in range (1, n+1):
        print("Tabla del " + str(i) )
        for j in range (1, m+1):
            print(f"{i} x {j} = {i*j}")
        print()


    if input("\n¿Continuar (s/n)?: ").lower().startswith('n'): break

print("\nProceso terminado")