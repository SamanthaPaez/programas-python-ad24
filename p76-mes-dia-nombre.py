# p76-mes-dia-nombre
#   Leer un número de mes (ej 4).
#   • Imprimir: días del mes, y nombre del mes (ej marzo, 30).
#   • Asume 28 para febrero, guarda días en una lista, y nombres de mes en otra.

import os
os.system("cls")

nombres_meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", 
                 "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
dias_meses = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

mes = int(input("Ingresa el numero de mes (1-12): "))

if 1 <= mes <= 12:
    nombre_mes = nombres_meses[mes-1]
    dias_mes = dias_meses[mes-1]
    
    print(f"{nombre_mes}, {dias_mes}")
else:
    print("Numero de mes invalido. Debe ser entre 1 y 12")
