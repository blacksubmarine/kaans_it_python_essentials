"""
esto es un comentario con varias lineas

esto no se ejecuta

"""
#este es un comentario

"""
print(type(edad))
edad = int(edad)
print(type(edad))
"""

nombre = ""
edad = 0
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))
num = 10_000_000
cadena = ("y mi nombre es "+nombre+" "+apellido)*10
print("Mi edad es",edad, cadena,num,sep="**",end="___")
#print("Mi edad es",edad, "y mi nombre es",nombre,sep="****",end=" ")
mensaje = "Mi edad es {} y mi nombre es {} ".format(edad,nombre)
#print(mensaje)