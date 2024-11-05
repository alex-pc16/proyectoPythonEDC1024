from random import choice

class GestorPalabras:
    """
    Clase para gestionar la selección de palabras basadas en diferentes temas.

    Attributes:
        opciones (dict): Un diccionario que contiene temas como claves y listas de palabras como valores.
    """

    def __init__(self, opciones=None):
        """
        Inicializa la clase con un diccionario de opciones que contiene temas y palabras relacionadas.
        """
        self.opciones = opciones or {
            "Música": ["rock", "salsa", "cumbia", "jazz", "clásica", "pop", "reggae"],
            "Deportes": ["fútbol", "baloncesto", "tenis", "natación", "béisbol", "ciclismo", "atletismo"],
            "Colores": ["rojo", "azul", "verde", "amarillo", "naranja", "morado", "negro"],
            "Frutas": ["manzana", "plátano", "uva", "naranja", "pera", "mango", "piña"],
            "Animales": ["perro", "gato", "león", "tigre", "elefante", "caballo", "jirafa"],
            "Países": ["México", "Estados Unidos", "Argentina", "España", "Francia", "Alemania", "Italia"],
            "Comidas": ["pizza", "pasta", "hamburguesa", "ensalada", "sushi", "tacos", "paella"],
            "Profesiones": ["médico", "ingeniero", "profesor", "abogado", "arquitecto", "policía", "bombero"],
            "Tecnología": ["computadora", "teléfono", "tablet", "impresora", "cámara", "robot", "drone"],
            "Vehículos": ["coche", "moto", "bicicleta", "camión", "avión", "barco", "tren"]
        }

    def obtener_temas(self):
        """
        Retorna los temas disponibles para la selección del usuario.

        Returns:
            str: Lista con los temas disponibles.
        """
        temas = list(self.opciones.keys())
        return temas
            
    def seleccionar_palabra(self, tema):
        """
        Selecciona una palabra al azar del tema elegido por el usuario.

        Returns:
            str: Una palabra aleatoria del tema seleccionado.
        """
        return choice(self.opciones[tema])  # Selecciona una palabra al azar de la lista de palabras del tema.

