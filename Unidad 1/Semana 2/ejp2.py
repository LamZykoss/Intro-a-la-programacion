print("Bienvenido a la calculadora v 1.0")
v1 = int(input("Dame el primer número: ")) ##pregunta al usuario el primer valor (incluir int ya que es un valor número no string)
v2 = int(input("Ahora el segundo número: ")) ##pregunta segundo valor

suma = v1+v2
resta = v1-v2
div = v1/v2
multi = v1*v2

print("¡Estos son los resultados!\n\n")
print(f"{v1} + {v2} = {suma}")
print(f"{v1} - {v2} = {resta}")
print(f"{v1} : {v2} = {div}")
print(f"{v1} x {v2} = {multi}")