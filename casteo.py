# Variables de Texto
from typing import Type


variable1 = "texto"
variable2 = "123456"
variable3 = "Texto 123456"

# Variables Numericas
variable4 = 100          # Entero
variable5 = 10.5         # Flotante
variable6 = 4j      # Complejo

# Imprimir los tipos de datos
print(variable1)
print(variable2)
print(variable3)
print(variable4)
print(variable5)
print(variable6)

print(type(variable1)) # <class 'str'>
print(type(variable2)) # <class 'str'>
print(type(variable3)) # <class 'str'>
print(type(variable4)) # <class 'int'>
print(type(variable5)) # <class 'float'>
print(type(variable6)) # <class 'complex'>

# Conversiones de Tipos de Datos (Casteo)
# De Texto a Numerico
texto_a_entero = int("123456")          # Convierte cadena a entero
texto_a_flotante = float("10.5")        # Convierte cadena a flot
texto_a_complejo = complex("4j")       # Convierte cadena a complejo
print(type(texto_a_entero))   # <class 'int'>
print(type(texto_a_flotante))  # <class 'float'>
print(type(texto_a_complejo))   # <class 'complex'>
# De Numerico a Texto
entero_a_texto = str(100)          # Convierte entero a cadena
flotante_a_texto = str(10.5)       # Convierte flotante a cadena
complejo_a_texto = str(4j)        # Convierte complejo a cadena
print(type(entero_a_texto))    # <class 'str'>
print(type(flotante_a_texto))  # <class 'str'>
print(type(complejo_a_texto))   # <class 'str'>
# De Entero a Otros Tipos
entero_a_flotante = float(100)        # Convierte entero a flotante
entero_a_complejo = complex(100)      # Convierte entero a complejo
