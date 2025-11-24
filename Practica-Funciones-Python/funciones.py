# ---------------------------------------------------
# - Funciones en Python
# ---------------------------------------------------

from functools import reduce

def saludar():
    """Función que imprime un saludo genérico."""
    print("¡Hola! Bienvenido a la práctica de funciones en Python.")
saludar()  # Llamada a la función para saludar al usuario

def saludo_personalizado(nombre):
    """Función que imprime un saludo personalizado."""
    print(f"¡Hola, {nombre}! Es un placer conocerte.")
saludo_personalizado("Ana")  # Llamada a la función con un nombre personalizado

def saludo_con_edad(nombre, edad = 25): #hago opcional la edad
    """Función que imprime un saludo con el nombre y la edad del usuario."""
    print(f"¡Hola, {nombre}! Tienes {edad} años.")
saludo_con_edad("Luis", 30)  # Llamada a la función con nombre y edad
saludo_con_edad("Marta")     # Llamada a la función con nombre y edad por defecto   

def sumar(a, b):
    """Función que devuelve la suma de dos números."""
    return a + b
resultado = sumar(5, 7)  # Llamada a la función para sumar dos números
print(f"La suma de 5 y 7 es: {resultado}")

def es_par(numero):
    """Función que verifica si un número es par."""
    return numero % 2 == 0
numero = 10
if es_par(numero):  # Llamada a la función para verificar si el número es par
    print(f"El número {numero} es par.")
else:
    print(f"El número {numero} es impar.")

