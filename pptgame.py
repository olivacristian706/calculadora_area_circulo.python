import random


def mostrar_bienvenida():
    """Muestra el mensaje de bienvenida del juego"""
    print("=" * 50)
    print("🎮 PIEDRA, PAPEL O TIJERA 🎮")
    print("=" * 50)
    print("¡Mejor de 3 rondas!")
    print("Opciones: 1=Piedra 🪨 | 2=Papel 📄 | 3=Tijera ✂️")
    print("=" * 50)


def obtener_eleccion_jugador():
    """Solicita y valida la elección del jugador"""
    opciones = {1: "Piedra 🪨", 2: "Papel 📄", 3: "Tijera ✂️"}

    while True:
        try:
            eleccion = int(input("\nTu elección (1-Piedra, 2-Papel, 3-Tijera): "))
            if eleccion in opciones:
                return eleccion, opciones[eleccion]
            else:
                print("❌ Por favor, elige 1, 2 o 3")
        except ValueError:
            print("❌ Por favor, ingresa un número válido")


def obtener_eleccion_computadora():
    """Genera la elección aleatoria de la computadora"""
    opciones = {1: "Piedra 🪨", 2: "Papel 📄", 3: "Tijera ✂️"}
    eleccion = random.randint(1, 3)
    return eleccion, opciones[eleccion]


def determinar_ganador(jugador, computadora):
    """
    Determina el ganador de una ronda
    Retorna: 'jugador', 'computadora' o 'empate'
    """
    # Piedra=1, Papel=2, Tijera=3
    if jugador == computadora:
        return 'empate'
    elif (jugador == 1 and computadora == 3) or \
            (jugador == 2 and computadora == 1) or \
            (jugador == 3 and computadora == 2):
        return 'jugador'
    else:
        return 'computadora'


def mostrar_resultado_ronda(ronda, jugador_texto, comp_texto, ganador):
    """Muestra el resultado de una ronda específica"""
    print(f"\n{'─' * 50}")
    print(f"RONDA {ronda}")
    print(f"{'─' * 50}")
    print(f"Tú elegiste: {jugador_texto}")
    print(f"Computadora eligió: {comp_texto}")

    if ganador == 'empate':
        print("⚖️  ¡EMPATE!")
    elif ganador == 'jugador':
        print("🎉 ¡GANASTE esta ronda!")
    else:
        print("💻 La computadora ganó esta ronda")


def mostrar_marcador(puntos_jugador, puntos_comp, ronda):
    """Muestra el marcador actual"""
    print(f"\n📊 MARCADOR después de {ronda} ronda(s):")
    print(f"   Tú: {puntos_jugador} | Computadora: {puntos_comp}")


def mostrar_resultado_final(puntos_jugador, puntos_comp):
    """Muestra el resultado final del juego"""
    print("\n" + "=" * 50)
    print("🏆 RESULTADO FINAL 🏆")
    print("=" * 50)
    print(f"Puntaje Final - Tú: {puntos_jugador} | Computadora: {puntos_comp}")

    if puntos_jugador > puntos_comp:
        print("🎊 ¡FELICITACIONES! ¡GANASTE EL JUEGO! 🎊")
    elif puntos_comp > puntos_jugador:
        print("😔 La computadora ganó el juego. ¡Inténtalo de nuevo!")
    else:
        print("🤝 ¡Es un EMPATE total!")
    print("=" * 50)


def jugar():
    """Función principal del juego"""
    mostrar_bienvenida()

    puntos_jugador = 0
    puntos_computadora = 0
    total_rondas = 3

    for ronda in range(1, total_rondas + 1):
        # Obtener elecciones
        jugador_num, jugador_texto = obtener_eleccion_jugador()
        comp_num, comp_texto = obtener_eleccion_computadora()

        # Determinar ganador de la ronda
        ganador = determinar_ganador(jugador_num, comp_num)

        # Actualizar puntos
        if ganador == 'jugador':
            puntos_jugador += 1
        elif ganador == 'computadora':
            puntos_computadora += 1

        # Mostrar resultados
        mostrar_resultado_ronda(ronda, jugador_texto, comp_texto, ganador)
        mostrar_marcador(puntos_jugador, puntos_computadora, ronda)

        # Verificar si alguien ya ganó (mejor de 3 = primero en ganar 2)
        if puntos_jugador == 3 or puntos_computadora == 3:
            print("\n🎯 ¡Alguien alcanzó 2 victorias! Fin del juego.")
            break

    # Mostrar resultado final
    mostrar_resultado_final(puntos_jugador, puntos_computadora)

    # Preguntar si quiere jugar de nuevo
    jugar_de_nuevo = input("\n¿Quieres jugar otra vez? (s/n): ").lower()
    if jugar_de_nuevo == 's':
        print("\n" * 2)
        jugar()
    else:
        print("\n👋 ¡Gracias por jugar! ¡Hasta pronto!")


# Iniciar el juego
if __name__ == "__main__":
    jugar()