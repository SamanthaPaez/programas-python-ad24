# p130-suma-pares-impares

import os

def suma_pares_impares(inicio, fin, tipo):
    suma = 0
    for num in range(inicio, fin + 1):
        if tipo.upper() == 'P' and num % 2 == 0: 
            suma += num
        elif tipo.upper() == 'I' and num % 2 != 0: 
            suma += num
    return suma

# Programa principal
os.system("Cls")
inicio = int(input("Ingresa el inicio del rango: "))
fin = int(input("Ingresa el fin del rango: "))
tipo = input("Ingresa 'P' para pares o 'I' para impares: ")

if tipo.upper() not in ['P', 'I']:
    print("Error: Debes ingresar 'P' para pares o 'I' para impares")
else:
    resultado = suma_pares_impares(inicio, fin, tipo)
    print(f"La suma de los numeros {'pares' if tipo.upper() == 'P' else 'impares'} en el rango de {inicio} a {fin} es: {resultado}")
