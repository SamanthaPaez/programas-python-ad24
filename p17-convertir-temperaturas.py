# p17-convertir-temperaturas - Convierte temperaturas de Centigrados a Farenheit y viceversa

import os
os.system("cls")

print("Convierte temperaturas de Centigrados a Farenheit y viceversa\n")
print ("[1] Convertir Farenheit a Centigrados ")
print ("[2] Convertir Centigrados a Farenheit ")
print ("[3] Salir ")

op=int(input("Elige: "))

if op ==1:
    print("Convirtiendo de Farenheit a Centigrados")
    temp = float(input("Dame los grados Farenheit: "))
    res = (temp - 32) * 5/9
    print(f"{temp} Farenheit equivale a {res:.3f} Centigrados")
elif op==2:
    print("Convirtiendo de Centigrados a Farenheit")
    temp = float(input("Dame los grados Centigrados: "))
    res = (temp * 9/5) + 32
    print(f"{temp} Centigrados equivale a {res:.3f} Farenheit")
elif op==3:
    print("\nTe vas porque tu quieres... gracias")
else:
    print("Opcion erronea...")

print("\nProceso terminado...")