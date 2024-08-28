# p14-numero-suerte - Dado el año de nacimiento, la suma de sus digitos individuales es el numero de la suerte

import os
os.system("cls")

print("Obten el numero de la suerte segun tu año de nacimiento\n")

año_nacimiento = int(input("Introduce tu año de nacimiento (4 dígitos): "))

primer_digito = año_nacimiento // 1000
segundo_digito = (año_nacimiento % 1000) // 100
tercer_digito = (año_nacimiento % 100) // 10
cuarto_digito = año_nacimiento % 10

print("Tu año de nacimiento es:", año_nacimiento)
print("Primer digito:  ", primer_digito)
print("Segundo digito: ", segundo_digito)
print("Tercer digito:  ", tercer_digito)
print("Cuarto digito:  ", cuarto_digito)

numero_suerte = primer_digito + segundo_digito + tercer_digito + cuarto_digito
print("\nTu numero de la suerte es: ", numero_suerte)
