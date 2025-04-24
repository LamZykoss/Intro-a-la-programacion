#tema 6 clase 24/04 ejercicio 1
import os 
os.system("cls")
print("Tienda de frutas providencia")
frutas=['naranja', 'uva', 'pera']

#función len (contar frutas)
vtotal_frutas=len(frutas)
print("El total de fruta en stock es de: ",vtotal_frutas)
input("Pulse [ENTER] para continuar")

print("Listado de las frutas en stock: ")
print("===============================")
#recorrido 
for i in frutas:
    print(i)

#agregar fruta
nueva_fruta=input("Ingrese nombre de la fruta: ").lower()
frutas.append(nueva_fruta)
print("Fruta añadida con éxito, a continuación la nueva lista: ")
print("========================================================")
vopc=0
for x in frutas:
    print('['+str(vopc+1)+']', x)
    vopc+=1

#borrar por nombre; metodo remove
borrar_fruta=input("Ingrese la fruta a borrar: ")
frutas.remove(borrar_fruta)
print("Fruta borrada con éxito, a continuación la nueva lista: ")
print("========================================================")
vopc=0
for x in frutas:
    print('['+str(vopc+1)+']', x)
    vopc+=1

input("Pulse enter para continuar")

#borrar por id; metodo pop
ID_fruta = int(input("Ingrese el ID de la fruta que desea borrar: "))
frutas.pop(ID_fruta-1)
print("Fruta borrada con éxito, pulse [ENTER] para continuar")

#buscar fruta
buscar_fruta=input("Ingrese la fruta a buscar: ")
v_existe = False
for x in frutas:
    if x==buscar_fruta:
        v_existe=True
        print(f"Fruta {x} encontrada!")
        input("Pulse [ENTER] para continuar")
if not v_existe:
    input("Fruta no encontrada o no existente")