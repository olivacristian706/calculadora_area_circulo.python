# ----------------------------------------------------------------------------
# Practica Final: Conversion de Moneda
# ----------------------------------------------------------------------------

# Paso 1: Definir el valor actual de Euro y del Dolar respecto al Peso Mexicano

tipo_cambio_eur_a_mxn=23.70
tipo_cambio_usd_a_mxn=20.75
    
# Paso2: Solicitar al usuario el tipo de conversion (Euro a Mex o Dolar a Mex)
    
tipo_conversion = input("Ingrese la moneda origen para la conversion (EUR/USD): ").strip().upper()

# Paso3: Solicitar al usuario el monto a convertir

monto_a_convertir = float(input("Ingrese el monto a convertir: "))

# Paso4: Realizar la conversion utilizando el tipo de cambio correspondiente
# Paso5: Mostar el resultado de la conversion al usuario

if tipo_conversion == "EUR":
    resultado = monto_a_convertir * tipo_cambio_eur_a_mxn
    print("El resultado de la conersion de EUR a MXN es: ", resultado)
elif tipo_conversion == "USD":
    resultado = monto_a_convertir * tipo_cambio_usd_a_mxn
    print("El resultado de la conersion de USD a MXN es: ", resultado)
else:
    print("Moneda no soportada. Por favor ingrese EUR o USD.")