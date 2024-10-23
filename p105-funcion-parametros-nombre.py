# p105-funcion-parametros-nombre - funciones con nombres en los parametros

import os

def saluda(apaterno, amaterno, nombre):
    print(f"Hola {apaterno} {amaterno}, {nombre} ")

# Principal
os.system("Cls")
saluda("Castaneda", "Ramirez", "Carlos")
saluda(nombre="Carlos", amaterno="Ramirez", apaterno="Castaneda")
saluda(amaterno="Bernal", nombre="Rocio", apaterno="Soto")