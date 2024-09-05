# p23-numeros-consecutivos - Dados tres numeros enteros, verifica si son consecutivos

import os; os.system("cls")

print("Dados tres numeros enteros, verifica si son consecutivos\n")

n1, n2, n3 = map(int, input("Ingresa tres numeros separados por espacio: ").split())
n1, n2, n3 = sorted([n1, n2, n3])

if n2 == n1 + 1 and n3 == n2 + 1:
    print(f"Los números {n1}, {n2} y {n3} son consecutivos")
else:
    print(f"Error: Los números {n1}, {n2} y {n3} no son consecutivos")

print("\nProceso terminado")