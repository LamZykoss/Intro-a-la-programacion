print("Bienvenido al promediador de notas pro\n")

n1 = float(input("Dime la primera nota: "))
n2 = float(input("Dime la segunda nota: "))
n3 = float(input("Dime la tercera y ultima nota: "))

promedio = (n1 + n2 + n3) / 3

if promedio>=4.0 and promedio<=5.9:
    print("Has aprobado, sigue así, tu promedio es: ",round(promedio, 2))
elif promedio>=6.0 and promedio<=7.0:
    print("Felicidades obtuviste un promedio sobresaliente, tu promedio es: ",round(promedio, 2))
else:
    print("Lo siento... No has aprobado a repetir el ramo xD, tu promedio es: ",round(promedio, 2))