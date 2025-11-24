# -----------------------------------------------------------------
# Estructura de Datos - Tipos de Datos Secuencia / Coleccion
# -----------------------------------------------------------------

# List - Lista [Colección ordenada y mutable]

lista = [1, 2, 3, 4, 5]
print("Lista:", lista)

# Tuple - Tupla (Colección ordenada e inmutable)

tupla = (1, 2, 3, 4, 5)
print("Tupla:", tupla)

# Range - Rango (Secuencia inmutable de números enteros)

rango = range(1, 6)
print("Rango:", list(rango))

# -----------------------------------------------------------------
# Estructura de Datos - Tipos de Datos de Mapeo - mapping tipes
# -----------------------------------------------------------------

# Dictionary - Diccionario {Colección desordenada, mutable y indexada}
diccionario = {'a': 1, 'b': 2, 'c': 3}
print("Diccionario:", diccionario)

# -----------------------------------------------------------------
# Estructura de Datos - Tipos de Datos de Conjunto - set types  
# -----------------------------------------------------------------

# Set - Conjunto {Colección desordenada, mutable y sin elementos duplicados}
conjunto = {1, 2, 3, 4, 5}
print("Conjunto:", conjunto)

# -----------------------------------------------------------------
# Estructura de Datos - Tipos de Datos Nulo - null types
# -----------------------------------------------------------------

# NoneType - Tipo Nulo (Representa la ausencia de valor)
nulo = None
print("Nulo:", nulo)

# -----------------------------------------------------------------
# Estructura de Datos - STRINGS - strings
# -----------------------------------------------------------------

# String - Cadena de Texto (Secuencia inmutable de caracteres)
cadena = "Hola, Mundo!"
print("Cadena de Texto:", cadena)

comillas_simples = 'Esto es una cadena con comillas simples.'
print("Comillas Simples:", comillas_simples)

comillas_dobles = "Esto es una cadena con comillas dobles."
print("Comillas Dobles:", comillas_dobles)

comillas_triples = """Esto es una cadena 
con comillas triples."""
print("Comillas Triples:", comillas_triples)

cadena_escape = "Línea 1\nLínea 2\tTabulado"
print("Cadena con Caracteres de Escape:\n", cadena_escape)

cadena_raw = r"Ruta de archivo: C:\nueva_carpeta\archivo.txt"
print("Cadena Raw:", cadena_raw)

cadena_concatenada = "Hola, " + "Mundo!"
print("Cadena Concatenada:", cadena_concatenada)

cadena_repetida = "Hola! " * 3
print("Cadena Repetida:", cadena_repetida)

cadena_indexada = "Hola, Mundo!"
print("Primer carácter:", cadena_indexada[0])

cadena_slicing = "Hola, Mundo!"
print("Subcadena (0-4):", cadena_slicing[0:5])

cadena_formateada = "Hola, {}. Tienes {} nuevos mensajes.".format("Usuario", 5)
print("Cadena Formateada:", cadena_formateada)

cadena_fstring = f"Hola, {'Usuario'}. Tienes {5} nuevos mensajes."
print("Cadena Formateada con f-string:", cadena_fstring)

cadena_metodos = "  hola, mundo!  "
print("Cadena Original:", cadena_metodos)
