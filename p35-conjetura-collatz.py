# p35-conjetura-collatz - Calcula e imprime los numeros de la conjetura Collatz

import os

while(True):

    os.system("cls")
    print("\nCalcula e imprime los numeros de la conjetura Collatz")
    num=int(input("\nDame un entero positivo: "))

    while num!=1 :
        print(num, end=" ")
        if num % 2 == 0 :
            num = num // 2
        else:
            num = num * 3 + 1
    print(num, end=" ")

    if input("\n\n¿Deseas continuar (S/N)? ").upper().startswith("N"):break

print ("\nProceso terminado")