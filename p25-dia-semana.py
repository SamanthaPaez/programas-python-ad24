# p25-dia-semana - Dado un numero entero entre 1 y 7, muestra el dia de la semana correspondiente

import os; os.system("cls")

print("Dado un numero entero entre 1 y 7, muestra el dia de la semana correspondiente\n")

numero = int(input("Ingresa un numero entre 1 y 7: "))

if numero >= 1 and numero <= 7:
    if numero == 1:
        dia = "Domingo"
    elif numero == 2:
        dia = "Lunes"
    elif numero == 3:
        dia = "Martes"
    elif numero == 4:
        dia = "Miercoles"
    elif numero == 5:
        dia = "Jueves"
    elif numero == 6:
        dia = "Viernes"
    elif numero == 7:
        dia = "Sabado"
    
    print(f"El número {numero} corresponde al dia: {dia}")
else:
    print("Dia invalido")

print("\nProceso terminado")
