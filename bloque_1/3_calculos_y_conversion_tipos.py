# Casting de datos o conversion de tipos
# se trata de convertir un tipo de dato en otro
# En python se pueden realizar conversiones de tipos de forma implicita y explicita
# la conversion implicita se realiza automaticamente por el interprete de python
# la conversion explicita se realiza utilizando funciones de conversion de tipos como str(), int(), float(),bool(), etc.

# Ejemplo de conversion implicita
a = 10 # int 
b = 5.5 # float
c = a + b 
print(c) # 15.5

# Ejemplo 2 de conversion implicita

x = 10 # int
y = 2.5 # float
z = x * y
print(z) # 25.0

# Ejemplo de conversion explicita

# conversion explicita de str a int
num1 = "100" # str
num2 = 200 # str

suma = int(num1) + num2 
print(suma) # 300

print(type(num1)) 

# conversion explicita de float a int

decimal = 9.99
entero = int(decimal)
print(entero) 
print(type(entero))

# conversion explicita de str a float

num_decimal = "3.14"
num_decimal_conv = float(num_decimal)
print(num_decimal_conv)
print(type(num_decimal_conv))
print(num_decimal)
print(type(num_decimal))

# convertir un str a int
# edad = "treinta"
# edad_int = int(edad) 
# print(edad_int) # esto genera un error ValueError: invalid literal for int() with base 10: 'treinta'

# conversion explicita de str a bool
valor_str = "True" 
valor_bool = bool(valor_str)
print(valor_bool) # True

# conversion explicita de int a bool
valor_int = 1
valor_bool_2 = bool(valor_int)
print(valor_bool_2) # True

cualquier_numero = -15 # cualquier numero diferente de 0 es True asi sea negativo o decimal
valor_bool_3 = bool(cualquier_numero)
print(valor_bool_3) # True

# conversion explicita de str a complejo
num_complejo_str = "3+4j"
num_complejo = complex(num_complejo_str)
print(num_complejo) # (3+4j)
print(type(num_complejo)) # <class 'complex'>

# Podemos concatenar dos str utilizando el operador +
nombre = "Juan"
apellido = "Perez"
nombre_completo = nombre + " " + apellido # El operador + concatena dos str 

print(nombre_completo) # JuanPerez


# Python tiene tipado  fuerte, lo que significa que no se pueden realizar operaciones entre tipos de datos diferentes sin una conversión explícita de tipos
# python no realiza conversiones de tipos de forma automatica entre tipos de datos diferentes
# Para calculos matemáticos, es importante asegurarse de que los tipos de datos sean compatibles

print("Operaciones matematicas\n")

#signos de operaciones matematicas
# suma + 

num1 = 10
num2 = 5.5
resultado = num1 + num2
print(resultado) # 15.5

# resta -   

resultado_resta = num1 - num2
print(resultado_resta) # 4.5

# multiplicacion *
resultado_multiplicacion = num1 * num2
print(resultado_multiplicacion) # 55.0

# division /
resultado_division = num1 / num2
print(resultado_division) # 1.8181818181818181


# division entera //
resultado_division_entera = num1 // num2
print(resultado_division_entera) # 1.0

# modulo % # devuelve el residuo de una division 
# lo podemos usar para saber si un numero es par o impar 
resultado_modulo = num1 % num2
print(resultado_modulo) # 4.5


# potencia **

resultado_potencia = num1 ** 2
print(resultado_potencia) # 100
resultado_potencia_2 = num2 ** 3

# orden de operaciones: primero se realizan las operaciones dentro de paréntesis, luego las potencias y raices, luego multiplicaciones y divisiones, y finalmente sumas y restas
# en caso de que haya operaciones del mismo nivel, se realizan de izquierda a derecha 












