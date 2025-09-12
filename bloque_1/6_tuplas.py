# una tupla es una colección de elementos que están ordenados y son inmutables.
# se definen utilizando paréntesis () y los elementos se separan por comas.
tupla = (1, 2, 3)

# a diferencia de las listas, las tuplas son inmutables, lo que significa que no se pueden modificar una vez creadas. (osea no se puede agregar, eliminar o modificar elementos)

"""
tupla_coordenadas = (1.8, 2.4, 3.6) # tupla de coordenadas x,y,z
print(tupla_coordenadas)

tupla_multi_coordenadas = ((1.8, 2.4), (3.6, 4.8)) # tupla de tuplas
print(tupla_multi_coordenadas)

tupla_vacia = () # tupla vacía
print(tupla_vacia)

tupla_un_elemento = (1,) # tupla con un solo elemento, se necesita la coma para diferenciarla de un paréntesis normal
print(tupla_un_elemento)

tupla_sin_parentesis = 1, 2, 3 # tupla sin paréntesis, se crea automáticamente al separar los elementos por comas
print(tupla_sin_parentesis)
"""

# no podemos modificar los elementos de una tupla, pero podemos acceder a ellos mediante índices
tupla_mixta = (1, "dos", 3.0, True) # tupla con diferentes tipos de datos
#print(tupla_mixta)

# tupla_mixta[0] = "otro valor"
# print(tupla_mixta)

# acceder a los elementos de una tupla mediante índices
"""
numeros_enteros = (1,2,3,4,5,6,7)
print(numeros_enteros) # acceder al primer elemento
print(numeros_enteros[2]) # acceder al primer elemento
print(numeros_enteros[-1]) # acceder al último elemento
print(numeros_enteros[-2])

# podemos usar slicing para obtener sub-tuplas o rebanadas de una tupla
# sintaxis: tupla[inicio:fin:paso]
primeros_tres = numeros_enteros[0:3:2] # obtener los primeros tres elementos
print(primeros_tres)

#puedo invertir una tupla usando slicing pero ojo no es el orden 
invertida = numeros_enteros[::-1] # invertir la tupla
print(invertida)
"""
# metodos propios de las tuplas
# count: cuenta cuántas veces aparece un elemento en la tupla
# index : devuelve el índice de la primera aparición de un elemento en la tupla

abecedario = ('a', 'b', 'c', 'd', 'e', 'a', 'b', 'a', 'x' , 'g') 
print(abecedario)
print(abecedario.count('a')) # cuenta cuántas veces aparece 'a' en la tupla
print(abecedario.index('d')) # devuelve el índice de la primera aparición de 'd' en la tupla

# podemos otros metodos con las tuplas que son:
# len(): devuelve la longitud de la tupla
# min(): devuelve el valor mínimo de la tupla
# max(): devuelve el valor máximo de la tupla
# sum(): devuelve la suma de los elementos de la tupla (solo si son numéricos)
# tuple(): convierte una lista en una tupla

print(len(abecedario))
print(min(abecedario))
print(max(abecedario))
# print(sum(abecedario)) # error porque no son numéricos

lista_numeros = [8,2,3,3,4,5,1]
print(lista_numeros)
print(min(lista_numeros))
print(max(lista_numeros))
print(sum(lista_numeros), end="\n\n")

# ejercicio de usar tuplas para calcular el promedio de notas
notas = (1.2, 2.5, 3.8, 4.0, 5.0)
promedio = sum(notas) / len(notas)
print(f"El promedio de las notas es: {promedio}\n") 


texto = "hola mundo"
print(len(texto))
print(type(texto))
texto_tupla = tuple(texto)
print(type(texto_tupla))
print(texto_tupla)





