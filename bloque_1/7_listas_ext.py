abcedario = ["a", "c", "b", "d", "e", "f", "g", "h", "i", "j", "k", "l"]
# Esto genera un none porque sort() no devuelve nada y modifica la lista original
abcedario.sort()
print(abcedario)

# rebanado de listas (slicing)
# sintaxis: lista[inicio:fin:paso] 

print(abcedario[0:6:3]) # obtiene los primeros 5 elementos
print(abcedario[::]) # invierte la lista
print(abcedario[6:0:-1]) # invierte la lista
print(abcedario[6::-1]) # invierte la lista 

print(abcedario[1:7:]) # invierte la lista
print(abcedario[5::]) # invierte la lista


# si utilizo sclicing para invertir una lista, no modifica la lista original y si agrego un inicio y un fin me tomara una sublista de forma descendente 

notas = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

suma_notas = sum(notas) 
print("Suma de notas:", suma_notas)
print(len(notas))

promedio_notas = suma_notas / len(notas) 
print("Promedio de notas:", promedio_notas)


# Ejercicio practico 
# Calcular cuantas personas asistieron a una clase
# y cuantas no asistieron, usando una lista de booleanos
# y calcular el total de asistencias
asistencias = [True, True, False, True, False, True, True, True, False, True]
personas_asistieron = sum(asistencias)
total_asistencias = len(asistencias)
print("Total de asistencias:", total_asistencias)
personas_no_asistieron = len(asistencias) - personas_asistieron
print("Personas que no asistieron:", personas_no_asistieron)
print("Personas que asistieron:", personas_asistieron)

print("-------------------") 


# fuciones de listas que pueden usar 
# max() Devuelve el elemento con el valor maximo
# min() Devuelve el elemento con el valor minimo
# list() Convierte un iterable en una lista

numeros = [5, 2, 9, 1, 5, 6]
num_max = max(numeros)
num_min = min(numeros) 
print("Numero maximo:", num_max)
print("Numero minimo:", num_min) 









