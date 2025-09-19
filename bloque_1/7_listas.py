# Caracteristicas de las listas
# Si se pueden modificar, agregar o eliminar elementos
# Puede tener multiples tipos de datos

# sintaxis para crear una lista
mi_lista = [1, 2, 3, 4, 5] # lista de enteros
lista_vacia = [] # lista vacia
lista_mixta = [1, "dos", 3.0, True, [5, 6, 7], ("a","b","c", [8, 9, 10])] # lista con multiples tipos de datos

# Las listas es como un carrito de compras, donde puedes agregar, eliminar o modificar diferentes productos
"""
print(lista_mixta[1]) # Acceder al primer elemento de la lista 
print(lista_mixta[4]) # Acceder a una lista interna 
print(lista_mixta[4][1]) # Acceder a un elemento de una lista interna
print(lista_mixta[-1]) # Acceder al ultimo elemento de la lista 
print(lista_mixta[5][3][1])  # Acceder a un elemento de una tupla interna que esta dentro de una lista interna
"""  
# Metodos mas comunes de las listas
# append() Agrega un elemento al final de la lista
vocales = ['a', 'e', 'i']
print(vocales)
vocales.append('o') 
print(vocales)
vocales.append('u')
print(vocales) 
print("-------------------")

# insert() Agrega un elemento en una posicion especifica    
alumnos_ranking = ['Juan', 'Maria', 'Pedro']
alumnos_ranking.insert(0, "Ana") # Agrega a Ana en la posicion 0
print(alumnos_ranking) 
print("-------------------")

# extend() Agrega multiples elementos al final de la lista
abcedario = ['a', 'b', 'c'] 
abcedario.extend(['d', 'e', 'f'])
print(abcedario) 

# como podemos agregar multiples elementos a una lista sin usar extend()
abcedario += ['g', 'h', 'i'] 
abcedario = abcedario +  ['j', 'k', 'l']
print(abcedario)

# remove() Elimina un elemento por su valor
# Elimina el primer elemento que encuentra con ese valor
abcedario.remove("e") # Elimina la letra "e" de la lista abcedario
print(abcedario) 


# pop() Elimina un elemento por su indice  
# pop guarda el elemento eliminado en una variable 

letra_eliminada = abcedario.pop(3) # Elimina la letra "d" de la lista abcedario
print(abcedario) 
print("Letra eliminada:", letra_eliminada)


# clear() Elimina todos los elementos de la lista 
# usamos clear para hacer un reset de la lista
# abcedario.clear() 
# print(abcedario)

# index() Devuelve el indice de un elemento 
print(abcedario.index("j"))

# count() Devuelve la cantidad de veces que aparece un elemento
abcedario.append("j")
print(abcedario.count("j"))
print("-------------------")
print(abcedario)

# sort() Ordena los elementos de la lista 
# sort modifica la lista original
numeros = [5, 2, 9, 1, 5, 6]
numeros.sort() 
print(numeros) 

letras = ['d', 'a', 'c', 'b', "A"]
letras.sort()
print(letras)

frutas = ["manzana", "pera", "banana", "kiwi", "anana", "Cereza"] # Ordena las frutas alfabeticamente pero si hay mayusculas las pone primero tambien alfabeticamente
frutas.sort()
print(frutas) 

# con sort podemos usar el parametro reverse para ordenar de forma descendente
frutas.sort(reverse=True)  
print(frutas)

# sorted() Ordena los elementos de la lista pero no modifica la lista original 
# La diferencia entre sort() y sorted() es que sort() modifica la lista original y sorted() no modifica la lista original, sino que devuelve una nueva lista ordenada  

paises = ["Argentina", "Brasil", "Chile", "Uruguay", "Paraguay", "Bolivia"]
paises_ordenados = sorted(paises) 
print(paises)
print(paises_ordenados) 

# reverse() Invierte el orden de los elementos de la lista 
paises_ordenados.reverse() 
print(paises_ordenados)

# copy() Crea una copia de la lista 
notas_juan = [10, 9, 8, 7, 6] 
notas_juan_copia = notas_juan.copy()
print(notas_juan)
print(notas_juan_copia)

notas_juan_copia.append(5.8)
print(notas_juan)
print(notas_juan_copia)

