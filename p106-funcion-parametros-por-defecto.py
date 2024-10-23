# p106-funcion-parametros-por-defecto - funciones con valores con defecto para los parametros

import os

def saluda(nombre="Alumno X", edad=15):
    print(f"Hola {nombre}, tienes {edad} años de edad")

# Principal
os.system("Cls")

saluda("Carlos")
saluda()
saluda("Rocio", 35)