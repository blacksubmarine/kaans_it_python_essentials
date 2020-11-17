#Condicionales

#if-elif-else

# /////////Ejemplo1: Queremos saber si un numero es positivo

num=int(input("Digite un numero: "))

if num>0:
    print("El numero", num, "es positivo") #salida llamando la variable con comas(,)
    #identación, bloque, sangria
elif num==0:
    print("El numero {} es cero".format(num))#salida con la funcion {} format()
else:
    print(f"El numero {num} es negativo")#nueva salida desde la version 3.6 de python f antes de las comillas y {variable}

print("Fin de la ejecución")















#//////////Condicionales Combinados////////////////
#programa que verifica la edad del usuario y valida si es correcta(menor a 100) y si es mayor de edad(mayor a 18)









#edad = int(input("digita tu edad: "))

# if edad>0:
#     if edad<100:#casi nadie jay de mas de 150 años
#         print("edad correcta")
#         if edad>=18:#condicional anidado
#             print("y eres mayor de edad")#en c/condicional hay que respetar la identacion
#         else:
#             print("pero no eres mayor de edad")
#     else:
#         print("lo dudo, edad incorrrecta")
# else:
#     print("edad incorrecta")

#///////// como simplificar el anterior codigo (and)

edad = int(input("digita tu edad: "))

if edad>0 and edad<100:
    print("edad correcta")
    if edad>=18:#condicional anidado
         print("es mayor de edad")
    else:
        print("Es menor de edad")
else:
    print("edad incorrecta")


#////////ejercicio///////////////
# Hacer un programa que pida 2 numeros y se de cuenta cual de ellos es par, o si ambos lo son
# 

# num1=int(input("ingresa el primer digito: "))
# num2=int(input("ingresa el segundo digito: "))

# if num1%2==0 and num2%2==0:
#     print("Ambos son pares")
# elif num1%2!=0 and num2%2==0:
#     print("el segundo numero es par")
# elif num1%2==0 and num2%2!=0:
#     print("el primer numero es par")
# else:
#     print("ninguno es par")


#////////ejercicio2///////////////
#Hacer un progra,a que pida 3 numeros y determine cual es mayor

# num1=int(input("ingresa el primer digito: "))
# num2=int(input("ingresa el segundo digito: "))
# num3=int(input("ingresa el primer digito: "))

# if num1>=num2 and num1>=num3:
#     print("el numero mayor es:",num1)
# elif num2>=num1 and num2>=num3: 
#     print("el numero mayor es:",num2)
# elif num3>=num1 and num3>=num2: 
#     print("el numero mayor es:",num3)

#////////ejercicio3///////////////
#hacer un programa que pida un caracter e indique si es una vocal o no.

# letra = input("Digite un caracter:")#.lower()#esta funcion transforma las mayusculas en minusculas#.upper()transforma a mayuscula
# if letra=='a' or letra == "e" or letra=='i' or letra=='o' or letra=='u':
#     print(letra,"es una vocal")
# else:
#     print(letra,"no es una vocal")

#////////ejercicio4///////////////
# Hacer un programa que simule le fucionamiento de una calculadora que puede realizar
# las 4 operaciones basicas(suma, resta, multiplicacion y division).
# El usuario debe especificar la operacion con el primer caracter del nombre de la operación.
# 
#  ''''
#  S, s - Suma
#  R, r - Resta
#  P, p, M, m - Multiplicacion
#  D, d -Division
#  ''''

# num1=float(input("ingresa el primer digito: "))
# num2=float(input("ingresa el segundo digito: "))

# operacion=input("ingresa la operacion que quieres realizar: ").upper()

# if operacion=='S':
#     suma = num1+num2
#     print("\n la suma es",suma)
# elif operacion=='R':
#     resta = num1-num2
#     print("\n la resta es",resta)
# elif operacion=='M' or operacion=='P' :
#     mult = num1*num2
#     print("\n la multiplicacion es",mult)
# elif operacion=='D':
#     division = num1/num2
#     print(f"\n la division es: {division:.2f}")
# else:
#     print("te equivicaste de operecion")

#////////ejercicio4///////////////
# Hacer un programa que simule un cajero automatico co un saldo inicial de $1000 dls 
# y tendra que el siguiente menú de opciones:
# 1. Ingresar dinero en la cuenta
# 2. Retirar dinero de la cuenta
# 3. Mostrar dinero disponible
# 4. Salir
# 


# saldo = 1000

# print("\t ..::MENU::.. ")
# print("1. Ingresar dinero en la cuenta")
# print("2. Retirar dinero de la cuenta")
# print("3. Mostrar dinero disponible")
# print("4. Salir")
# opcion=int(input("digite un opcion de menu: "))
# print()

# if opcion==1:
#     extra=float(input("cuanto dinero desea ingresar -> "))
#     saldo += extra#saldo=saldo+extra
#     print(f"dinero disponible en la cuenta es:{saldo}")
# elif opcion==2:
#     retiro=float(input("canto desea retirar ->"))
#     if retiro>saldo:
#         print("no tiene la cantidad de dinero suficiente")
#     else:
#         saldo-=retiro#saldo= saldo-retiro
#         print(f"Tu saldo es de : {saldo}")
# elif opcion==3:
#     print(f"tu saldo al momento es de {saldo}")
# elif opcion==4:
#     print("Gracias, vulva pronto")
# else:
#     print("opcion de menu no valida")


