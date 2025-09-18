# While nos sirve para repetir un bloque de codigo mientras una condicion sea verdadera 

# Ejemplo 1: Contar de 1 a 5 usando while 

# Syntaxis:
"""
while condicion:
    # bloque de codigo
    # bloque de codigo
    # bloque de codigo
"""
#contador = 0
#while contador < 5:
#    contador += 1 # contador = contador + 1
#    print("Contador:", contador)    

# Ejemplo 2: Pedir un numero al usuario hasta que ingrese un numero valido 
"""
numero = 0
print(type(numero))
while numero <= 0:
    numero = int(input("Ingresa un numero mayor que 0: "))
    if numero <= 0: 
        print("El numero debe ser mayor que 0")
    else:
        print("El numero es valido:", numero)
"""

# Ejemplo 3 pedir un numero y validar si es diferente de 0
# != Diferente que  

numero = 1
while numero != 0 and numero > 0:
    numero = int(input("Ingresa un numero diferente de 0: "))
    if numero > 0: 
        print("El numero es mayor a cero, saliendo del bucle")
    else:
        print("El numero es diferente de 0 pero en negativo, intenta de nuevo")


