# p40-pares-descendente - Imprimir los numeros pares desde 100 hasta n y su suma

import os

while True:
    os.system("cls")
    print("Imprime los numeros pares desde 100 hasta n y su suma total")

    n = int(input("\nIngresa el valor de n (debe ser mayor que 100): "))
   
    while n <= 100:
        print("El numero debe ser mayor que 100")
        n = int(input("Por favor, ingresa un valor mayor que 100: "))

    suma = 0
    i = 100

    while i <= n:
        if i % 2 == 0:
            print(i, end=" ")
            suma += i
        i += 1

    print(f"\nLa suma de los numeros pares de 100 a {n} es: {suma}")

    if input("\n¿Deseas continuar (S/N)? ").upper().startswith("N"):
        break

print("\nProceso terminado")
