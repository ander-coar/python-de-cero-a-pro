# La función input() se utiliza para obtener datos del usuario
# La entrada del usuario se recibe como una cadena de texto (str)
# Se puede utilizar la función int() para convertir la entrada a un número entero
# Se puede utilizar la función float() para convertir la entrada a un número de punto flotante

# input tambien puede registrar valores seprarados por coma a dos o mas variables


"""
nombre = input('Ingrese su nombre:')
edad = input("Ingrese su edad: ") 
hobbies = input("di cuales son tus hobbies: ")
estado_switch = input("Estado del swhitch (True/False): ")
# Lo que el usuario ingresa siempre es una cadena de texto 

print(nombre, edad, hobbies, estado_switch)
print(type(nombre))
print(type(edad))
print(type(hobbies))
print(type(estado_switch))


# Calcular promedio de notas
nota1 = input("Ingrese la primera nota: ") 
nota1_float = float(nota1) # hacer esto no es la manera mas eficiente

nota1 = float(input("Ingrese la primera nota: ")) #4.1 str -> float 4.1 float
"""
"""
# Solicitar notas en una sola linea
nota1, nota2, nota3, nota4, nota5 = input("ingrese sus 5 notas y separelas por un espacio:").split(" ")
print(f"nota 1 es: {nota1}\nnota 2 es: {nota2}\nnota 3 es: {nota3}\nnota 4 es: {nota4}\nnota 5 es: {nota5}")

# convertir las notas a float
nota1 = float(nota1)
nota2 = float(nota2)
nota3 = float(nota3)
nota4 = float(nota4)
nota5 = float(nota5)
"""

# promedio = (nota1 + nota2 + nota3 + nota4 + nota5) / 5
#print(f"Su promedio es: {promedio}")

codigo_pais, pais, ciudad = input("ingrese su codigo de pais, pais y ciudad separados por coma:").split(",")

print(codigo_pais,pais,ciudad)







