
#///////////////////////
# Realiza una función llamada area_rectangulo(base, altura) que devuelva el 
# área del rectangulo a partir de una base y una altura. Calcula el área de 
# un rectángulo de 15 de base y 10 de altura:

# def area_rectangulo(base, altura):
#     return base*altura

# print( area_rectangulo(15,10) )


# Realiza una función llamada intermedio(a, b) que a partir de dos números, 
# devuelva su punto intermedio. 
# Cuando lo tengas comprueba el punto intermedio entre -12 y 24:






# def intermedio(a, b):
#     return (a + b) / 2

# print( intermedio(-12, 24) )



#//////////////////////////////////////////////////////////
# Realiza una función llamada relacion(a, b) que a partir de dos números que cumpla lo 
# siguiente:

# Si el primer número es mayor que el segundo, debe devolver 1
# Si el primer número es menor que el segundo, debe devolver -1
# Si ambos números son iguales, debe devolver un 0.

# Comprueba la relación entre los números: '5 y 10', '10 y 5' y '5 y 5'

def relacion(a, b=2):
    if a > b: 
        return 1
    elif a < b:
        return -1
    else:
        return 0

print( relacion(5, 10) )
print( relacion(10, 5) )
print( relacion(b=1) )


#//////funciones globales y locales//////////////
# Define función

# def acelerar():
#     # Declara la variable 'km' como global
#     # Ahora se podrá utilizar dentro de la función
#     global km
    
#     # Declara variable local (ámbito función)
#     tiempo = 1

#     # Se incrementa la velocidad en 5 km
#     km+= 5

# # Define variable local (ámbito programa principal)
# km = 10

# # Muestra variable 'km'
# print('Velocidad:', km)  # velocidad: 10

# # Llama a la función acelerar()
# acelerar()

# # Muestra variable 'km'
# print('Velocidad:', km)  # velocidad: 15

# # Intenta mostrar la variable 'tiempo'
# # Se produce una excepción (error) de tipo NameError
# # porque la variable no pertenece a este ámbito:
# # NameError: name 'tiempo' is not defined
# print('Tiempo:', tiempo)