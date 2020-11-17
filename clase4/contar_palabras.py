# programa que cuenta cuantas palabras diferentes 
# hay en un texto y cuantas veces se repite cada una
mensaje = "Bello es mejor que feo. Explícito es mejor que implícito. Simple es mejor que complejo. Complejo es mejor que complicado. Plano es mejor que anidado. Espaciado es mejor que denso. La legibilidad es importante. Los casos especiales no son lo suficientemente especiales como para romper las reglas. Sin embargo la practicidad le gana a la pureza. Los errores nunca deberían pasar silenciosamente. A menos que se silencien explícitamente. Frente a la ambigüedad, evitar la tentación de adivinar. Debería haber una, y preferiblemente solo una, manera obvia de hacerlo. A pesar de que esa manera no sea obvia a menos que seas Holandés. Ahora es mejor que nunca. A pesar de que nunca es muchas veces mejor que *ahora* mismo. Si la implementación es difícil de explicar, es una mala idea. Si la implementación es fácil de explicar, puede que sea una buena idea. Los espacios de nombres son una gran idea, ¡tengamos más de esos!"

import re
# Import re nos permite utilizar expresiones regulares
# Lo que nos permite buscar patrones en palabras 
# re.sub nos permite quitar palabras con acentos, numeros y signos de puntuacion
texto_normalizado = re.sub('[^A-Za-z ]+', '', mensaje)




#volvemos todas las letras en minusculas para que
# HoLa y hola cuenten como las mismas palabras
texto_normalizado = texto_normalizado.lower()
# solo quitamos acentos y simbolos para normalizar el texto

#con split volvemos la cadena en una lista, cada elemento es creado por los espacios que tenia la cadena
#ejemplo: "hola adios".split() ---> ["hola","adios"]
texto_normalizado = texto_normalizado.split()



print("#"*15)

print(texto_normalizado)

# creamos un diccionario vacio
word_count = {}

#por cada palabra que exista en el texto la agregamos al diccionario como llave y le asignamos un uno
#el uno significa que al menos aparece una vez en el texto
#si la volvemos a encontrar, le sumamos a su valor otro uno
for word in texto_normalizado:
	if word in word_count:
		word_count[word]+=1
	else:
		word_count[word] = 1


print("\n"*2)
print("#"*15)
print("\n"*2)

# imprimimos las llaves con los valores del diccionario	
for items in word_count.items():
	print(items)
