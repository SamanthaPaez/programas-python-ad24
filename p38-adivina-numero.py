#  p38-adivina-numero - El usuario adivina un numero entero entre 1-100

import os, random

while True:
    os.system("cls")
    numero_secreto=random.randint(1,100)
    intentos=0
    
    while True:
        numero_ingresado=int(input("\nAdivina el numero secreto (1-100): "))
        intentos +=1
        if numero_ingresado==numero_secreto:
            print(f"\nFelicidades, adivinaste en {intentos} intentos")
        elif numero_ingresado<numero_secreto:
            print("El numero secreto es mayor")
        else:
            print("El numero secreto es menor")

        if input("\n¿Deseas continuar (S/N)? ").upper().startswith("N"): break

    print("\n\nProceso terminado")