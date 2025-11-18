# Paso 1: Solicitar al usuarion la medida de la pieza en cms 

medida_en_cms = float(input("Por favor, ingresar la medida de la pieza del mueble en (cms): "))

# Paso2: Convertir las medidas de centimetros a pulgadas

medida_en_pulgadas = medida_en_cms / 2.54

# Paso3: Mostrar las medidas convertidas en pulgadas al usuario

print("La medida en pulgadas de la pieza ingresada es: ", medida_en_pulgadas)

