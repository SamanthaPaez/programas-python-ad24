# p42-suma-200 - Calcular la suma de numeros ingresados por el usuario hasta que sea mayor o igual a 200

import os

while True:
    os.system("cls")
    print("Calcula la suma de numeros ingresados por el usuario hasta que sea mayor o igual a 200")

    suma_numeros = 0
    contador = 0

    while suma_numeros < 200:
        numero = float(input("\nIngresa un numero: "))
        suma_numeros += numero
        contador += 1

    print(f"\nLa suma total de los numeros es: {suma_numeros}")
    print(f"Cantidad de numeros ingresados: {contador}")

    if input("\n¿Deseas continuar (S/N)? ").upper().startswith("N"): break

print("\nProceso terminado")
