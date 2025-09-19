
#ejercicio 4 
# de una lista de numeros validar si en ella hay esta el numer 5, si esta imprimir "el numero 5 esta en la lista", si no esta imprimir "el numero 5 no esta en la lista"
# lista_numeros = [1, 2, 3, 4, 6, 7, 8, 9, 10]

lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

"""
resultado = 5 in lista_numeros
if resultado:
    print("El numero 5 esta en la lista")
else:
    print("El numero 5 no esta en la lista")
"""

# esta opcion es la segunda mas recomendada
"""" 
if 5 in lista_numeros:
        print("El numero 5 esta en la lista")
else:
        print("EL numero no esta en la lista") 
"""

# Esta ocpion es la mas recomendada pero menos legible
print("El numero 5 está en la lista" if 5 in lista_numeros else "El número 5 no está en la lista")


# resultado_2 = "el numero si esta en la lista" if 5 in lista_numeros else "El numero no esta # en la lista"
# print(resultado_2)


# el operador ternario es una forma corta de escribir un condicional if-else en una sola línea
# syntaxis:
# instruccion_verdadera if condicion else instruccion_falsa 

