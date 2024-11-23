import unicodedata
from palabras import GestorPalabras
from enum import Enum

class EstadoJuego(Enum):
    """
    Enum para representar los distintos estados 
    posibles despues de un turno del juego.
    """
    LETRA_REPETIDA = "Letra repetida"
    # Se ingresa una letra correcta pero aún no se completa la palabra
    SEGUIR_JUGANDO = "Seguir jugando"
    LETRA_INCORRECTA = "Letra incorrecta"
    # Se ingresa una letra y con ella se completa la palabra
    LETRAS_COMPLETAS = "Letras completas"
    # Se ingresa toda la palabra completa y es correcta
    PALABRA_CORRECTA = "Palabra correcta"
    PALABRA_FUERA_DE_TIEMPO = "Palabra fuera de tiempo ya no puedes adivinar la palabra completa"


print(EstadoJuego.LETRA_INCORRECTA.value)
class Juego:
    """Clase que representa el juego de adivinanza de palabras."""
    
    def __init__(self, palabra):
        """
        Inicializa el juego con la palabra a adivinar.

        Args:
            palabra (str): La palabra que el jugador intentará adivinar.
        """
        self.palabra = palabra
        self.palabra_normalizada = self.normalizar_letra(self.palabra)
        self.errores = 0
        self.letras_usadas = set()
        self.letras_incorrectas = set()
        self.letras_adivinadas = set()
        self.avance = "_ " * len(self.palabra)
        letras_unicas = set(self.normalizar_letra(self.palabra))
        self.letras_restantes = len(letras_unicas) - len(self.letras_adivinadas)
        self.puntos = 0
        self.intentos_max = 6
        

    def normalizar_letra(self, letra):
        """
        Normaliza una letra o palabra eliminando acentos y convirtiendo a minúsculas,
        preservando la letra 'ñ'.

        Args:
            letra (str): La letra o palabra a normalizar.
        
        Returns:
            str: La letra o palabra normalizada.
        """
        # Convertir a minúsculas
        letra = letra.lower()

        # Reemplazar "ñ" con un marcador temporal antes de normalizar
        letra = letra.replace("ñ", "__TEMP_N__")

        # Descomponer caracteres y eliminar marcas de acento
        letra = ''.join(
            c for c in unicodedata.normalize('NFD', letra)
            if unicodedata.category(c) != 'Mn'
        )

        # Restaurar "ñ" desde el marcador
        return letra.replace("__TEMP_N__", "ñ")


    def verificar_ganar_letra(self):
        """
        Verifica si el jugador ha completado todas las letras de la palabra.
        
        Returns:
            bool: True si todas las letras han sido adivinadas, False en caso contrario.
        """
        return "_" not in self.avance
    
    def verificar_ganar_palabra(self, entrada_usuario):
        """
        Verifica si el jugador ha adivinado la palabra completa correctamente.

        Args:
            entrada_usuario (str): La palabra ingresada por el jugador.
        
        Returns:
            bool: True si la palabra es correcta, False en caso contrario.
        """
        return (len(entrada_usuario) > 1 
                and entrada_usuario == self.palabra_normalizada)
    
    def generar_avance(self):
        """
        Actualiza el progreso del jugador cambiando los 
        guiones por las letras adivinadas correctamente.
        """
        self.avance = " ".join([letra if self.normalizar_letra(letra) in 
                                self.letras_adivinadas else "_"
                                for letra in self.palabra])
        
        letras_unicas = set(self.normalizar_letra(self.palabra))
        self.letras_restantes = len(letras_unicas) - len(self.letras_adivinadas)
       
    def calcular_puntos(self):
        """Calcula la puntuación al terminar el juego
        Returns:
            int: Puntuación considerando letras restantes y 
                 cantidad de errores
        """

        puntos = (200 + (self.letras_restantes) * 20 
                      - len(self.letras_incorrectas) * 5)

        return puntos

    def jugar_turno(self, entrada_usuario):
        """
        Procesa el turno del jugador con la entrada dada y actualiza el estado del juego.

        Args:
            entrada_usuario (str): La letra o palabra ingresada por el jugador.
        
        Returns:
            EstadoJuego: El estado actual del juego después de la entrada del jugador.
            int: La puntuación obtenida en el turno actual.
        """
        
        entrada_normal = self.normalizar_letra(entrada_usuario)
        
        # Verificar si la letra ya fue usada
        if entrada_normal in self.letras_usadas:
            return EstadoJuego.LETRA_REPETIDA, 0
            
        # Agregar la entrada a las letras usadas
        self.letras_usadas.add(entrada_normal)
        
        # Verificar si es una letra incorrecta
        if len(entrada_normal) == 1 and entrada_normal not in self.palabra_normalizada:
            self.letras_incorrectas.add(entrada_normal)
            self.errores += 1
            
            return EstadoJuego.LETRA_INCORRECTA, 0

        # Verificar si aun es valido el intento de palabra completa 
        if len(entrada_normal) > 1 and self.letras_restantes < 3:
            return EstadoJuego.PALABRA_FUERA_DE_TIEMPO, 0

        # Verificar si la palabra completa es correcta
        if self.verificar_ganar_palabra(entrada_normal):
            return EstadoJuego.PALABRA_CORRECTA, self.calcular_puntos()
        
        self.letras_adivinadas.add(entrada_normal)
        self.generar_avance()
       
        # Verificar si se completaron todas las letras
        if self.verificar_ganar_letra():
            return EstadoJuego.LETRAS_COMPLETAS, self.calcular_puntos() 

        return EstadoJuego.SEGUIR_JUGANDO, 0

