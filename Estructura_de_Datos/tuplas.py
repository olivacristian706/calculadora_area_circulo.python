# ------------------------------------------------------------
# Tuplas en Python - Estructura de Datos
# La tupla es una estructura de datos similar a la lista,
# pero a diferencia de las listas, las tuplas son inmutables.
# ------------------------------------------------------------

# Crear una tupla
mi_tupla = (1, 2, 3, 4, 5)
print("Tupla original:", mi_tupla)  # Salida: (1, 2, 3, 4, 5)

# Acceder a elementos de la tupla
print(mi_tupla[0])  # Salida: 1
print(mi_tupla[-1])  # Salida: 5
print(mi_tupla[1:4])  # Salida: (2, 3, 4)

# Tupla de frutas
tupla_frutas = ("manzana", "banana", "cereza")
print("Tupla de frutas:", tupla_frutas)  # Salida: ('manzana', 'banana', 'cereza')

#elementos en tupla de frutas
if 'manzana' in tupla_frutas:   
    print("La tupla contiene manzana")  # Salida: La tupla contiene manzana

tupla = type(tupla_frutas)
print("Tipo de tupla_frutas:", tupla)  # Salida: <class 'tuple'>

# Tupla con un solo elemento
frutas2 = ("cereza")
print(type(frutas2))  # Salida: <class 'str'>

frutas2 = ("cereza",)
print(type(frutas2))  # Salida: <class 'tuple'>

# Utilizar un constructor de tuplas
otra_tupla = tuple(["pera", "mango", "uva"])
print("Otra tupla de frutas:", otra_tupla)  # Salida: ('pera', 'mango', 'uva')

# Acceder a elementos de la tupla
print("Primer elemento:", tupla_frutas[0])  # Salida: 'manzana'
print("Último elemento:", tupla_frutas[-1])  # Salida: 'cereza'
for fruta in tupla_frutas:
    if 'e' in fruta:
        print("Fruta con 'e':", fruta)  # Salida: Fruta con 'e': cereza 

# Acceder a porciones de la tupla (slicing)
print("Elementos del índice 0 al 1:", tupla_frutas[0:2])  # Salida: ('manzana', 'banana')
print("Elementos desde el índice 1 hasta el final:", tupla_frutas[1:])  # Salida: ('banana', 'cereza')  

# Intentar modificar elementos de la tupla (esto generará un error)
try:
    tupla_frutas[1] = "naranja"
except TypeError as e:
    print("Error al modificar la tupla:", e)  # Salida: Error al modificar la tupla: 'tuple' object does not support item assignment

# Intentar agregar elementos a la tupla (esto generará un error)
try:
    tupla_frutas.append("uva")
except AttributeError as e:
    print("Error al agregar a la tupla:", e)  # Salida: Error al agregar a la tupla: 'tuple' object has no attribute 'append'

# Intentar eliminar elementos de la tupla (esto generará un error)
try:
    tupla_frutas.remove("banana")
except AttributeError as e:
    print("Error al eliminar de la tupla:", e)  # Salida: Error al eliminar de la tupla: 'tuple' object has no attribute 'remove'

# Obtener la longitud de la tupla
print("Longitud de la tupla:", len(tupla_frutas))  # Salida: 3

# Recorrer una tupla con un bucle for
print("Recorrer la tupla:")
for fruta in tupla_frutas:
    print(fruta)

#Recorrer una tupla con el range
print("Recorrer la tupla con range:")
for i in range(len(tupla_frutas)):
    print(tupla_frutas[i], "en índice", i)  # Salida: manzana en índice 0, banana en índice 1, cereza en índice 2

# Frutas con e 
for fruta in tupla_frutas:
    if 'e' in fruta:
        print(f"Fruta con 'e': {fruta}")  # Salida: Fruta con 'e': cereza

# Recorrer una tupla con un bucle while
print("Recorrer la tupla con while:")
i = 0
while i < len(tupla_frutas):
    print(tupla_frutas[i])
    i += 1                               # Salida: manzana, banana, cereza

