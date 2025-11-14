# Cadena de Caracteres
# Definicion de Variables de Texto

txt = "Hola, Mundo!"          # Cadena con comillas dobles
txt2 = 'Python es genial'     # Cadena con comillas simples
txt3 = """Este es un texto
multilinea en Python."""      # Cadena con comillas triples dobles

print(type(txt))   # <class 'str'>
print(type(txt2))  # <class 'str'>
print(type(txt3))  # <class 'str'>

# Indices y Slicing
print(txt[0])      # 'H' - Primer caracter
print(txt[-1])     # '!' - Ultimo caracter
print(txt[0:5])    # 'Hola,' - Subcadena desde indice 0 hasta 4
print(txt[7:])     # 'Mundo!' - Subcadena desde indice 7 hasta el final
print(txt[:5])     # 'Hola,' - Subcadena desde el inicio hasta indice 4

# Operaciones con Cadenas

# Busqueda en Cadena
existe = "Mundo" in txt
print(existe)  # True

# Concatenacion
saludo = txt + " " + txt2
print(saludo)  # 'Hola, Mundo! Python es genial'

# Repeticion
eco = txt * 3
print(eco)  # 'Hola, Mundo!Hola, Mundo!Hola, Mundo!'

# Longitud de la Cadena
longitud = len(txt)
print(longitud)  # 13

# Conversion a Mayusculas y Minusculas
mayusculas = txt.upper()
minusculas = txt.lower()
print(mayusculas)  # 'HOLA, MUNDO!'
print(minusculas)  # 'hola, mundo!'

# Busqueda de Subcadena
posicion = txt.find("Mundo")
print(posicion)  # 6

# Reemplazo de Subcadena
nuevo_txt = txt.replace("Mundo", "Python")
print(nuevo_txt)  # 'Hola, Python!'

# Division de Cadena
partes = txt.split(", ")
print(partes)  # ['Hola', 'Mundo!']

# Union de Cadenas
frutas = ["manzana", "banana", "cereza"]
union_frutas = ", ".join(frutas)
print(union_frutas)  # 'manzana, banana, cereza'

# Eliminacion de Espacios en Blanco
txt_espacios = "   Hola, Mundo!   "
txt_sin_espacios = txt_espacios.strip()
print(txt_sin_espacios)  # 'Hola, Mundo!'

# Formateo de Cadenas
nombre = "Juan"
edad = 30
formateado = "Mi nombre es {} y tengo {} años.".format(nombre, edad)
print(formateado)  # 'Mi nombre es Juan y tengo 30 años.'

#usar un palabra desde el texto
txt = "El aprendizaje de Python es divertido"
palabra = txt[3:15]
print(palabra)  # 'aprendizaje'

#contar cuantas veces aparece una letra en el texto
letra = 'e'
contador = txt.count(letra)
print(contador)  # 3

#verificar si una palabra existe en el texto
palabra_buscar = "Python"
existe_palabra = palabra_buscar in txt
print(existe_palabra)  # True

#convertir el texto en una lista de palabras
lista_palabras = txt.split()
print(lista_palabras)  # ['El', 'aprendizaje', 'de', 'Python', 'es', 'divertido']

#unir la lista de palabras en una sola cadena separada por guiones
cadena_unida = '-'.join(lista_palabras)
print(cadena_unida)  # 'El-aprendizaje-de-Python-es-divertido'

#reemplazar una palabra en el texto
nuevo_texto = txt.replace("divertido", "emocionante")
print(nuevo_texto)  # 'El aprendizaje de Python es emocionante'

#convertir el texto a mayusculas
texto_mayusculas = txt.upper()
print(texto_mayusculas)  # 'EL APRENDIZAJE DE PYTHON ES DIVERTIDO'

#convertir el texto a minusculas
texto_minusculas = txt.lower()
print(texto_minusculas)  # 'el aprendizaje de python es divertido'

#eliminar espacios en blanco al inicio y al final del texto
texto_espacios = "   El aprendizaje de Python es divertido   "
texto_sin_espacios = texto_espacios.strip()
print(texto_sin_espacios)  # 'El aprendizaje de Python es divertido'

#formatear una cadena con variables
nombre = "Ana"
edad = 25
formateo = f"Mi nombre es {nombre} y tengo {edad} años."
print(formateo)  # 'Mi nombre es Ana y tengo 25 años.'

#obtener la longitud del texto
longitud_texto = len(txt)
print(longitud_texto)  # 36

#buscar la posicion de una palabra en el texto
posicion_palabra = txt.find("Python")
print(posicion_palabra)  # 15

#contar cuantas palabras hay en el texto
cantidad_palabras = len(txt.split())
print(cantidad_palabras)  # 6

# escape de caracteres especiales
texto_escape = "Ella dijo: \"Python es genial!\"\nNueva linea."
print(texto_escape)
# Ella dijo: "Python es genial!"
# Nueva linea.

# raw string para evitar escape de caracteres
ruta = r"C:\nueva_carpeta\archivo.txt"
print(ruta)  # C:\nueva_carpeta\archivo.txt
# C:\nueva_carpeta\archivo.txt

# salto de linea en cadena
texto_salto = "Primera linea.\nSegunda linea."
print(texto_salto)
# Primera linea.
# Segunda linea.

# tabulacion en cadena
texto_tab = "Columna1\tColumna2\tColumna3"
print(texto_tab)
# Columna1	Columna2	Columna3






