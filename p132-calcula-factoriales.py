# p132-calcula-factoriales

import os

def leer_arreglo():
    numeros = input("Ingresa los numeros: ")
    lista_numeros = [int(num) for num in numeros.split()]
    return lista_numeros

def factorial(n):
    f = 1
    for i in range(1, n + 1):
        f = f * i
    return f

def calcular_factoriales(lista):
    lista_factoriales = []
    for num in lista:
        lista_factoriales.append(factorial(num))  
    return lista_factoriales

# Programa principal
os.system("Cls")
numeros = leer_arreglo()
factoriales_resultado = calcular_factoriales(numeros)

print(f"La lista de numeros original: {numeros}")
print(f"La lista con los factoriales de los numeros: {factoriales_resultado}")
