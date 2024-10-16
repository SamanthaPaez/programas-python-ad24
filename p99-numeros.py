# p99–numeros

import os; os.system('cls')

A = {50, 60, 70, 80, 90, 100, 200}
B = {60, 90, 100, 300, 400, 500}
C = {10, 20, 60, 90, 70, 100, 600, 700}

print("Conjunto A:", A)
print("Conjunto B:", B)
print("Conjunto C:", C)

print("\nUnion de A y B:", A | B)
print("Union de B y C:", B | C)
print("Diferencia de A - C:", A - C)
print("Diferencia simetrica de B y C:", B ^ C)
print("Interseccion de B y C:", B & C)

print("\n¿A es subconjunto de B?:", A.issubset(B))
print("¿C es subconjunto de A?:", C.issubset(A))
print("¿100 esta en A?:", 100 in A)
print("¿60 esta en A, B y C?:", 60 in A and 60 in B and 60 in C)
print("¿900 no esta en C?:", 900 not in C)
