# Tipos de variables en Python
# Variables: son espacios en memoria donde se almacenan datos
# Tipos de variables: enteros, flotantes, cadenas, booleanos, complejos

# la variables no se determinan por su nombre, si no por su contenido o tipo de dato que almacena

# sintaxis para crear variables
# nombre_variable = valor

nombre = "Juan" 
id = 1
precio = 19.99
descuento_1 = 0.15
descuento_2 = "15%"
descuento_3 = "quince porciento"
descuento_4 = "15"
luz_encendida = True
luz_encendida = False
complejo = 3 + 5j
complejo_2 = "2 + 4j"


# las variables pueden cambiar de valor a lo largo del tiempo de ejecución por eso es de TIPADO DINAMICO

# Cuando naci mi nombre era "Ander Steven Correa Arroyave"
nombre = "Ander Steven Correa Arroyave"

# cuando mis padres hiceron mi registro de Tarjeta de identidad mi nombre el registrados lo coloco mal y me lo cambio a "Anderson Steven Correa Arroyave"

nombre = "Anderson Steven Correa Arroyave"

# Pensando en modificar mis documentos a mi nombre real "Ander Steven Correa Arroyave"
nombre = "Ricardo Jose Correa Arroyave"

# Ahora me quiero volver no Binario
nombre = 1236 

edad = 30
edad = 31
edad = 32.5
edad = "treinta y dos años" 

# Las variables en Python no necesitan declarar su tipo, pero pueden hacerlo usando anotaciones, pero aun asi no determina su tipo 

# La sintaxis para declarar el tipo de una variable es:
# nombre_variable: tipo_dato = valor
precio: float = 50.200
estado: bool = False  

# pero aun asi pueden cambiar su tipo de dato a lo largo del tiempo de ejecución
# para python no existe ningun error
# Podemos usar type checking para verificar el tipo de dato de una variable
precio = "50.200" 
estado = "True"
estado = 1

# en python no existen las constantes pero se pueden simular utilizando variables en mayusculas, aúnque se puede cambiar su valor por lo que solo es visual para el programador detectar errores

# Por convención las constantes se escriben en mayúsculas

pi = 3.1416
Pi = 3.1416 
pI = 3.1416

PI = 3.1416 
PI = 3.14 

# Se puede usar la funcion type() para obtener el tipo de una variable

nombre_profesor = "Jose Cordoba"
print(type(nombre_profesor))  # imprime <class 'str'>

id_profesor = 1
precio_credito = 300.000
estado_curso = True

nombre_profesor = 1000 # imprime <class 'int'>
print(type(nombre_profesor)) 

# La sintaxis de type() es type(variable)

type(nombre_profesor) 

print(type(nombre_profesor)) 
print(type(id_profesor))
print(type(precio_credito))
print(type(estado_curso))   

# En python puedes asignar multiples variables en una sola linea, pero no es una buena practica, aunque en algunos casos es necesario

# Tengo un grupo de 3 estudiantes
# Información de estudiante 1
nombre_estudiante_1, edad_estudiante_1, promedio_estudiante_1 = "Juan", 20, 4.5  # esto no es una buena practica

nombre_estudiante_1 = "Maria"
edad_estudiante_1 = 21
promedio_estudiante_1 = 4.8

# Ejemplo de donde si es necesario usar esta tecnica
# Información del plano cartesiano en 3d x, y, z
x, y, z = 10, 20, 30  # esto es necesario


# Convenciones de nombres de variables

# 1. Usar nombres descriptivos, cortos y significativos
# 2. Usar letras minúsculas y guiones bajos para separar palabras usando snake_case 
# 3. Evitar el uso de caracteres especiales y espacios
# 4. No comenzar los nombres de variables con números
# 5. Usar un estilo consistente en toda la base de código
# 6. Evitar el uso de nombres de variables que sean palabras reservadas
# 7. Evitar usar PascalCase
# 8. Para las constantes, se recomienda usar nombres en mayúsculas UPPER_CASE

# Ejemplos de nombres de variables incorrectos
# 1. Nombres poco descriptivos, largos y poco significativos
n = "Juan"  # no es descriptivo
a = 10  # no es descriptivo 
promedio_final_del_estudiante = 4.5  # es muy largo

# 2. Uso de mayúsculas y minúsculas inconsistente 
NombreEstudiante = "Maria"  # no es consistente
nombreEstudiante = "Maria"  # no es consistente
nombre-estudiante = "Maria"  # no es consistente    

# 3. Uso de caracteres especiales y espacios
nombre@estudiante = "Carlos"  # no es válido
nombre estudiante = "Carlos"  # no es válido
nombre#estudiante = "Carlos"  # no es válido
$precio = 100  # no es válido

# 4. Comenzar con números
1nombre = "Ana"  # no es válido
2edad = 20  # no es válido

# 6 . Uso de palabras reservadas
def = "funcion"  # no es válido 
class = "clase"  # no es válido
for = "bucle"  # no es válido
if = "condicional"  # no es válido
else = "sino"  # no es válido
range = "rango"  # no es válido 
type = "tipo"  # no es válido 

# Las palabras reservadas son las siguientes:
# False      await      else       import     pass
# None       break      except     in         raise
# True       class      finally    is         return
# and        continue   for        lambda     try
# as         def        from       nonlocal   while
# assert     del        global     not        with
# async      elif       if         or         yield


# 7. Uso de PascalCase
NombreEstudiante = "Luis"  # no es consistente
EdadEstudiante = 22  # no es consistente    
PromedioEstudiante = 4.7  # no es consistente 

# Nombre de variables correctas
nombre_estudiante = "Luis"
edad_estudiante = 22
promedio_estudiante = 4.7
area_circulo = 3.14 * (5 ** 2)  # area de un circulo de radio 5
PI = 3.14
GRADOS = 360
VELOCIDAD_LUZ = 299792458  # en metros por segundo












