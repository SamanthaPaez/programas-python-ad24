# p133-estadisticas-basicas

import os
import math

def leer_arreglo():
    numeros = input("Ingresa numeros: ")
    lista = list(map(int, numeros.split()))
    return lista

def mayor(lista):
    return max(lista)

def menor(lista):
    return min(lista)

def media(lista):
    return sum(lista) / len(lista)

def varianza(lista):
    mu = media(lista)
    return sum((x - mu) ** 2 for x in lista) / len(lista)

def desviacion_estandar(lista):
    return math.sqrt(varianza(lista))

# Programa princial
os.system("Cls")
lista_numeros = leer_arreglo()
print(f"Lista de numeros: {lista_numeros}")
print(f"La media: {media(lista_numeros):.3f}")
print(f"Mayor de los datos: {mayor(lista_numeros)}")
print(f"Menor de los datos: {menor(lista_numeros)}")
print(f"Varianza: {varianza(lista_numeros):.3f}")
print(f"Desviacion estandar: {desviacion_estandar(lista_numeros):.3f}")