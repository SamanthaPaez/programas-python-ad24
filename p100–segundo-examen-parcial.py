# p100–segundo-examen-parcial - procesar los datos de los empleados de una empresa de muebles

import os; os.system("clear")

empleados = []

print("Muebleria Muebles Dico")
print("Sistema de Procesamiento de Empleados")

while True:
    nombre = input("\nNombre del empleado (o * para terminar): ")
    if nombre == "*":
        break
    edad = int(input("Edad: "))
    sexo = input("Sexo (h/m): ")
    pasatiempos = input("Pasatiempos (separados por comas): ").split(',')
    sueldo = float(input("Sueldo: "))

    empleado = {
        'nombre': nombre,
        'edad': edad,
        'sexo': sexo,
        'pasatiempos': [p.strip() for p in pasatiempos],
        'sueldo': sueldo
    }
    empleados.append(empleado)

print("\nTabla de datos:")
print(f"{'Nombre':<10} {'Edad':<5} {'Sexo':<5} {'Sueldo':<10} {'Pasatiempos'}")
for empleado in empleados:
    pasatiempos = ', '.join(empleado['pasatiempos'])
    print(f"{empleado['nombre']:<10} {empleado['edad']:<5} {empleado['sexo']:<5} {empleado['sueldo']:<10.2f} {pasatiempos}")

total_empleados = len(empleados)
hombres = sum(1 for e in empleados if e['sexo'] == 'h')
mujeres = sum(1 for e in empleados if e['sexo'] == 'm')

pasatiempos_contador = {}
suma_edades = 0
suma_sueldos = 0
mayor_edad = menor_edad = empleados[0]['edad']
mayor_empleado = menor_empleado = empleados[0]['nombre']

for empleado in empleados:
    suma_edades += empleado['edad']
    suma_sueldos += empleado['sueldo']
    
    if empleado['edad'] > mayor_edad:
        mayor_edad = empleado['edad']
        mayor_empleado = empleado['nombre']
    if empleado['edad'] < menor_edad:
        menor_edad = empleado['edad']
        menor_empleado = empleado['nombre']
    
    for pasatiempo in empleado['pasatiempos']:
        if pasatiempo in pasatiempos_contador:
            pasatiempos_contador[pasatiempo] += 1
        else:
            pasatiempos_contador[pasatiempo] = 1

promedio_edad = suma_edades / total_empleados
promedio_sueldo = suma_sueldos / total_empleados

print("\nResumen:")
print(f"Empleados: {total_empleados}")
print(f"Mujeres: {mujeres}")
print(f"Hombres: {hombres}")

print("Pasatiempos:", ', '.join([f"{p}/{c}" for p, c in pasatiempos_contador.items()]))
print(f"Edad -> suma: {suma_edades}, Promedio: {promedio_edad:.1f}")
print(f"Sueldo -> suma: {suma_sueldos:.2f}, Promedio: {promedio_sueldo:.2f}")
print(f"{mayor_empleado} de {mayor_edad} es el mayor, {menor_empleado} de {menor_edad} es el menor")
