# p24-numero-mayor - Dados tres números enteros, verificar cual es el mayor

import os; os.system("cls")

print("Dados tres números enteros, verifica cuál es el mayor\n")


n1, n2, n3 = map(int, input("Ingresa tres números separados por espacio: ").split())


if (n1 >= n2) and (n1 >= n3):
    mayor = n1
elif (n2 >= n1) and (n2 >= n3):
    mayor = n2
else:
    mayor = n3

print(f"El mayor de los números {n1}, {n2} y {n3} es {mayor}")

print("\nProceso terminado")
