# Ejercicio 1 Filtrar los nombres que tengan mas de 4 letras
# Los nombres que tengan mas de 4 letras se guardaran en una lista llamada nombres_filtrados

nombres = ["Ana", "Juan", "Pedro", "Maria", "Luisa", "Carlos"]
print("en la lista hay: ", len(nombres)) # len() devuelve la cantidad de elementos de una lista o cadena de texto
# caja 0 = ana 
# caja 1 = Juan

# ana tien un indice 0
# juan tiene un indice 1
# pedro tiene un indice 2
# maria tiene un indice 3
# luisa tiene un indice 4
# carlos tiene un indice 5

nombres_filtrados = [] # aqui iran los nombres filtrados que tengan mas de 4 letras

"""
for n in nombre_variable:
    # bloque de codigo
    instruccion
"""
# el ciclo for itera sobre una lista o cadena de texto
# n es una variable que toma el valor de cada elemento de la lista en cada iteracion

#["Ana", "Juan", "Pedro", "Maria", "Luisa", "Carlos"]
for nombre in nombres:
    print(nombre) 
    if len(nombre) > 4: # len(nombre) devuelve la cantidad de letras del nombre
        nombres_filtrados.append(nombre) # append() agrega un elemento al final de una lista



print("nombres filtrados: ", nombres_filtrados)
print("nombres originales: ", nombres)



# Ejercio 2 usar while  para sumar numeros de una lista hasta que la suma sea mayor a 15
# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Ejercico 3 
# de una lista separar en lista_pares y lista_impares los numeros pares e impares respectivamente
# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

#ejercicio 4 
# de una lista de numeros validar si en ella hay esta el numer 5, si esta imprimir "el numero 5 esta en la lista", si no esta imprimir "el numero 5 no esta en la lista"
# lista_numeros = [1, 2, 3, 4, 6, 7, 8, 9, 10]

#ejercicio 5
# Eliminar de una lisa los numeros que sean iguales a un valor dado
# lista_numeros = [1, 2, 3, 4, 5, 6, 5, 7, 8, 5, 9, 10, 5, 5]


# Averiguar cómo funciona enumarate con for y while





