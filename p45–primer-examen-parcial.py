# p45-primer-examen-parcial - Se desea llevar el control de la inscripción a un evento académico de la Universidad Patito. 
# Se especifica: Tipo de usuario, paquete y cantidad.

import os

total_ventas_por_dia = 0

while True:
    os.system("cls")
    print ("Universidad Patio SA de CV")
    print ("Sistema de Inscripción Congreso de Sistemas")

    print("\nTipo de Usuario:")
    print("[1] Alumno      $100")
    print("[2] Trabajador  $200")
    print("[3] Docente     $500")

    usuario = int(input("\nEscoge el tipo de usuario (1-3): "))
    while usuario < 1 or usuario > 3:
        print("Tipo de usuario no valido. Por favor intenta nuevamente")
        usuario = int(input("\nEscoge el tipo de usuario (1-3): "))

    if   usuario == 1:
        p_usuario = 100
        tipo_usuario = "Alumno"
    elif usuario == 2:
        p_usuario = 200
        tipo_usuario = "Trabajador"
    elif usuario == 3:
        p_usuario = 500
        tipo_usuario = "Docente"

    print("\nTipo de Paquete:")
    print("[1] Solo Conferencias      $600")
    print("[2] Con Eventos Sociales   $800")
    print("[3] Con Kit de Acceso      $900")

    paquete = int(input("\nEscoge el tipo de paquete (1-3): "))
    while paquete < 1 or paquete > 3:
            print("Tipo de paquete no valido. Por favor intenta nuevamente")
            paquete = int(input("\nEscoge el tipo de paquete (1-3): "))

    if paquete == 1:
        p_paquete = 600
        tipo_paquete = "Solo Conferencias"
    elif paquete == 2:
        p_paquete = 800
        tipo_paquete = "Con Eventos Sociales"
    elif paquete == 3:
        p_paquete = 900
        tipo_paquete = "Con Kit de Acceso"
    
    c_inscripciones = int(input("\nIngresa la cantidad de inscripciones: "))

    subtotal = (p_usuario + p_paquete) * c_inscripciones

    if subtotal > 5000:
        if usuario == 1:
            descuento = subtotal * 0.20
            porcentaje = 20.0
        elif usuario == 2:
            descuento = subtotal * 0.10
            porcentaje = 10.0
        elif usuario == 3:
            descuento = subtotal * 0.05
            porcentaje = 5.0
    else:
            descuento = 0
            porcentaje = 0.0

    total = subtotal - descuento

    print("\nTu pedido fue el siguiente:") 
    print(f"Tipo de usuario: {tipo_usuario}, Tipo de Paquete: {tipo_paquete}, Cantidad de Inscripciones: {c_inscripciones}")
    print(f"Subtotal: ${subtotal:.2f} con un descuento de ${descuento:.2f} ({porcentaje}%) y un total de ${total:.2f}")

    total_ventas_por_dia += total

    if input("\n¿Deseas continuar (S/N)? ").upper().startswith("N"): break

print(f"\nTotal de ventas del día: ${total_ventas_por_dia:.2f}")
print("\nProceso terminado") 


    
