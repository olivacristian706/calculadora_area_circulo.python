# ----------------------------------------------
# Tipos de Datos en Python
#----------------------------------------------

# Cadenas de texto
cadena = "Hola, Mundo!"  # Tipo str

# Numericos
entero = 10          # Tipo entero
flotante = 10.5     # Tipo flotante
complexo = 3 + 4j       # Tipo complejo
booleano = True      # Tipo booleano

# Secuencias
lista = [1, 2, 3, 4, 5]          # Tipo lista, Coleccion ordenada y mutable
tupla = (1, 2, 3, 4, 5)        # Tipo tupla, coleccion ordenada e inmutable
range_obj = range(0, 10)  # Tipo range, secuencia inmutable de numeros

#Mapeos
diccionario = {
    "clave1": "valor1",
      "clave2": "valor2"
      }  # Tipo diccionario, coleccion de pares clave-valor

# Set types Conjuntos
conjunto = {1, 2, 3, 4, 5}          # Tipo conjunto, coleccion no ordenada y mutable de elementos unicos
conjunto_frozenset = frozenset([1, 2, 3, 4, 5])  # Tipo frozenset, conjunto inmutable

#Booleanos
verdadero = True    # Tipo booleano

#Binarios
bytes_obj = b"Hola"          # Tipo bytes, secuencia inmutable de bytes
bytearray_obj = bytearray(b"Hola")  # Tipo bytearray, secuencia mutable de bytes
memoryview_obj = memoryview(b"Hola")  # Tipo memoryview, vista de memoria

# NoneType
nulo = None  # Tipo NoneType, representa la ausencia de valor   

# Imprimir los tipos de datos
print("Tipo de cadena:", type(cadena))  
print("Tipo de entero:", type(entero))
print("Tipo de flotante:", type(flotante))
print("Tipo de complejo:", type(complexo))
print("Tipo de booleano:", type(booleano))
print("Tipo de lista:", type(lista))
print("Tipo de tupla:", type(tupla))
print("Tipo de range:", type(range_obj))
print("Tipo de diccionario:", type(diccionario))
print("Tipo de conjunto:", type(conjunto))
print("Tipo de frozenset:", type(conjunto_frozenset))
print("Tipo de bytes:", type(bytes_obj))
print("Tipo de bytearray:", type(bytearray_obj))
print("Tipo de memoryview:", type(memoryview_obj))
print("Tipo de NoneType:", type(nulo))



