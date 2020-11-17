cad = "hola esto es una cadena"
# longitud de una lista o string es con len(variable)
print(len(cad))
long = len(cad)
print(cad[long-1])
print(cad[-1])

# rango entre la cadena
print(cad[5:10])
#saltando
steps=4
print(cad[0::steps])
#reversa
print(cad[::-1])
#inicio < final
# el indice no debe de ser mayor a la longitud de la cadena
cad = "hola esto es una cadena"

#la linea de abajo es un error de ejecucion
#print(cad[-24])
# pyt


cad = "python"
print(cad[2:])
print(cad[2:5])
print(len(cad))
#listas

# no se puede hacer ejecucion de la siguiente linea
#cad[3]="s" # los valores por separado de los strings son inmutables


cad = "p y t h o n"
#split = separa un string con un token y me genera una lista
lista = cad.split("t")
print(lista)
lista = [1,2.5,3,4,5,"s",True,[6,7,8]]
print(lista)
lista[0]= "Python"
print(lista)
x = 10
print(x in lista)
print(lista)
print(1 not in ["a","b"])
#
lista1 = [1,2,3,4,5]
lista2 = lista1.copy()
lista1[0] = "s"
print(lista1)
print(lista2)

#metodos de strings
cad= "hola esto es una cadena"
cad = cad.upper()
print(cad)
cad = cad.lower()
print(cad)
#preguntas de examen: split, upper, lower, copy
cad = cad.capitalize()
print(cad)
#metodos de lista
lista =[5,3,2,8,9,11,-5,-2,100]
print(lista)
#print(sorted(lista))
l=len(lista)
lista.insert(l,"XXX")
lista.reverse()
print(lista)
# #00000000
# #00000010 -> 2
# #00000100 -> 4
# #00001000 -> 8
# lista.remove("XXX")
# #pop es parecido al remove pero este en vez de un valor va a pedir una posicion
# lista.pop(1)
# #contamos ocurrencias de un valor dado
# print("El elemento: ",2,"se repite : ",lista.count(2),"vez")
lista =  [1,2,3,4,5,[6,7,8,9]]
print()
print(lista)
lista.extend(["a","b","c"])
print(lista)
# ############################################################
tpl = tuple(lista)

print(tpl)
#listas anidadas
print(lista[5][2])