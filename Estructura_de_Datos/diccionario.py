# ---------------------------------------------------------
# Estructura de Datos: Diccionarios en Python
# Un diccionario es una colección desordenada de pares clave-valor.
# ---------------------------------------------------------

# Crear un diccionario
mi_diccionario = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid"
}
print("Diccionario original:", mi_diccionario)  # Salida: {'nombre': 'Juan', 'edad': 30, 'ciudad': 'Madrid'}

# Acceder a valores mediante claves
print("Nombre:", mi_diccionario["nombre"])  # Salida: Juan

# Agregar un nuevo par clave-valor
mi_diccionario["profesion"] = "Ingeniero"
print("Diccionario después de agregar profesion:", mi_diccionario)  # Salida: {'nombre': 'Juan', 'edad': 30, 'ciudad': 'Madrid', 'profesion': 'Ingeniero'}

# Metodo get para acceder a valores
edad = mi_diccionario.get("edad")  
print("Edad usando get:", edad)  # Salida: Edad usando get: 30

# Modificar un valor existente
mi_diccionario["edad"] = 31
print("Diccionario después de modificar edad:", mi_diccionario)  # Salida: {'nombre': 'Juan', 'edad': 31, 'ciudad': 'Madrid', 'profesion': 'Ingeniero'}

# Eliminar un par clave-valor
del mi_diccionario["ciudad"]
print("Diccionario después de eliminar ciudad:", mi_diccionario)  # Salida: {'nombre': 'Juan', 'edad': 31, 'profesion': 'Ingeniero'}    

# Verificar si una clave existe en el diccionario
if "nombre" in mi_diccionario:
    print("La clave 'nombre' existe en el diccionario.")  # Salida: La clave 'nombre' existe en el diccionario.

# Obtener todas las claves del diccionario
claves = mi_diccionario.keys()
print("Claves del diccionario:", list(claves))  # Salida: ['nombre', 'edad', 'profesion']

# Obtener todos los valores del diccionario
valores = mi_diccionario.values()
print("Valores del diccionario:", list(valores))  # Salida: ['Juan', 31, 'Ingeniero']

# Obtener todos los pares clave-valor del diccionario
pares = mi_diccionario.items()
print("Pares clave-valor del diccionario:", list(pares))  # Salida: [('nombre', 'Juan'), ('edad', 31), ('profesion', 'Ingeniero')]

#Copias de diccionarios
# Copia superficial usando el método copy()
copia_diccionario = mi_diccionario.copy()
print("Copia del diccionario:", copia_diccionario)  # Salida: {'nombre': 'Juan', 'edad': 31, 'profesion': 'Ingeniero'}

# Recorrer el diccionario con un bucle for
print("Recorrer el diccionario:")
for clave, valor in mi_diccionario.items():
    print(f"{clave}: {valor}")
# Salida:
# nombre: Juan
# edad: 31
# profesion: Ingeniero  

# Obtener la longitud del diccionario
print("Longitud del diccionario:", len(mi_diccionario))  # Salida: Longitud del diccionario: 3

# Limpiar el diccionario
mi_diccionario.clear()
print("Diccionario después de limpiar:", mi_diccionario)  # Salida: Diccionario después de limpiar: {}

# Crear un diccionario anidado
diccionario_anidado = {
    "persona1": {
        "nombre": "Ana",
        "edad": 25
    },
    "persona2": {
        "nombre": "Luis",
        "edad": 28
    }
}   
print("Diccionario anidado:", diccionario_anidado)  # Salida: Diccionario anidado: {'persona1': {'nombre': 'Ana
#', 'edad': 25}, 'persona2': {'nombre': 'Luis', 'edad': 28}}

# Acceder a valores en un diccionario anidado
print("Nombre de persona1:", diccionario_anidado["persona1"]["nombre"])  # Salida: Nombre de persona1: Ana
print("Edad de persona2:", diccionario_anidado["persona2"]["edad"])  # Salida: Edad de persona2: 28
# ---------------------------------------------------------

# Recorrer el diccionario anidado
print("Recorrer el diccionario anidado:")
for persona, info in diccionario_anidado.items():
    print(f"{persona}:")
    for clave, valor in info.items():
        print(f"  {clave}: {valor}")    

# Salida:
# persona1:
#   nombre: Ana
#   edad: 25
# persona2:
#   nombre: Luis
#   edad: 28
# Nota: Los diccionarios en Python son mutables, lo que significa que se pueden modificar después de su creación.

# ---------------------------------------------------------

# Ejemplo de uso de diccionarios para contar frecuencias de elementos
elementos = ['manzana', 'banana', 'manzana', 'cereza', 'banana', 'manzana']
frecuencias = {}
for elemento in elementos:
    if elemento in frecuencias:
        frecuencias[elemento] += 1
    else:
        frecuencias[elemento] = 1
print("Frecuencias de elementos:", frecuencias)  # Salida: Frecuencias de elementos: {'manzana': 3, 'banana': 2, 'cereza': 1}
# ---------------------------------------------------------

# Nota: Los diccionarios en Python son mutables, lo que significa que se pueden modificar después de su creación.

# ---------------------------------------------------------
