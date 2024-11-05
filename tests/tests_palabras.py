import unittest
from src.palabras import GestorPalabras  # Asegúrate de que el nombre del archivo sea correcto
from random import choice

class TestGestorPalabras(unittest.TestCase):

    def setUp(self):
        """
        Configura una instancia de GestorPalabras para cada prueba.
        """
        # Opciones personalizadas para las pruebas
        self.opciones = {
            "Música": ["rock", "salsa"],
            "Deportes": ["fútbol", "tenis"],
            "Colores": ["rojo", "azul"],
        }
        self.gestor = GestorPalabras(opciones=self.opciones)

    def test_obtener_temas(self):
        """
        Prueba que obtener_temas retorne todos los temas en las opciones.
        """
        temas = self.gestor.obtener_temas()
        self.assertEqual(temas, list(self.opciones.keys()), "Los temas obtenidos no coinciden con los esperados")

    def test_seleccionar_palabra(self):
        """
        Prueba que seleccionar_palabra retorne una palabra válida del tema especificado.
        """
        tema = "Música"
        palabra = self.gestor.seleccionar_palabra(tema)
        self.assertIn(palabra, self.opciones[tema], "La palabra seleccionada no pertenece al tema especificado")

    def test_seleccionar_palabra_tema_inexistente(self):
        """
        Prueba que seleccionar_palabra genere un error cuando se pasa un tema inexistente.
        """
        tema = "Inexistente"
        with self.assertRaises(KeyError):
            self.gestor.seleccionar_palabra(tema)

    def test_seleccionar_palabra_sin_opciones(self):
        """
        Prueba que seleccionar_palabra funcione con los valores predeterminados cuando no se pasan opciones.
        """
        gestor_por_defecto = GestorPalabras()  # Sin opciones personalizadas
        temas = gestor_por_defecto.obtener_temas()
        # Verifica que hay temas predeterminados y que se puede seleccionar una palabra de uno de ellos
        self.assertTrue(len(temas) > 0, "No hay temas disponibles en las opciones predeterminadas")
        palabra = gestor_por_defecto.seleccionar_palabra(temas[0])
        self.assertIsInstance(palabra, str, "La palabra seleccionada no es de tipo str")

if __name__ == "__main__":
    unittest.main()