# Nota: Para modificar una tupla, es necesario crear una nueva tupla
nueva_tupla = tupla_frutas + ("naranja",)
print("Nueva tupla:", nueva_tupla)  # Salida: ('manzana', 'banana', 'cereza', 'naranja')

# Convertir una tupla a lista para modificarla y luego volver a convertirla a tupla
lista_temporal = list(tupla_frutas)
lista_temporal.append("uva")
tupla_modificada = tuple(lista_temporal)
print("Tupla modificada:", tupla_modificada)  # Salida: ('manzana', 'banana', 'cereza', 'uva')

fruta2 = list(tupla_frutas)
fruta2.remove("banana")
tupla_frutas = tuple(fruta2)
print("Tupla después de eliminar banana:", tupla_frutas)  # Salida: ('manzana', 'cereza')

# concatenar tuplas
tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)
tupla_concatenada = tupla1 + tupla2
print("Tupla concatenada:", tupla_concatenada)  # Salida: (1, 2, 3, 4, 5, 6)

# concatenar tuplas con multipliacion de un elemento
tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)    
tupla_concatenada = tupla1 *2 + tupla2
print("Tupla concatenada:", tupla_concatenada)  # Salida: (1, 2, 3, 1, 2, 3, 4, 5, 6)
print(tupla_concatenada.count(3))  # Salida: 2

# repetir tuplas
tupla_repetida = tupla1 * 3
print("Tupla repetida:", tupla_repetida)  # Salida: (1, 2, 3, 1, 2, 3, 1, 2, 3)

# Desempaquetado de tuplas
tupla_desempaquetada = ("rojo", "verde", "azul")
color1, color2, color3 = tupla_desempaquetada
print("Color 1:", color1)  # Salida: 'rojo'
print("Color 2:", color2)  # Salida: 'verde'
print("Color 3:", color3)  # Salida: 'azul'


#Desempaquetado con asterisco
tupla_desempaquetada2 = (1, 2, 3, 4, 5)
a, b, *resto = tupla_desempaquetada2
print("a:", a)  # Salida: 1
print("b:", b)  # Salida: 2
print("Resto:", resto)  # Salida: [3, 4, 5]

# Tuplas anidadas
tupla_anidada = (1, 2, (3, 4), (5, 6))
print("Tupla anidada:", tupla_anidada)  # Salida: (1, 2, (3, 4), (5, 6))
print("Elemento anidado:", tupla_anidada[2])  # Salida: (3, 4)
print("Elemento dentro de la tupla anidada:", tupla_anidada[2][0])  # Salida: 3 

# Contar elementos en una tupla
tupla_contar = (1, 2, 2, 3, 4, 2)
conteo = tupla_contar.count(2)
print("Cantidad de veces que aparece el número 2:", conteo)  # Salida: 3

# Encontrar el índice de un elemento en una tupla
indice = tupla_contar.index(3)
print("Índice del número 3:", indice)  # Salida: 3

# Convertir lista a tupla
lista_a_convertir = ["a", "b", "c"]
tupla_convertida = tuple(lista_a_convertir)
print("Tupla convertida:", tupla_convertida)  # Salida: ('a', 'b', 'c') 

# Convertir tupla a lista
tupla_a_convertir = (1, 2, 3)
lista_convertida = list(tupla_a_convertir)
print("Lista convertida:", lista_convertida)  # Salida: [1, 2, 3]

# Uso de tuplas para retornar múltiples valores desde una función
def coordenadas():
    return (10, 20)
x, y = coordenadas()
print("Coordenadas:", x, y)  # Salida: Coordenadas: 10 20   

# Comparar tuplas
tupla_a = (1, 2, 3)
tupla_b = (1, 2, 4)
print("¿tupla_a es menor que tupla_b?", tupla_a < tupla_b)  # Salida: True

# Iterar con índice usando enumerate
for indice, valor in enumerate(tupla_frutas):
    print(f"Índice: {indice}, Valor: {valor}")
# Salida:
# Índice: 0, Valor: manzana

 