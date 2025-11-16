# --------------------------------------------------------------------
# Algoritmo para contar la cantidad de letras en una palabra o frase
# --------------------------------------------------------------------

import math  

# Paso 1: Solicitar al usuario que ingrese el radio del círculo

radio = float(input("Por favor, ingresa el radio del círculo: "))

# Paso2: Calcular el área del círculo utilizando la fórmula = π * radio^2

area = math.pi * (radio ** 2)

# Paso3: Mostrar al usuario el área calculada

print("El área del círculo con radio", radio, "es:", area)