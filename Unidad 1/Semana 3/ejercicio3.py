import os
os.system("cls")

print("Bienvenido al VancoEstao du chile")

name = input("Dame tu nombre: ")
print(f"¡Hola {name} bienvenido, necesitamos saber algunas cosas antes de otorgar algun crédito!\n\n")
nacional = input("¿Cuál es su nacionalidad? ")
if nacional == "chilena":
    rut = int(input("Ingresa tu rut: "))
    edad = int(input("¿Cuántos años tiene? "))
    if edad < 18 or edad > 60:
        print("No cumples con la edad requerida para adquirir el crédito ")
    else:
        corriente = input("¿Que tipo de cuenta tiene? (RUT, Ahorro, Corriente) ")
        if corriente == "corriente":
            antiguo = int(input("¿Cuantos meses de antigüedad posee con la cuenta? "))
            if antiguo >= 6:
                dicom = input("¿Se encuentra registrado en DICOM? ")
                if dicom == "si":
                    tiempodicom = int(input("¿Haces cuantos meses ingresaste a DICOM?"))
                    if tiempodicom <= 12:
                        sueldo = int(input("¿Cuál es su sueldo? "))
                    else: 
                        print("Para liberarte de DICOM deben pasar 12 meses desde que fuiste ingresado")
                else:
                    sueldo = int(input("¿Cuál es su sueldo? "))

                    if sueldo >= 800000 and sueldo <= 999999:
                        print("¡Felicidades has obtenido un crédito de 10.000.000 ClP! Gracias por preferir VancoEstado (Se te otorgo un rango: Bronce)")
                        print(f"Datos finales:\nSu nombre es: {name}\nRUT: {rut}\nSueldo: ${sueldo} \nCrédito: si\nRango: Bronce")
                    elif sueldo >= 1000000 and sueldo <= 4000000:
                        print("¡Felicidades has obtenido un crédito de 20.000.000 ClP! Gracias por preferir VancoEstado (Se te otorgo un rango: Oro)")
                        print(f"Datos finales:\nSu nombre es: {name}\nRUT: {rut}\nSueldo: ${sueldo} \nCrédito: si\nRango: Oro")
                    elif sueldo > 4000000:
                        print("¡Felicidades has obtenido un crédito de 50.000.000 ClP! Gracias por preferir VancoEstado (Se te otorgo un rango: Platino)")
                        print(f"Datos finales:\nSu nombre es: {name}\nRUT: {rut}\nSueldo: ${sueldo} \nCrédito: si\nRango: Platino")
                    elif sueldo < 800000:
                        print("Lo siento pero no cumples con los requisitos para obtener un crédito")
            else:
                print("No cumples con el tiempo mínimo requerrido")
        else:
            print("El crédito solo está permitido para usuarios de cuentas CORRIENTE")
else:
    print("Lo siento pero no puedes adquirir nuestro crédito debido a tu nacionalidad")