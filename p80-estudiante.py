# p80-estudiante - Datos de un estudiante usando diccionario

import os
os.system("cls")

estudiante = {'nombre' : 'Juan Perez',
              'edad' : 45,
              'correo' : 'jperez@msn.com',
              'carrera' : 'Sistemas',}


print("El estudiante: ", estudiante, len(estudiante))

estudiante['calificacion'] = 9.5
estudiante['correo'] = 'juanp@gmail.com'
print("El estudiante: ", estudiante, len(estudiante))

print('Llaves ', estudiante.keys())
for k in estudiante.keys():
    print(k, end=" ")

print("\n\nValores ",estudiante.values())
for v in estudiante.values():
    print(v, end=" - ")

print("\n\nLlaves y valores al mismo tiempo")
for k, v in estudiante.items():
    print(f"{k:<15} : {v}")

print("\n\nLlaves y valores al mismo tiempo - forma 2")
for k in estudiante.keys():
    print(f"{k:<15} : {estudiante[k]}")