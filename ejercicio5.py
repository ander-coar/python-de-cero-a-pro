#ejercicio 5
# Eliminar de una lisa los numeros que sean iguales a un valor dado
# lista_numeros = [1, 2, 3, 4, 5, 6, 5, 7, 8, 5, 9, 10, 5, 5]

numeros = [1, 2, 3, 4, 5, 6, 5, 7, 8, 5, 9, 10, 5, 5]


num = int(input("Ingrese el numero que deseas eliminar: "))

indice_num = []

# este codigo busca todas las apariciones del numero seleccionado y muestra sus indices en la lista
# funciona como una copia de seguridad por si queremos volver a insertar el numero en la lista en su posición correspondiente
if num in numeros: # con esta linea verifico si por lo menos una vez esta el numero en la lista
    for i in range(len(numeros)): # cuando usamos range() debemos usar len() para obtener la longitud de la lista en este caso va de 0 a 14 sin tener en cuenta el "14"
        if numeros[i] == num:
            indice_num.append(i)
    print(f"El numero {num} está en las posiciones: {indice_num}")
else:
    print("El numero no está en la lista")

# este codigo elimina todas las apariciones del numero seleccionado de la lista
while num in numeros:
    numeros.remove(num)
print("Lista actualizada:", numeros)

# ejercicio 
# volver a insertar el numero en la lista en su posición correspondiente









