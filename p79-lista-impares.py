# p79-lista-impares
#   • Llenar una lista con los primeros n números impares (ej 1 3 5 7 9 11 n)
#   • Calcular e imprimir la suma y promedio de los números
#   • Mostrar los números que son divisibles entre 3 y sumarlos
#   • Pedir un elemento a buscar en la lista original y decir si esta y en que posición

import os
os.system("cls")

n = int(input("Ingresa el valor de n (numero de impares): "))

impares = []

for i in range(n):
    impares.append(2 * i + 1)

suma = sum(impares)
promedio = suma / len(impares)

print("\nNumeros impares:", impares)
print("Suma:", suma)
print("Promedio:", promedio)

divisibles_por_3 = [num for num in impares if num % 3 == 0]
suma_divisibles = sum(divisibles_por_3)

print("Numeros impares divisibles entre 3:", divisibles_por_3)
print("Suma de numeros divisibles entre 3:", suma_divisibles)

buscar = int(input("Ingresa un numero a buscar en la lista de impares: "))

if buscar in impares:
    posicion = impares.index(buscar)
    print(f"El numero {buscar} esta en la lista en la posicion {posicion}")
else:
    print(f"El numero {buscar} no esta en la lista")
