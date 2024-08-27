# p07-funciones-trigonometricas - Calcula las funciones trigonometricas sobre un angulo

print ("Calcula las funciones trigonometricas sobre un angulo")

import math as mt

angulod = float(input("Dame un angulo: "))
angulor = mt.radians(angulod)

print(f"Angulo original: {angulod}, Angulo en radianes: {angulor}")

salida = ("Resumen de funciones trigonometricas \n"
f"Seno     : {mt.sin(angulor):.3f} \n"
f"Coseno   : {mt.cos(angulor):.3f} \n"
f"Tangente : {mt.tan(angulor):.3f} \n" )

print(salida)