import csv
from random import choice

class GestorPalabras:
    """
    Clase para gestionar la selección de palabras basadas en diferentes temas, almacenadas en un archivo CSV.

    Attributes:
        archivo_csv (str): La ruta al archivo CSV que contiene los temas y las palabras.
        opciones (dict): Un diccionario que contiene temas como claves y listas de palabras como valores.
    """

    def __init__(self, archivo_csv="temas_palabras.csv"):
        """
        Inicializa la clase con la ruta del archivo CSV y carga las opciones.
        """
        self.archivo_csv = archivo_csv
        self.opciones = self.cargar_palabras()

    def cargar_palabras(self):
        """
        Carga las palabras desde el archivo CSV y las organiza en un diccionario.

        Returns:
            dict: Un diccionario con los temas como claves y listas de palabras como valores.
        """
        opciones = {}
        try:
            with open(self.archivo_csv, mode='r', encoding='utf-8') as archivo:
                lector = csv.reader(archivo)
                for fila in lector:
                    tema, *palabras = fila
                    opciones[tema] = palabras
        except FileNotFoundError:
            print(f"El archivo {self.archivo_csv} no se encontró. Asegúrate de que existe.")
        return opciones

    def guardar_palabras(self):
        """
        Guarda las palabras actuales en el archivo CSV.
        """
        with open(self.archivo_csv, mode='w', encoding='utf-8', newline='') as archivo:
            escritor = csv.writer(archivo)
            for tema, palabras in self.opciones.items():
                escritor.writerow([tema] + palabras)

    def agregar_palabra(self, tema, palabra):
        """
        Agrega una palabra a un tema existente o crea un nuevo tema.

        Args:
            tema (str): El tema al que se quiere agregar la palabra.
            palabra (str): La palabra a agregar.
        """
        if tema in self.opciones:
            self.opciones[tema].append(palabra)
        else:
            self.opciones[tema] = [palabra]
        self.guardar_palabras()

    def obtener_temas(self):
        """
        Retorna los temas disponibles para la selección del usuario.

        Returns:
            list: Lista con los temas disponibles.
        """
        return list(self.opciones.keys())

    def seleccionar_palabra(self, tema):
        """
        Selecciona una palabra al azar del tema elegido por el usuario.

        Args:
            tema (str): El tema del que se seleccionará una palabra.

        Returns:
            str: Una palabra aleatoria del tema seleccionado.
        """
        if tema in self.opciones:
            return choice(self.opciones[tema])
        else:
            raise ValueError(f"El tema '{tema}' no existe. Por favor, elige uno de los temas disponibles.")


