from palabras import GestorPalabras
from diagrama import DiagramaAhorcado
from juego import Juego
from interfaz import InteraccionConsola, ControladorAhorcado


if __name__=="__main__":
    interacciones = InteraccionConsola()
    interacciones.mostrar_instrucciones()
    diagrama_ahorcado = DiagramaAhorcado([])
    gestor_palabras = GestorPalabras("src/temas_palabras.csv")
    temas = gestor_palabras.obtener_temas()
    tema = interacciones.seleccionar_tema(temas)
    palabra = gestor_palabras.seleccionar_palabra(tema)
    juego = Juego(palabra)
    interfaz_ahorcado = ControladorAhorcado(juego, diagrama_ahorcado, interacciones)
    interfaz_ahorcado.jugar()