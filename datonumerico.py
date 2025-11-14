# --------------------------------------------------------------------------------
# Datos Numericos y Casteo
# --------------------------------------------------------------------------------

# Variables Numericas
x = 42               # Entero
y = 3.14             # Flotante
z = 1 + 2j          # Complejo

print(type(x))  # <class 'int'>
print(type(y))  # <class 'float'>
print(type(z))  # <class 'complex'>

# Casteo de Tipos
# De Entero a Flotante y Complejo   

x_to_float = float(x)        # Convierte entero a flotante
x_to_complex = complex(x)    # Convierte entero a complejo

print(type(x_to_float))   # <class 'float'>
print(type(x_to_complex))  # <class 'complex'>

# De Flotante a Entero y Complejo
y_to_int = int(y)            # Convierte flotante a entero
y_to_complex = complex(y)    # Convierte flotante a complejo

print(type(y_to_int))      # <class 'int'>
print(type(y_to_complex))   # <class 'complex'>


# De Flotante a Entero
flotante_a_entero = int(10.5)      # Convierte flotante
print(type(flotante_a_entero))  # <class 'int'>

# De Complejo a Entero y Flotante
# Nota: No se puede convertir directamente un número complejo a entero o flotante
# Se debe convertir primero a flotante usando la parte real o imaginaria
complejo_a_flotante = float(z.real)  # Convierte la parte real del complejo a flotante
print(type(complejo_a_flotante))  # <class 'float'>
#print(type(entero_a_flotante))   # <class 'float'>
#print(type(entero_a_complejo))   # <class 'complex'>
print(type(complejo_a_flotante))  # <class 'float'>
# De Complejo a Entero (usando la parte real)
complejo_a_entero = int(z.real)      # Convierte la parte real del complejo a entero
print(type(complejo_a_entero))    # <class 'int'>

# --------------------------------------------------------------------------------
# Ejercicio Practico
# --------------------------------------------------------------------------------

import random

X = random.randrange(1, 100)
print(X)
print(type(X))  # <class 'int'>

y = random.random()
print(y)
print(type(y))  # <class 'float'>

x = random.randint(1, 50)
print(x)
print(type(x))  # <class 'int'>

