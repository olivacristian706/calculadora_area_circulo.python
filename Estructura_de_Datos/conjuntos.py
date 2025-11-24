# ----------------------------------------------------
# Estructura de Datos - Conjuntos o Sets en Python
# Un conjunto es una colección desordenada de elementos únicos. 
# ----------------------------------------------------

# Crear un conjunto
mi_conjunto = {1, 2, 3, 4, 5}
print("Conjunto original:", mi_conjunto)  # Salida: {1, 2, 3, 4, 5}

# Conjunto de frutas
conjunto_frutas = {"manzana", "banana", "cereza"}
print("Conjunto de frutas:", conjunto_frutas)  # Salida: {'manzana', 'banana', 'cereza'}

# Verificar si un elemento está en el conjunto
if 'manzana' in conjunto_frutas:   
    print("El conjunto contiene manzana")  # Salida: El conjunto contiene manzana

# Tipo de conjunto
conjunto = type(conjunto_frutas)
print("Tipo de conjunto_frutas:", conjunto)  # Salida: <class 'set'>

# Agregar elementos al conjunto
conjunto_frutas.add("naranja")
print("Conjunto después de add:", conjunto_frutas)  # Salida: {'manzana', 'banana', 'cereza', 'naranja'}

# Intentar agregar un elemento duplicado (no generará error, pero no se añadirá)
conjunto_frutas.add("manzana")
print("Conjunto después de intentar agregar duplicado:", conjunto_frutas)  # Salida: {'manzana', 'banana', 'cereza', 'naranja'}

# Eliminar elementos del conjunto
conjunto_frutas.remove("banana")
print("Conjunto después de remove:", conjunto_frutas)  # Salida: {'manzana', 'cereza', 'naranja'}

elemento_eliminado = conjunto_frutas.pop()
print("Elemento eliminado con pop:", elemento_eliminado)  # Salida: Un elemento eliminado al azar
print("Conjunto después de pop:", conjunto_frutas)  # Salida: Conjunto sin el elemento eliminado 

#Agregar otra tupla con update
otra_tupla = ("pera", "mango")
conjunto_frutas.update(otra_tupla)
print("Conjunto después de update:", conjunto_frutas)  # Salida: Conjunto con las frutas originales más "pera" y "mango"

# Agregar lista con update
otra_lista = ["kiwi", "uva"]
conjunto_frutas.update(otra_lista)
print("Conjunto después de update:", conjunto_frutas)  # Salida: Conjunto con las frutas originales más "kiwi" y "uva"

# Intentar eliminar un elemento que no existe (esto generará un error)
try:
    conjunto_frutas.remove("uva")
except KeyError:
    print("Error: El elemento 'uva' no se encuentra en el conjunto.")  # Salida: Error: El elemento 'uva' no se encuentra en el conjunto.

# Utilizar discard para eliminar un elemento que no existe (no generará error)
conjunto_frutas.discard("uva")
print("Conjunto después de discard:", conjunto_frutas)  # Salida: Conjunto sin cambios, ya que "uva" no estaba presente

# Obtener la longitud del conjunto
print("Longitud del conjunto:", len(conjunto_frutas))  # Salida: Longitud del conjunto: 3

# Recorrer un conjunto con un bucle for
print("Recorrer el conjunto:")
for fruta in conjunto_frutas:
    print(fruta)  # Salida: Frutas en el conjunto (orden no garantizado)


# if en fruta:
    if 'e' in fruta:
        print("Fruta con 'e':", fruta)  # Salida: Fruta con 'e': cereza

# Operaciones de conjuntos
conjunto_a = {1, 2, 3, 4}
conjunto_b = {3, 4, 5, 6}
# Unión
union = conjunto_a.union(conjunto_b)
print("Unión de conjuntos:", union)  # Salida: {1, 2, 3, 4, 5, 6}
# Intersección
interseccion = conjunto_a.intersection(conjunto_b)
print("Intersección de conjuntos:", interseccion)  # Salida: {3, 4}
# Diferencia
diferencia = conjunto_a.difference(conjunto_b)
print("Diferencia de conjuntos:", diferencia)  # Salida: {1, 2}
# Diferencia simétrica
diferencia_simetrica = conjunto_a.symmetric_difference(conjunto_b)
print("Diferencia simétrica de conjuntos:", diferencia_simetrica)  # Salida: {1, 2, 5, 6}

#boolenao true con 1 y false con 0
conjunto_c = {1, 2, 3, True, False, 0}
print(conjunto_c) # Salida: {0, 1, 2, 3} (True se considera igual a 1 y no se duplica y false igual a 0)

# Limpiar un conjunto
conjunto_frutas.clear()

#Union de conjuntos
conjunto1 = {1, 2, 3}
conjunto2 = {4, 5, 6}
union = conjunto1.union(conjunto2)
print("Unión de conjunto1 y conjunto2:", union)  # Salida: {1, 2, 3, 4, 5, 6}

# Unión con el operador |
union_operador = conjunto1 | conjunto2 
print("Unión con operador |:", union_operador)  # Salida: {1, 2, 3, 4, 5, 6}

# Intersección de conjuntos
interseccion = conjunto1.intersection(conjunto2)
print("Intersección de conjunto1 y conjunto2:", interseccion)  # Salida: set() (ya que no hay elementos comunes)

# Intersección con el operador &
interseccion_operador = conjunto1 & conjunto2
print("Intersección con operador &:", interseccion_operador)  # Salida: set() (ya que no hay elementos comunes)

# Diferencia de conjuntos
diferencia = conjunto1.difference(conjunto2)
print("Diferencia de conjunto1 y conjunto2:", diferencia)  # Salida: {1, 2, 3}

# Diferencia con el operador -
diferencia_operador = conjunto1 - conjunto2 
print("Diferencia con operador -:", diferencia_operador)  # Salida: {1, 2, 3}

# Diferencia simétrica de conjuntos
diferencia_simetrica = conjunto1.symmetric_difference(conjunto2)
print("Diferencia simétrica de conjunto1 y conjunto2:", diferencia_simetrica)  # Salida: {1, 2, 3, 4, 5, 6}

# Diferencia simétrica con el operador ^
diferencia_simetrica_operador = conjunto1 ^ conjunto2
print("Diferencia simétrica con operador ^:", diferencia_simetrica_operador)  # Salida: {1, 2, 3, 4, 5, 6}

# Verificar subconjunto y superconjunto
conjunto_a = {1, 2}
conjunto_b = {1, 2, 3, 4, 5}
print("¿conjunto_a es subconjunto de conjunto_b?", conjunto_a.issubset(conjunto_b))  # Salida: True
print("¿conjunto_b es superconjunto de conjunto_a?", conjunto_b.issuperset(conjunto_a))  # Salida: True

# Verificar disjunción
conjunto_c = {6, 7}
print("¿conjunto_a y conjunto_c son disjuntos?", conjunto_a.isdisjoint(conjunto_c))  # Salida: True

# Crear un conjunto inmutable con frozenset
conjunto_inmutable = frozenset([1, 2, 3, 4, 5])
print("Conjunto inmutable (frozenset):", conjunto_inmutable)  # Salida: frozenset({1, 2, 3, 4, 5})