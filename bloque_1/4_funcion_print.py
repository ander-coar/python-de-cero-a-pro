# Maneras de mostrar algo en pantalla
print("Hola Mundo con comillas dobles", end = " ------- ")
print('Hola Mundo con comillas simples', sep=" +++ ")
print(15 , sep = " - ", end = " *** ")
print(3.1416)
print(True)
print(None, end = "\n\n")

print("El resultado de 3 > 2 es:", end = " ")
print(3 > 2)

# 1. Usando la función print()
nombre = "Juan"
print (nombre, end = " \n\n")

# 2. usando la concatenación de cadenas 
# no les recomiendo usar esta forma
texto1 = "Hola"
texto2 = "Compañeros"
edad = 30

print(texto1 + " " + texto2 + " mi nombres es Ander y mi edad es " + str(edad), end= "\n\n")

# 3. usando la coma 

nota1 = 4.5
nota2 = 3.8
nota3 = 5.0
nota4 = 4.2

print("Mis notas son:", nota1, nota2, nota3, nota4, sep=" ", end = "\n\n")
print("Mi promedio es:", (nota1 + nota2 + nota3 + nota4) / 4, end = "\n\n")
print(nota1, nota2, nota3, nota4)


# 4. usando el formato de cadenas .format() 
# la forma mas moderna y recomendable es usando f-strings
# sintaxis: f"texto {variable} texto {expresion}"
otras_nota1 = 4.5
otras_nota2 = 3.8
otras_nota3 = 5.0
otras_nota4 = 4.2


print('Esto es usando f-strings')
print(f'Mis notas de este semestre son: {otras_nota1}, {otras_nota2}, {otras_nota3}, {otras_nota4}')
print(f"mi promedio es: {(otras_nota1 + otras_nota2 + otras_nota3 + otras_nota4) / 4}")

print('\n\tEstoy estudiando "Ciencias de Datos"\n')

# la mas recomendable y moderna es usando f-strings

# codigos de escape
# \n - nueva linea
# \t - tabulacion
# \\ - barra invertida
# \' - comilla simple
# \" - comilla doble
# \r - retorno de carro
# \b - retroceso
# \f - avance de pagina