def factorial(n):
    """Función que calcula el factorial de un número."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
num = 5
fact = factorial(num)  # Llamada a la función para calcular el factorial
print(f"El factorial de {num} es: {fact}")

# keyword arguments
def presentar_persona(nombre, edad, ciudad):
    """Función que presenta a una persona con su nombre, edad y ciudad."""
    print(f"Me llamo {nombre}, tengo {edad} años y vivo en {ciudad}.")
presentar_persona(edad=28, ciudad="Madrid", nombre="Carlos")  # Llamada a la función usando keyword arguments

def calcular_area_rectangulo(base, altura):
    """Función que calcula el área de un rectángulo."""
    return base * altura
area = calcular_area_rectangulo(5, 3)  # Llamada a la función para calcular el área
print(f"El área del rectángulo es: {area}")

def convertir_a_mayusculas(texto):
    """Función que convierte un texto a mayúsculas."""
    return texto.upper()
texto_original = "hola mundo"
texto_mayusculas = convertir_a_mayusculas(texto_original)  # Llamada a la función para convertir el texto
print(f"Texto en mayúsculas: {texto_mayusculas}")

def es_primo(numero):
    """Función que verifica si un número es primo."""
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True
numero = 17
if es_primo(numero):
    print(f"El número {numero} es primo.")
else:
    print(f"El número {numero} no es primo.")

def obtener_nombres_longitud(nombres, longitud):
    """Función que devuelve una lista de nombres con una longitud específica."""
    return [nombre for nombre in nombres if len(nombre) == longitud]
nombres = ["Ana", "Luis", "Marta", "Carlos", "Eva"]
nombres_filtrados = obtener_nombres_longitud(nombres, 4)  # Llamada a la función para filtrar nombres
print(f"Nombres con 4 letras: {nombres_filtrados}")

# uso de pass
def funcion_vacia():
    pass  # Función vacía que no hace nada

funcion_vacia()  # Llamada a la función vacía

def calcular_promedio(lista_numeros):
    """Función que calcula el promedio de una lista de números."""
    if len(lista_numeros) == 0:
        return 0
    return sum(lista_numeros) / len(lista_numeros)
numeros = [10, 20, 30, 40, 50]
promedio = calcular_promedio(numeros)  # Llamada a la función para calcular el promedio
print(f"El promedio de la lista es: {promedio}")


#recursion de funciones
def suma_numeros(n):
    """Función recursiva que calcula la suma de los primeros n números naturales."""
    if n == 1:
        return 1
    else:
        return n + suma_numeros(n - 1)
    
def contador(n):
    """Función recursiva que cuenta desde n hasta 1."""
    if n <= 0:
        return
    print(n)
    contador(n - 1)
contador(5)  # Llamada a la función para contar desde 5 hasta 1

# recursión para calcular la suma de una lista
def suma_lista(lista):
    """Función recursiva que calcula la suma de una lista de números."""
    if not lista:
        return 0
    return lista[0] + suma_lista(lista[1:])

numeros = [1, 2, 3, 4, 5]
suma = suma_lista(numeros)  # Llamada a la función para calcular la suma
print(f"La suma de la lista es: {suma}")

def invertir_cadena(cadena):
    """Función que invierte una cadena de texto."""
    return cadena[::-1]
cadena = "hola mundo"
cadena_invertida = invertir_cadena(cadena)  # Llamada a la función para invertir la cadena
print(f"Cadena invertida: {cadena_invertida}")


# Docstrings
def calcular_potencia(base, exponente):
    """Función que calcula la potencia de un número dado una base y un exponente."""
    return base ** exponente
potencia = calcular_potencia(2, 3)  # Llamada a la función para calcular la potencia
print(f"2 elevado a la 3 es: {potencia}")

# Como visualizar el docstring
print(calcular_potencia.__doc__)  # Imprime el docstring de la función calcular_potencia

# o tambien con help
help(calcular_potencia)  # Muestra la ayuda de la función calcular_potencia

#--------------------------------------------------------------------------------------
# Funciones lambda, son funciones pequeñas y anónimas
# se usan para operaciones simples y se definen en una sola línea
# no tienen nombre y se utilizan generalmente como argumentos para otras funciones
# Sintaxis: lambda argumentos: expresión
# Ejemplos:

# Función lambda para sumar dos números
sumar = lambda x, y: x + y
resultado = sumar(3, 5)
print(f"La suma de 3 y 5 es: {resultado}")  

# Función lambda para verificar si un número es par
es_par = lambda x: x % 2 == 0
numero = 8
if es_par(numero):
    print(f"El número {numero} es par.")

# Función lambda para calcular el cuadrado de un número
cuadrado = lambda x: x ** 2
num = 4
print(f"El cuadrado de {num} es: {cuadrado(num)}")

# Función lambda para filtrar números mayores a un valor dado
filtrar_mayores = lambda lista, valor: list(filter(lambda x: x > valor, lista))
numeros = [1, 5, 8, 12, 3, 7]
mayores_a_5 = filtrar_mayores(numeros, 5)
print(f"Números mayores a 5: {mayores_a_5}")

# Como usar lamba de manera correcta

def operaciones(operacion):
    """Función que realiza una operación matemática utilizando una función lambda."""
    if operacion == "suma":
        return lambda x, y: x + y
    elif operacion == "resta":
        return lambda x, y: x - y
    elif operacion == "multiplicacion":
        return lambda x, y: x * y
    elif operacion == "division":
        return lambda x, y: x / y
    else:
        return None

suma_func = operaciones("suma")
if suma_func:
    print(f"La suma de 10 y 5 es: {suma_func(10, 5)}") # Llamada a la función para sumar 10 y 5
resta_func = operaciones("resta")
if resta_func:
    print(f"La resta de 10 y 5 es: {resta_func(10, 5)}") # Llamada a la función para restar 10 y 5
multiplicacion_func = operaciones("multiplicacion")
if multiplicacion_func:
    print(f"La multiplicación de 10 y 5 es: {multiplicacion_func(10, 5)}") # Llamada a la función para multiplicar 10 y 5
division_func = operaciones("division")
if division_func:
    print(f"La división de 10 y 5 es: {division_func(10, 5)}") # Llamada a la función para dividir 10 y 5
else:
    print("Operación no válida.")


# funciones como argumentos, callback functions
# son funciones que se pasan como argumentos a otras funciones
# permiten mayor flexibilidad y reutilización de código
# Ejemplos:

# Función que aplica una operación a dos números

def aplicar_operacion(a, b, operacion):
    """Función que aplica una operación matemática a dos números."""
    return operacion(a, b) # Llamada a la función operacion con los argumentos a y b

# otro ejemplo
def aplicar_funcion(funcion, valor):
    """Función que aplica una función a un valor dado."""
    return funcion(valor)  # Llamada a la función con el valor proporcionado 

def cuadrado(x):
    """Función que calcula el cuadrado de un número."""
    return x ** 2
def cubo(x):
    """Función que calcula el cubo de un número."""
    return x ** 3

print(f"El cuadrado de 4 es: {aplicar_funcion(cuadrado, 4)}")  # Llamada a la función para calcular el cuadrado de 4
print(f"El cubo de 3 es: {aplicar_funcion(cubo, 3)}")          # Llamada a la función para calcular el cubo de 3

#--------------------------------------------------------------------------------------------------------------
# Funciones de orden superior: son aqellas que recibe y devuelven funciones como argumentos
#--------------------------------------------------------------------------------------------------------------

# map, toma una función y un iterable, y aplica la función a cada elemento del iterable


def cuadrado(x):
    return x ** 2

lista_numeros = [1, 2, 3, 4, 5]

numeros_al_cuadrado = list(map(cuadrado, lista_numeros))
print(f"Números al cuadrado: {numeros_al_cuadrado}") # Muestra la lista de números al cuadrado, 
# [1, 4, 9, 16, 25]

#Filter, toma una función y un iterable, y devuelve un nuevo iterable con los elementos que cumplen una condición

def par(x):
    return x % 2 == 0

pares = list(filter(par, lista_numeros))
print(f"Números pares: {pares}") # Muestra la lista de números pares, [2, 4]

#Reduce, toma una función y un iterable, y devuelve un único valor acumulado

def sumar(x, y):
    return x + y

suma_total = reduce(sumar, lista_numeros)
print(f"Suma total: {suma_total}") # Muestra la suma de todos los números en la lista, 15


