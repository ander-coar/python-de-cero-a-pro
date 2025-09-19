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



