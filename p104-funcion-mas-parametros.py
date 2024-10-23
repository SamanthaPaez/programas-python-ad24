# p104-funcion-mas-parametros - numeros de parametros desconocido

import os

def saludatodos(*todos):
    print(todos)
    print("Hola", todos[0])
    print(f"Separados por - {"-".join(todos)}")
    for n in todos:
        print("Hola : ", n.upper())

# Principal
os.system("Cls")
saludatodos("Juan", "Pedro", "Luis", "Rocio", "Maria")
saludatodos("Luis", "Jose")
saludatodos("Carlos")