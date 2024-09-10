# p39-impares-ascendente - Imprimir los números impares desde 1 hasta n y su suma

import os

while True:
    os.system("cls")
    print("Imprime los numeros impares desde 1 hasta n y su suma total")

    n = int(input("\nIngresa el valor de n: "))
    suma = 0
    i = 1

    while i <= n:
        if i % 2 != 0:
            print(i, end=" ")
            suma += i
        i += 1

    print(f"\nLa suma de los numeros impares de 1 a {n} es: {suma}")

    if input("\n¿Deseas continuar (S/N)? ").upper().startswith("N"):
        break

print("\nProceso terminado")
