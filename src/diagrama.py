class Diagrama:
    def dibujar(self, errores):
        raise NotImplementedError("Implementa este método en la subclase")

class DiagramaAhorcado(Diagrama):
    """
    Clase que representa el dibujo del ahorcado en el juego.
    Su propósito es dibujar progresivamente las partes del cuerpo en función de los errores cometidos.
    """
    def __init__(self, cuerpo=None):
        self.cuerpo = cuerpo or ["0","|", "/", "\\", "/", "\\"]

    def dibujar(self, errores):
        """
        Muestra el diagrama del ahorcado en función de los errores cometidos.

        Args:
            errores (int): errores cometidos en el juego
        """
        partes_dibujar = [parte if i < errores else " " for i, parte in enumerate(self.cuerpo)]
        print(f"=" * 10)
        print(f"||{' ':5}|")
        print(f"||{' ':5}{partes_dibujar[0]}")
        print(f"||{' ':4}{partes_dibujar[2]}{partes_dibujar[1]}{partes_dibujar[3]}")
        print(f"||{' ':4}{partes_dibujar[4]} {partes_dibujar[5]}")
        print("=" * 10)
