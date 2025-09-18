# enumerate se utiliza para iterar sobre un objeto iterable y obtener tanto el índice como el valor del elemento en cada iteración.
# La función enumerate() toma un iterable (como una lista, tupla o cadena) y devuelve un objeto enumerado que contiene pares de índice y valor.

# es normal usarlo con bucles for aunque se puede usar en otras situaciones 

frutas = ["manzana", "pera", "banana", "kiwi", "piña", "Cereza"]
coordenadas = (1.89, 2.5, 3.6)
print(frutas)

enum_obj = enumerate(frutas)
corr_enum_obj = enumerate(coordenadas, start=500)
# enumerate funciona cómo una lista trasportadora cargada de cajas y entrega un indice y valor en cada iteracion

print(next(enum_obj)) # (0, 'manzana') 
print(next(enum_obj)) # (1, 'pera')
print(next(enum_obj)) # (2, 'banana')
print(next(enum_obj)) # (3, 'kiwi')
print(next(enum_obj)) # (4, 'piña')
print(next(enum_obj)) # (5, 'Cereza')


print(next(corr_enum_obj)) # (1, 1.89)
print(next(corr_enum_obj)) # (2, 2.5)   
print(next(corr_enum_obj)) # (3, 3.6)


"""
1 manzana
2 pera
3 banana
4 kiwi
5 piña
6 cereza
"""
