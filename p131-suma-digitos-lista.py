# p131-suma-digitos-lista

import os

def leerarreglo():
    numeros = input("Ingresa los numeros: ")
    lista_numeros = [int(num) for num in numeros.split()]
    return lista_numeros

def sumadigitos(n):
    suma = 0
    while n != 0:
        dig = n % 10
        suma += dig
        n = n // 10
    return suma

def suma_digitos_lista(lista):
    suma_lista = []
    for num in lista:
        suma_lista.append(sumadigitos(num))
    return suma_lista

# Programa principal
os.system("Cls")
numeros = leerarreglo()
suma_digitos_resultado = suma_digitos_lista(numeros) 

print(f"La lista de numeros original: {numeros}")
print(f"La lista con las sumas de digitos de los numeros: {suma_digitos_resultado}")
