import math
print(""
"selecciona la operación:\n"
"1.- Sumar\n"
"2.- Restar\n"
"3.- Multiplicar\n"
"4.- Dividir\n"
"5.- MCM\n"
"6.- MCD\n"
"7.- Potencia (Elevar un número)\n"
"8.- Raiz cuadrada\n")
ree = int(input())

if ree == 1:
    n1 = int(input("Dame el primero número: "))
    n2 = int(input("Dame el segundo número: "))
    suma = n1 + n2
    print("El resultado es: "+ str(suma))
elif ree == 2:
    n1 = int(input("Dame el primero número: "))
    n2 = int(input("Dame el segundo número: "))
    resta = n1 - n2
    print("El resultado es: "+ str(resta))
if ree == 3:
    n1 = int(input("Dame el primero número: "))
    n2 = int(input("Dame el segundo número: "))
    multi = n1*n2
    print("El resultado es: "+ str(multi))
if ree == 4:
    n1 = int(input("Dame el primero número: "))
    n2 = int(input("Dame el segundo número: "))
    div = n1 / n2
    print("El resultado es: "+ str(div))
if ree == 5:
    n1 = int(input("Dame el primero número: "))
    n2 = int(input("Dame el segundo número: "))
    mcm=math.lcm(n1, n2)
    print("El mínimo común múltiplo entre "+str(n1)+" y "+str(n2)+" es: "+str(mcm))
if ree == 6:
    n1 = int(input("Dame el primero número: "))
    n2 = int(input("Dame el segundo número: "))
    mcd=math.gcd(n1, n2)
    print("El máximo común divisor entre "+str(n1)+" y "+str(n2)+" es: "+str(mcm))
if ree == 7:
    n1 = int(input("Dame el número base: "))
    n2 = int(input("Dame el exponente: "))
    poten = n1 ** n2
    def exponente(numero):
        indice = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")
        return str(numero).translate(indice)
    print("El resultado de: "+str(n1)+exponente(n2)+" es "+str(poten))
if ree == 8: 
    n = int(input("Dame el número del cuál quieras la raiz: "))
    raiz = math.sqrt(n)
    print("La raíz cuadrada de "+str(n)+" es: "+str(raiz))