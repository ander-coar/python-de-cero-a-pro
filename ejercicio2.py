# Ejercio 2 usar while  para sumar numeros de una lista hasta que la suma sea mayor a 15
# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 


numeros = [1, 2, 3, 4, 2, 6, 7, 8, 9, 10]
suma = 0
i = 0
num_seleccionado = []
suma_actual = []

while suma < 15 and i < len(numeros):
    suma += numeros[i]
    suma_actual.append(suma)
    num_seleccionado.append(numeros[i])
    i += 1
    
print("La suma total es de: ", suma)
print("Los numeros seleccionados son: ", num_seleccionado)
print("Las sumas parciales fueron: ", suma_actual)

# -------























