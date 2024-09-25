# p61-secuencia-numeros-1 - Imprimir la secuencia de números mostrados el numero de renglones que el usuario desee:

import os
os.system("cls") 

print("Imprime la secuencia de numeros mostrados con el numero de renglones que el usuario desee")
n = int(input("\nDame numero: "))

for i in range(1, n + 1):
    print((str(i) + " ") * i) 
