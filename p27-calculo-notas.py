# p27-calculo-notas - Calcula el promedio de 5 calificaciones e imprime el mensaje correspondiente


import os; os.system("cls")

print("Calcula el promedio de 5 calificaciones e imprime el mensaje correspondiente\n")

calificaciones = input("Ingresa 5 calificaciones separadas por espacio: ").split()
calificaciones = map(int, calificaciones)

promedio = sum(calificaciones) / 5

if promedio > 0 and promedio < 6:
    mensaje = "Quedas reprobado"
elif promedio >= 6 and promedio < 7:
    mensaje = "Pasas de panzazo"
elif promedio >= 7 and promedio < 8:
    mensaje = "Muy bien, puedes mejorar"
elif promedio >= 8 and promedio < 9:
    mensaje = "Excelente, sigue así"
elif promedio >= 9 and promedio <= 10:
    mensaje = "Perfecto, tu esfuerzo valió la pena"
else:
    mensaje = "Calificación fuera de rango"

print(f"Tienes un promedio de: {promedio:.2f}. {mensaje}")

print("\nProceso terminado")
