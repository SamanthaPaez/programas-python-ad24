# p103-funcion-parametros - funcion que recibe dos parametros

import os

def saluda (apaterno, nombre):
    print(f"Hola {apaterno} {nombre} longitud {len(apaterno+nombre)}")

# Principal
os.system("Cls")
saluda("Castaneda", "Carlos")
#saluda("Soto")
