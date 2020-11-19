#bucle while
#bucle con un numero indeterminado de condiciones
#raiz cuadrada de un numero(a fuerza es un nuero positivo)

# import math

# num=int(input("Digite un numero: "))
# #aqui el usuario nos puede dar cualquier numero asi que tenemos qe verificar qe el numero sea positivo

# while num<0:
#     print("Error porfa ingresa un numero positvio")
#     num=int(input("Digite un numero: "))

# print(f"\nsu raiz cuadrada es: {(math.sqrt(num)):.2f}")

#/////////////////////////////
#while con un numero determinado de iteraciones
#mostrar un mensaje 10 veces

# i=0
# while i<10:
#     print("hola mundo")
#     i+=1#i=i+1

#////////////////////////
# mostrar los numeros del 0 al 9

# i=0
# while i<10:
#     print(i)
#     i+=1
#////////////////////////
# mostrar los numeros del 1 al 10
i=1
while i<=10:
    print(i)
    i+=1


#///////////////bucles infinitos no intencionados///////
#El programador ha olvidado modificar la variable de control dentro del bucle y el programa 
# imprimirá números 1 indefinidamente:

# i = 1
# while i <= 10:
#     print(i, end=" ")

#/////////
#El programador ha escrito una condición que se cumplirá siempre y el programa 
# imprimirá números consecutivos indefinidamente

# i = 1
# while i > 0:
#     print(i, end=" ")
#     i += 1


#/////<
#Se aconseja expresar las condiciones como desigualdades en vez de comparar valores. 
# En el ejemplo siguiente, el programador ha escrito una condición que se cumplirá 
# siempre y el programa imprimirá números consecutivos indefinidamente:

i = 1
while i != 100:
    print(i, end=" ")
    i += 2