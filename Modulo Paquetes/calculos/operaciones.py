# --------------------------------------------------------------
# Modulos y Pauetes
# -------------------------------------------------------------

def sumar(a, b):
    """Suma dos numeros."""
    return a + b

def restar(a, b):
    """Resta dos numeros."""
    return a - b

def multiplicar(a, b):
    """Multiplica dos numeros."""
    return a * b

def dividir(a, b):
    """Divide dos numeros."""
    if b == 0:
        raise ValueError("No se puede dividir por cero.")
    return a / b

