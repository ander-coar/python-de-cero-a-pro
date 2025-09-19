
# Ejercico 3 
# de una lista separar en lista_pares y lista_impares los numeros pares e impares respectivamente
# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
numeros_pares = []
numeros_impares = []

for numero in numeros:
    if numero % 2 == 0:
        numeros_pares.append(numero)
    else:
        numeros_impares.append(numero)

print("Numeros Pares:", numeros_pares)
print("Numeros Impares:", numeros_impares)


# en la sintaxis del for siempre debemos tener una variable diferente que recorre el iterable a la variable a iteral 

# for variable_diferente in iterable:
# bloque de codigo
# instruccion

