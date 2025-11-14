# Estructuras de control en Python

# Estructura condicional if, elif, else
edad = 20
if edad < 18:
    print("Eres menor de edad.")
elif edad >= 18 and edad < 65:
    print("Eres adulto.")
else:
    print("Eres adulto mayor.")

# Extructura condicional anidada
nota = 85
if nota >= 90:
    print("Excelente")
elif nota >= 75:
    print("Bueno")
    if nota >= 80:
        print("Puedes mejorar aún más.")
else:
    print("Necesitas mejorar.")

#Estrucura condicional ternaria
es_mayor = True if edad >= 18 else False
print("Es mayor de edad:", es_mayor)

# Estructura de bucle while
contador = 0
while contador < 5:
    print("Contador es:", contador)
    contador += 1   

# Estructura de bucle for
frutas = ["manzana", "banana", "cereza"]
for fruta in frutas:
    print("Fruta:", fruta)

for i in range(3):
    print("Número:", i)

for i in range(2, 10, 2):
    print("Número par:", i)

for i in range(0, 11, 2):
    if i == 2:
        print("paso por el numero 2")
    else:
        print("no paso por el 2, es numero es: ", i)

for i in range(5, 0, -1):
    print("Cuenta regresiva:", i)
    print("¡Despegue!")

# Uso de break y continue en bucles
for numero in range(10):
    if numero == 5:
        print("Se encontró el número 5, saliendo del bucle.")
        break
    if numero % 2 == 0:
        continue
    print("Número impar:", numero)

#Uso de pass
for i in range(5):
    if i == 3:
        pass  # No hacer nada cuando i es 3
    else:
        print("Valor de i:", i) 

# Estructura try-except para manejo de excepciones
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Error: División por cero no permitida.")
finally:
    print("Operación finalizada.")

# Estructura with para manejo de archivos
with open("archivo_ejemplo.txt", "w") as archivo:
    archivo.write("Hola, este es un archivo de ejemplo.")
with open("archivo_ejemplo.txt", "r") as archivo:
    contenido = archivo.read()
    print("Contenido del archivo:", contenido)  
    
#uso de finally
try:
    numero = int(input("Ingresa un número: "))
    resultado = 100 / numero
finally:
    print("Operación finalizada.")

#usar un palabra desde el texto
txt = "Hola, Mundo!"
palabra = "Mundo"
if palabra in txt:
    print(f"La palabra '{palabra}' se encuentra en el texto.")

#contar cuantas veces aparece una letra en el texto
letra = 'o'
contador = txt.count(letra)
print(f"La letra '{letra}' aparece {contador} veces en el texto.")

#verificar si una palabra existe en el texto
palabra_buscar = "Python"
existe_palabra = palabra_buscar in txt
if existe_palabra:
    print(f"La palabra '{palabra_buscar}' existe en el texto.")
else:
    print(f"La palabra '{palabra_buscar}' no existe en el texto.")



