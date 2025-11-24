# ------------------------------------------------------
# Estructura de Datos - Listas
# ------------------------------------------------------

# Crear una lista
mi_lista = [1, 2, 3, 4, 5]
print("Lista original:", mi_lista)  # Salida: [1, 2, 3, 4, 5]

lista = ["manzana", "banana", "cereza"]
print("Lista de frutas:", lista)  # Salida: ['manzana', 'banana', 'cereza']

# Acceder a elementos de la lista
print("Primer elemento:", lista[0])  # Salida: 'manzana'
print("Último elemento:", lista[-1])  # Salida: 'cereza'

#Acceder a porciones de la lista (slicing)
print("Elementos del índice 0 al 1:", lista[0:2])  # Salida: ['manzana', 'banana']
print("Elementos desde el índice 1 hasta el final:", lista[1:])  # Salida: ['banana', 'cereza']

# Modificar elementos de la lista
lista[1] = "naranja"
print("Lista modificada:", lista)  # Salida: ['manzana', 'naranja', 'cereza']

# Agregar elementos a la lista
lista.append("uva")
print("Lista después de append:", lista)  # Salida: ['manzana', 'naranja', 'cereza', 'uva']

lista.insert(1, "kiwi")
print("Lista después de insert:", lista)  # Salida: ['manzana', 'kiwi', 'naranja', 'cereza', 'uva'] 

# Extender la lista con otra lista
otra_lista = ["pera", "mango"]
lista.extend(otra_lista)
print("Lista después de extend:", lista)  # Salida: ['manzana', 'kiwi', 'naranja', 'cereza', 'uva', 'pera', 'mango']

# Eliminar elementos de la lista
lista.remove("naranja")
print("Lista después de remove:", lista)  # Salida: ['manzana', 'kiwi', 'cereza', 'uva']

elemento_eliminado = lista.pop()
print("Elemento eliminado con pop:", elemento_eliminado)  # Salida: 'uva'
print("Lista después de pop:", lista)  # Salida: ['manzana', 'kiwi', 'cereza']

elemento_eliminado_indice = lista.pop(1)
print("Elemento eliminado en índice 1 con pop:", elemento_eliminado_indice)  # Salida: 'kiwi'
print("Lista después de pop en índice 1:", lista)  # Salida: ['manzana', 'cereza']

del lista[1]
print("Lista después de del en índice 1:", lista)  # Salida: ['manzana']

# Obtener la longitud de la lista
print("Longitud de la lista:", len(lista))  # Salida: 3

# Recorrer una lista con un bucle for
print("Recorrer la lista:")
for fruta in lista:
    print(fruta)
# Frutas con e 
for fruta in lista:
    if 'e' in fruta:
        print(f"Fruta con 'e': {fruta}")  # Salida: Fruta con 'e': cereza

fruta_con_e = [fruta for fruta in lista if 'e' in fruta]
print("Frutas con 'e' usando comprensión de listas:", fruta_con_e)  # Salida: ['cereza']

#bucle for con índice usando range
print("Recorrer la lista con índice:")
for i in range(len(lista)):
    print(f"Índice {i}: {lista[i]}") # Salida: Índice 0: manzana, Índice 1: kiwi, Índice 2: cereza

#shorthand for
[print(fruta) for fruta in lista]  # Salida: manzana, kiwi, cereza

#bucle while
print("Recorrer la lista con while:")
i = 0
while i < len(lista):
    print(lista[i])
    i += 1   # Salida: manzana, kiwi, cereza



# Verificar si un elemento está en la lista
print("¿Está 'kiwi' en la lista?", "kiwi" in lista)  # Salida: True
print("¿Está 'banana' en la lista?", "banana" in lista)  # Salida: False

# Ordenar una lista
lista.sort()
print("Lista ordenada:", lista)  # Salida: ['cereza', 'kiwi', 'manzana']

#Ordenar una lista en orden inverso
lista.sort(reverse=True)
print("Lista ordenada en orden inverso:", lista)  # Salida: ['manzana', 'kiwi', 'cereza']

#oedenra una lista sin tener en cuenta mayusculas y minusculas
lista_mixta = ["Banana", "apple", "Cherry"]
lista_mixta.sort(key=str.lower)
print("Lista mixta ordenada sin tener en cuenta mayúsculas y minúsculas:", lista_mixta)  # Salida: ['apple', 'Banana', 'Cherry']

# Invertir una lista
lista.reverse()
print("Lista invertida:", lista)  # Salida: ['manzana', 'kiwi', 'cereza']

# Copiar una lista
copia_lista = lista.copy()
print("Copia de la lista:", copia_lista)  # Salida: ['manzana', 'kiwi', 'cereza']

# Limpiar una lista
copia_lista.clear()
print("Copia de la lista después de clear:", copia_lista)  # Salida: []

# Concatenar listas
otra_lista = ["pera", "mango"]
lista_concatenada = lista + otra_lista
print("Lista concatenada:", lista_concatenada)  # Salida: ['manzana', 'kiwi', 'cereza', 'pera', 'mango']

# Repetir listas
lista_repetida = lista * 2
print("Lista repetida:", lista_repetida)  # Salida: ['manzana', 'kiwi', 'cereza', 'manzana', 'kiwi', 'cereza']

# Encontrar el índice de un elemento
indice_kiwi = lista.index("kiwi")
print("Índice de 'kiwi':", indice_kiwi)  # Salida: 1

# Contar ocurrencias de un elemento
contador_manzana = lista.count("manzana")
print("Número de veces que 'manzana' aparece en la lista:", contador_manzana)  # Salida: 1

# Convertir una cadena en una lista usando split
cadena = "rojo,verde,azul"
lista_colores = cadena.split(",")
print("Lista de colores:", lista_colores)  # Salida: ['rojo', 'verde', 'azul']

# Unir una lista en una cadena usando join
cadena_unida = "-".join(lista_colores)
print("Cadena unida:", cadena_unida)  # Salida: "rojo-verde-azul"

# Listas anidadas
lista_anidada = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Lista anidada:", lista_anidada)  # Salida: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Elemento en la posición [1][2]:", lista_anidada[1][2])  # Salida: 6

# Comprensión de listas
cuadrados = [x**2 for x in range(6)]
print("Lista de cuadrados:", cuadrados)  # Salida: [0, 1, 4, 9, 16, 25]







