# p58-combina - colores - Genera todas las combinaciones posibles entre los colores dados por el usuario

import os; os.system("cls")

colores = input("Ingresa colores separados por un espacio: ").split()
print(colores)

for color1 in colores:
    for color2 in colores:
        if color1 != color2:
            print(f"{color1.strip()} y {color2.strip()}")
    print()