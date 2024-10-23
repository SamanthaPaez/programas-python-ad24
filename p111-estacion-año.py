# p111-estacion-año - funcion que regresa una cadena con la estacion del año, recibe como parametro un numero entre 1 y 4

import os

def estacion(n):
    if n==1:
        return "Primavera"
    elif n==2:
        return"Verano"
    elif n==3:
        return "Otoño"
    elif n==4:
        return "Invierno"
    else:
        return "Error"
    
# Principal
os.system("Cls")
n = int(input("Dame estacion del año (1-4) y te la doy con letra: "))
print(f"La estacion es {estacion(n)}")