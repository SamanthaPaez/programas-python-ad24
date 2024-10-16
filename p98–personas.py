# p98–personas
import os; os.system('cls')

A = {'Juan', 'Maria', 'Pedro', 'Jose', 'Rocio'}
B = {'Pedro', 'Juan', 'Pablo', 'Mateo', 'Esther'}

print("Conjunto A:", A)
print("Conjunto B:", B)

print("\nUnion de A y B:", A | B)

print("Interseccion de A y B:", A & B)

print("Diferencia de A - B:", A - B)

print("Diferencia simetrica de A y B:", A ^ B)

print("\nPablo y Mateo son subconjunto de B:", {'Pablo', 'Mateo'}.issubset(B))
print("A es superconjunto de Reynaldo y Angelica:", A.issuperset({'Reynaldo', 'Angelica'}))

print("\nPedro esta en A:", 'Pedro' in A)
print("Lilia no esta en B:", 'Lilia' not in B)
