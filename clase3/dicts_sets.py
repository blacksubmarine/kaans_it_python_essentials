my_dict = {}
print(type(my_dict))
#agregando elementos
my_dict["key"] = 1
d = {1: "a", 2: 2.5,"a":[1,2,3],"val":"esto es un diccionario"}
print(d)
#conjunto de llaves y de valores
print(d.items())
#llaves
print(d.keys())
#valores
print(d.values())
#del d[1]
#print(d)
x = [1,2,3,4,5,6,7,8,9]
x = list(range(100))
#para borrar variables o partes de variables se usa del
del x[0:4]
#print(x)
d.pop(1)
print("este es mi diccionario: ")
d[2]="pera"
print(d)
d2 = d.copy()
print(d2)
lista = [2,1,1,"x","y",2,3,4,8,76,4,3,1,2,2,"y"]
conjunto = set(lista)
print("Esto es un conunto:",conjunto)
conjunto.add(100)
print(conjunto)
#conjunto[0] = 1
print(conjunto)



