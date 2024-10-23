# p102-funcion-parametro - funcion con parametros
 
import os

def saluda(nombre):
    print(f"Hola {nombre} bienvenido a Python, tu nombre tiene {len(nombre)} caracteres")


# Programa principal
os.system("Cls")
saluda("Carlos Castaneda")
saluda("Juan Perez Diaz")
saluda("Maria Soto Garcia")
saluda(20)

