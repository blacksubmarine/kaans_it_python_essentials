#programa que genere una clave aleatoria de 3 digitos y que el usuario la adivine
#si el intento del usuario le atina a un numero de la clave en posicion correcta que le diga, hubo un match
#si el intento del usuario le atina  a un numero pero en una posicion diferente que le diga, estas cerca
#si el usuario no le atina a ningun numero que le diga, no hay match 

import random 

clave = [str(num) for num in range(10)]

random.shuffle(clave)
clave = clave[:3]
print(clave)

x=""
clave = clave[0]+clave[1]+clave[2]
print(clave)
entrada = ""
while entrada != clave:
	
	pistas= []
	matches = []

	entrada = input("ingrese la clave de 3 digitos: ")
	if entrada == clave:
		print("Adivinaste la clave! :D")
		break

	for i in range(3):
		if clave[i]==entrada[i]:
			pistas.append("Hubo un match en "+str(i))
			matches.append(i)
		elif clave[i] in entrada:
			pistas.append("Estas cerca en "+str(i))

	if len(pistas) == 0:
		print("No hubo match :c")
	else: 
		print(pistas)

print("\nFin del programa")

