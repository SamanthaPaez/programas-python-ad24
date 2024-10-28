# p128-dia-semana

import os

def dia_semana(n):
    if n == 1:
        return "Lunes"
    elif n == 2:
        return "Martes"
    elif n == 3:
        return "Miercoles"
    elif n == 4:
        return "Jueves"
    elif n == 5:
        return "Viernes"
    elif n == 6:
        return "Sabado"
    elif n == 7:
        return "Domingo"
    else:
        return "Numero invalido. Ingresa un numero entre 1 y 7"

# Programa principal
os.system("Cls")
n = int(input("Ingresa un numero entre 1 y 7: "))
print(f"El dia de la semana es: {dia_semana(n)}")
