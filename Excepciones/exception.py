# Excepciones/exception.py

def division(dividendo, divisor):
    try:
        resultado = dividendo / divisor
    except ZeroDivisionError:
        return "Error: No se puede dividir por cero."
    except TypeError:
        return "Error: Los operandos deben ser números."
    else:
        return resultado
    
# Ejemplos de uso
print(division(10, 2))  # Salida: 5.0
print(division(10, 0))  # Salida: Error: No se puede dividir por cero.
print(division(10, 'a'))  # Salida: Error: Los operandos deben ser números.
