# p43-conversion-temperaturas - Convertir grados Cº a Fº en un intervalo ingresado por el usuario

import os

while True:
    os.system("cls")
    print("Conversor de temperaturas de grados Centigrados a Fahrenheit")

    ti = float(input("\nIngresa la temperatura inicial en grados Centigrados: "))
    tf = float(input("Ingresa la temperatura final en grados Centigrados: "))

    while tf < ti:
        print("La temperatura final debe ser mayor o igual a la temperatura inicial")
        tf = float(input("Por favor, ingresa una temperatura final valida en grados Centigrados: "))

    print("\nCentigrados\tFahrenheit")
    print("-" * 30)

    t_actual = ti

    while t_actual <= tf:
        f = (t_actual * 9/5) + 32
        print(f"{t_actual:.2f}\t\t{f:.2f}")
        t_actual += 1

    if input("\n¿Deseas continuar (S/N)? ").upper().startswith("N"):
        break

print("\nProceso terminado")
