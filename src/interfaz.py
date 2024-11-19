import os
import time
import platform
from juego import EstadoJuego

class InteraccionConsola:
    """Clase para gestionar la interacción del juego del ahorcado en la consola."""

    def mostrar_menu(self, opciones):
        """
        Muestra un menú interactivo de temas disponibles y permite al usuario seleccionar uno.

        Args:
            opciones (list): Lista de temas disponibles.
        """
        separador = "="
        ancho_max = len(max(opciones, key=len))
        print("\nSelecciona un tema para comenzar:\n")
        print(separador * (ancho_max + 16))
        for i, opcion in enumerate(opciones):
            linea_menu = f"{i + 1:<3}.- {opcion}"
            print(f"||{' ' * 4}{linea_menu:{ancho_max + 8}}||")
        print(separador * (ancho_max + 16))

    def seleccionar_tema(self, opciones):
        """
        Captura la selección del usuario para elegir un tema del menú.

        Args:
            opciones (list): Lista de temas disponibles.

        Returns:
            str: El tema seleccionado por el usuario.
        """
        self.mostrar_menu(opciones)
        opciones_numericas = {str(i + 1): opcion for i, opcion in enumerate(opciones)}
        while True:
            opcion_seleccionada = input("Selecciona una opción: ")
            if opcion_seleccionada in opciones_numericas:
                return opciones_numericas[opcion_seleccionada]
            print("Opción no válida. Intenta de nuevo.")

    def mostrar_instrucciones(self):
        """Muestra las instrucciones del juego al usuario."""
        self.limpiar_pantalla()
        instrucciones = """
        ¡Bienvenido al Juego del Ahorcado!

        Instrucciones:
        1. Tu misión es descubrir la palabra secreta antes 
           de que el ahorcado esté completo.
        2. Puedes adivinar la palabra letra por letra o intentar 
           adivinar la palabra completa (siempre que falten más de tres letras por adivinar).
        3. Por cada letra incorrecta, una nueva parte del dibujo 
           del ahorcado aparecerá. ¡Tienes un máximo de 6 intentos!
        4. Si completas el dibujo del ahorcado antes de encontrar 
           todas las letras, habrás perdido.
        5. Al terminar cada partida obtendras una puntuación dependiendo de cuantas letras
           tenga la palabra y cuantos errores hayas tenido.
        6. Si adivinas todas las letras antes de completar el dibujo 
           del ahorcado, ¡serás el ganador!

        ¡Buena suerte, y que comience el desafío!
        """
        print(instrucciones)
        input("Presiona enter para continuar . . .")
        self.limpiar_pantalla()

    def limpiar_pantalla(self):
        """Limpia la pantalla de la consola según el sistema operativo."""
        if platform.system() == "Windows":
            os.system("cls")
        else:
            os.system("clear")


class ControladorAhorcado:
    """Clase controladora para gestionar el flujo del juego del ahorcado."""

    def __init__(self, juego, diagrama, interacciones):
        """
        Inicializa el controlador del juego del ahorcado.

        Args:
            juego (Juego): Instancia del juego.
            diagrama (DiagramaAhorcado): Instancia para dibujar el diagrama del ahorcado.
            interacciones (InteraccionConsola): Instancia para gestionar la interacción en consola.
        """
        self.juego = juego
        self.diagrama = diagrama
        self.interacciones = interacciones

    def mostrar_avance(self):
        """Muestra el estado actual del juego y el progreso del jugador."""
        self.interacciones.limpiar_pantalla()
        self.diagrama.dibujar(self.juego.errores)
        
        
    def jugar(self):
        """Ejecuta el bucle principal del juego, gestionando cada turno."""
        print("¡El juego ha comenzado! Adivina la palabra.")
        while self.juego.errores < self.juego.intentos_max:
            self.mostrar_avance()
            print(f"Progreso: {self.juego.avance}")
            entrada_usuario = input("Ingresa una letra o intenta adivinar la palabra: ")
          
            resultado_turno, puntos = self.juego.jugar_turno(entrada_usuario)        
            if resultado_turno in [EstadoJuego.LETRAS_COMPLETAS, EstadoJuego.PALABRA_CORRECTA]:
                self.mostrar_avance()
                print(f"La palabra es: {' '.join(self.juego.palabra)}")
                print("¡¡¡Felicidades, ganaste!!!")
                print(f"Puntos: {puntos}")
                break
           
            elif resultado_turno == EstadoJuego.PALABRA_FUERA_DE_TIEMPO:
                print("Ya no puedes adivinar la palabra completa. Sigue letra por letra.")
                time.sleep(1)
            
            elif resultado_turno == EstadoJuego.LETRA_INCORRECTA:
                print("Letra incorrecta")
                time.sleep(1)

            elif resultado_turno == EstadoJuego.LETRA_REPETIDA:
                print("Ya usaste esa letra")
                time.sleep(1)
        
        else:
            print("¡¡¡Perdiste!!!")
            print(f"La palabra secreta era: {self.juego.palabra}")



