# p26-numeros-romanos - Dado un numero entero entre 1 y 10, muestra su equivalente en numero romano
 
import os; os.system("cls")

print("Dado un numero entero entre 1 y 10, muestra su equivalente en numero romano\n")

numero = int(input("Ingresa un numero entre 1 y 10: "))

if numero >= 1 and numero <= 10:
    if numero == 1:
        romano = "I"
    elif numero == 2:
        romano = "II"
    elif numero == 3:
        romano = "III"
    elif numero == 4:
        romano = "IV"
    elif numero == 5:
        romano = "V"
    elif numero == 6:
        romano = "VI"
    elif numero == 7:
        romano = "VII"
    elif numero == 8:
        romano = "VIII"
    elif numero == 9:
        romano = "IX"
    elif numero == 10:
        romano = "X"
    
    print(f"\nEl número {numero} corresponde a {romano} en numero romano")
else:
    print("\nNúmero inválido")

print("\nProceso terminado")
