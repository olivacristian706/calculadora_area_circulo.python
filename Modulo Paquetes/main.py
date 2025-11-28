from calculos import operaciones
from calculos.auxiliares import es_par, es_primo

resultado_suma = operaciones.sumar(5, 3)
resultado_resta = operaciones.restar(5, 3)
resultado_multiplicacion = operaciones.multiplicar(5, 3)
resultado_division = operaciones.dividir(5, 3)

print("Suma: ", resultado_suma)
print("Resta: ", resultado_resta)   
print("Multiplicación: ", resultado_multiplicacion)
print("División: ", resultado_division)

print("¿Es 4 par?: ", es_par(4))
print("¿Es 7 primo?: ", es_primo(7))