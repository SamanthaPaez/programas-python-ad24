# p20-ley-de-newton - Calcular la segunda ley de Newton (F = M * A)

import os; os.system("cls")
print("Calcular la segunda ley de Newton\n ") 
print("[ F ] Fuerza          F = M * A")
print("[ M ] Masa            M = F / A")
print("[ A ] Aceleracion     A = F * M")
op = input("Elige: ").upper()

if op=="F":
    print("\nCalculando la Fuerza...")
    m=float(input("Dame la Masa: "))
    a=float(input("Dame la Aceleracion: "))
    f=m*a
    print(f"La Fuerza es: {f}")
elif op=="M":
    print("\nCalculando la Masa...")
    f=float(input("Dame la Fuerza: "))
    a=float(input("Dame la Aceleracion: "))
    m=f/a
    print(f"La Masa es: {m}")
elif op=="A":
    print("\nCalculando la Aceleracion")
    f=float(input("Dame la Fuerza: "))
    m=float(input("Dame la Masa: "))
    a=f/m
    print(f"La Aceleracion es: {a}")
else:
    print("\nOpcion invalida...")

print("\nProceso terminado")