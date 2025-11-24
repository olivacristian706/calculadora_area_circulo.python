# ----------------------------------------------------------
# Strings Methods Examples
# ----------------------------------------------------------

texto = "hola mundo!"

#Capitalize: Convierte el primer carácter en mayúscula y el resto en minúscula
print(texto.capitalize())  # Salida: "Hola mundo!"

#Upper: Convierte todos los caracteres en mayúscula
print(texto.upper())  # Salida: "HOLA MUNDO!"

#Lower: Convierte todos los caracteres en minúscula
print(texto.lower())  # Salida: "hola mundo!"

#strip: Elimina los espacios en blanco al inicio y al final de la cadena
texto_con_espacios = "   hola mundo!   "
print(texto_con_espacios.strip())  # Salida: "hola mundo!"

#Replace: Reemplaza una subcadena por otra
print(texto.replace("mundo", "Python"))  # Salida: "hola Python!"

#Split: Divide la cadena en una lista de subcadenas basadas en un separador
print(texto.split(" "))  # Salida: ['hola', 'mundo!']

#Join: Une una lista de cadenas en una sola cadena con un separador
palabras = ['hola', 'mundo!']
print(" ".join(palabras))  # Salida: "hola mundo!"

#Find: Busca una subcadena y devuelve el índice de la primera aparición
print(texto.find("mundo"))  # Salida: 5

#rfind: Busca una subcadena desde el final y devuelve el índice de la última aparición
print(texto.rfind("o"))  # Salida: 8

#Index: Busca una subcadena y devuelve el índice de la primera aparición (lanza un error si no se encuentra)
print(texto.index("mundo"))  # Salida: 5

#Count: Cuenta cuántas veces aparece una subcadena en la cadena
print(texto.count("o"))  # Salida: 2

#Startswith: Verifica si la cadena comienza con una subcadena específica
print(texto.startswith("hola"))  # Salida: True

#Endswith: Verifica si la cadena termina con una subcadena específica
print(texto.endswith("mundo!"))  # Salida: True

#Isalpha: Verifica si todos los caracteres en la cadena son alfabéticos
print("hola".isalpha())  # Salida: True

#Isdigit: Verifica si todos los caracteres en la cadena son dígitos
print("12345".isdigit())  # Salida: True

#Isalnum: Verifica si todos los caracteres en la cadena son alfanuméricos
print("hola123".isalnum())  # Salida: True

#Isspace: Verifica si la cadena contiene solo espacios en blanco
print("   ".isspace())  # Salida: True

#Length: Devuelve la longitud de la cadena
print(len(texto))  # Salida: 11

# Format: Formatea la cadena con valores específicos
nombre = "Juan"
edad = 30
print("Mi nombre es {} y tengo {} años.".format(nombre, edad))  # Salida: "Mi nombre es Juan y tengo 30 años."

# F-Strings: Formatea la cadena usando f-strings (Python 3.6+)
print(f"Mi nombre es {nombre} y tengo {edad} años.")  # Salida: "Mi nombre es Juan y tengo 30 años."

# Replace with f-strings: Formatea la cadena usando f-strings (Python 3.6+)
print(f"Mi nombre es {nombre} y tengo {edad} años.")  # Salida: "Mi nombre es Juan y tengo 30 años."

# Title: Convierte el primer carácter de cada palabra en mayúscula
print(texto.title())  # Salida: "Hola Mundo!"

# Zfill: Rellena la cadena con ceros a la izquierda hasta alcanzar una longitud específica
numero = "42"
print(numero.zfill(5))  # Salida: "00042"

# Center: Centra la cadena en un campo de ancho específico, rellenando con espacios
print(texto.center(20))  # Salida: "     hola mundo!     "

# Ljust: Alinea la cadena a la izquierda en un campo de ancho específico, rellenando con espacios
print(texto.ljust(20))  # Salida: "hola mundo!         "

# Rjust: Alinea la cadena a la derecha en un campo de ancho específico, rellenando con espacios
print(texto.rjust(20))  # Salida: "         hola mundo!"

# Swapcase: Invierte mayúsculas y minúsculas en la cadena
print(texto.swapcase())  # Salida: "HOLA MUNDO!"

# Partition: Divide la cadena en tres partes basadas en el primer separador encontrado
print(texto.partition(" "))  # Salida: ('hola', ' ', 'mundo!')







