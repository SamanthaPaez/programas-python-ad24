# p54 - tabla-multiplicar - Imprime la tabla de multiplicar usando un ciclo for

import os; 

while True:
    os.system("cls")

    t = int(input("Dame la tabla que deseas imprimir: "))
    n = int(input("¿Hasta donde deseas la tabla?: "))

    for i in range(1, n+1):
        print(f"{t} x {i} = {t*i}")

    if input("\n¿Continuar (s/n)?: ").lower().startswith('n'): break

print("\nProceso terminado")