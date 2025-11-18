# --------------------------------------------------------------------
# Algoritmo para permitir el ingreso si la edad es mayor o igual a 18 años
# --------------------------------------------------------------------

# Paso 1: Solicitar al usuario que ingrese la edad del cliente

edad = int(input("Por favor, ingresa tu edad: "))
    
# Paso2: Verificar si la edad ingresada cumple con el requisito para ingresar a la discoteca

permitido = True if edad >= 18 else False #ternario


# Paso3: Mostrar al usuario si su cliente puede o no ingrasar a la discoteca    

if permitido:
    print("Puedes ingresar a la discoteca!")
else:
    print("Lo sentimos mucho, No puedes ingresar a la discoteca siendo menor de edad")