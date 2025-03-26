import os
saldo = 0.0
opcion = ""
def depositar():
    global saldo
    print("---Deposito de Dinero---")
    print("Su monto actual en su cuenta es: "+str(saldo))
    vmonto = int(input("¿Cuánto desea depositar? "))
    saldo = vmonto+saldo
    print(f"Saldo actualizado: {saldo}")
    input("Transacción realizada con éxito. Pulse ENTER")
while opcion != "S":
    os.system("cls")
    print("----------")
    print("BANCU DU ESTADO BRASIUL")
    print("----------")
    print("C --> Consultar saldo")
    print("D --> Depositar dinero")
    print("R --> Retirar dinero")
    print("S --> Salir")
    print("----------")
    opcion = input("¿Qué desea realizar? ").upper()
    if opcion == "D":
        depositar()
    elif opcion == "R":
        print("---Retiro de Dinero---")
        vmonto = float(input("¿Cuánto desea retirar? "))
        if vmonto > saldo:
            print(f"El monto del retiro es superior al de su saldo. ({saldo})")
            depos = input("¿Desea depositar? (S/N)").upper()
            if depos == "S":
                depositar()
            else:
                break
    elif opcion == "C":
        print("---Consulta de Saldo---")
        print("Su monto actual en su cuenta es: "+str(saldo))
        input("Operación realizada con éxito. ENTER para volver")
    elif opcion == "S":
        print("Muchas gracias por preferir cajeros tulons")
    else:
        print("Opción incorrecta. Pulse ENTER")

