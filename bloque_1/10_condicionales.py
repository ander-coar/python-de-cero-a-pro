# Una condicional es una estructura que permite ejecutar diferentes bloques de código
# en función de si una condición es verdadera o falsa. 

# syntaxis: 
""" 
if condicion:
    # bloque de código si la condición es verdadera
else:
    # bloque de código si la condición es falsa
"""

edad = 17
aprobo_curso_manejo = True

# Ejemplo de condicional simple

if edad >= 18: 
    print("Eres mayor de edad")
else: 
    print("Eres menor de edad") 

# Ejemplo de condicional compuesta
# Validar si una persona puede obtener una licencia de conducir
# para obtener una licencia de conducir debe ser mayor de edad y tener un curso de manejo aprobado

if edad >= 18:
    print("Es mayor de edad")
    if aprobo_curso_manejo:
        print("Puede obtener una licencia de conducir")
    else:
        print("No puede obtener una licencia de conducir, debe aprobar el curso de manejo")
else:
    print("No puede obtener una licencia de conducir, es menor de edad")


if edad >= 18 and aprobo_curso_manejo == True: 
    print("Puede obtener una licencia de conducir")
else:
    print("No puede obtener una licencia de conducir")

# ejemplo con or 
# Valiar si una persona puede entrar a un bar
# para entrar a un bar debe ser mayor de edad o tener una identificacion oficial

edad_bar = 16 
tiene_identificacion = False

if edad_bar >= 18 or tiene_identificacion:
    print("Puede entrar al bar")
else:
    print("No puede entrar al bar") 




# >= Mayor o igual que
# <= Menor o igual que
# > Mayor que
# < Menor que
# == Igual que  
# != Diferente que 
# and Y
# or O  
# not No
# is Es (compara si dos variables son el mismo objeto en memoria)
# is not No es (compara si dos variables no son el mismo objeto en memoria)
# in (verifica si un elemento existe en una secuencia como una lista, tupla o cadena)
# not in (verifica si un elemento no existe en una secuencia como una lista, tupla o cadena)

