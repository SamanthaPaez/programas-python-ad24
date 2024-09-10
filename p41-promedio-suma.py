# p41-promedio-suma - Calcular la suma y el promedio de una serie de numeros ingresados por el usuario. 0 para terminar

import os

while True:
    os.system("cls")
    print("Calcula la suma y el promedio de una serie de numeros ingresados por el usuario. Para terminar, ingresa 0")

    suma_numeros = 0
    contador = 0

    while True:
        numero = float(input("\nIngresa un numero (0 para terminar): "))
        if numero == 0:
            break
        suma_numeros += numero
        contador += 1

    if contador == 0:
        print("No se ingresaron numeros.")
    else:
        promedio = suma_numeros / contador
        print(f"\nSuma de los numeros: {suma_numeros}")
        print(f"Promedio de los numeros: {promedio:.2f}")
        print(f"Cantidad de numeros ingresados: {contador}")

    if input("\n¿Deseas continuar (S/N)? ").upper().startswith("N"): break

print("\nProceso terminado")
