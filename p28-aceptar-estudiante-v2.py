# p28-aceptar-estudiante-v2 - La Universidad Kitty Kat SA es solo para mujeres mayores de 21 años con un promedio de entre 8 y 9.5.

import os; os.system("cls")

print("Evaluacion de aceptacion en la Universidad Kitty Kat SA\n")
print("Condiciones:")
print("Solo mujeres")
print("Solo mayores de 21 años")
print("Solo con promedio entre 8 y 9.5\n")

nombre = input("Dame el nombre: ")
edad = int(input("Dame la edad: "))
sexo = input("Dame el sexo [H / M]: ").upper()

print("Ingresa 3 calificaciones:")
c1 = int(input("Calificacion 1: "))
c2 = int(input("Calificacion 2: "))
c3 = int(input("Calificacion 3: "))

promedio = (c1 + c2 + c3) / 3

if sexo == "M":
    if edad >= 21:
        if 8 <= promedio < 9.5:
            print(f"\n{nombre}, has sido aceptada, tu edad de {edad} y tus calificaciones {c1}, {c2}, {c3} (promedio {promedio:.2f}) lo permiten")
        elif promedio == 10:
            print(f"\n{nombre}, has sido aceptada con un promedio perfecto de {promedio:.2f}. Excelente trabajo, tus calificaciones {c1}, {c2}, {c3} superan nuestro rango requerido")
        else:
            print(f"\n{nombre}, eres mujer, tienes la edad, pero tu promedio de {promedio:.2f} no esta en el rango requerido (8 a 9.5)")
    else:
        print(f"\n{nombre}, eres mujer, pero no tienes la edad adecuada, solo mayores a 21 (tu edad es {edad})")
else:
    print(f"\n{nombre}, solo aceptamos mujeres. Tu sexo es {sexo}")

print("\nProceso terminado")

