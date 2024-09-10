# p34-tabla-conversion - Imprimir una tabla de conversion de peso a dolar

import os

while(True):
    os.system("cls")

    print("Imprime una tabla de conversion de peso a dolar\n")

    tc = 19.87

    while(True): # Pide valores hasta que pi < pf
        pi = float(input("Valor en pesos inicial: "))
        pf = float(input("Valor en pesos final: "))
        if pi<pf:
            break

    c = pi

    print("\nPeso\tDollar")
    print("-"*15)
    while c <= pf :
        print(f"{c}\t{c/tc:.2f}")
        c+=1
    print("-"*15)

    if input("¿Deseas continuar (S/N)? ").upper().startswith("N") : break
print("\nProceso terminado")