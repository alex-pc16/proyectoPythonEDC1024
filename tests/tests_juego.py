import unittest
from src.juego import Juego, EstadoJuego  # Asegúrate de que el nombre del archivo sea correcto

class TestJuego(unittest.TestCase):

    def setUp(self):
        """
        Configura una instancia del juego con una palabra específica para cada prueba.
        """
        self.juego = Juego("café")

    def test_normalizar_letra(self):
        """
        Prueba que normalizar_letra elimine acentos y conserve la letra ñ.
        """
        self.assertEqual(self.juego.normalizar_letra("café"), "cafe")
        self.assertEqual(self.juego.normalizar_letra("mañana"), "mañana")

    def test_verificar_ganar_letra(self):
        """
        Prueba que verificar_ganar_letra detecte correctamente la victoria al adivinar todas las letras.
        """
        self.juego.letras_adivinadas = set("cafe")
        self.juego.generar_avance()
        self.assertTrue(self.juego.verificar_ganar_letra(), "Debería detectar que todas las letras han sido adivinadas")

    def test_verificar_ganar_palabra_correcta(self):
        """
        Prueba que verificar_ganar_palabra detecte correctamente una palabra completa ingresada correctamente.
        """
        self.assertTrue(self.juego.verificar_ganar_palabra("cafe"), "Debería detectar la palabra completa correctamente")

    def test_verificar_ganar_palabra_incorrecta(self):
        """
        Prueba que verificar_ganar_palabra devuelva False para una palabra incorrecta.
        """
        self.assertFalse(self.juego.verificar_ganar_palabra("cama"), "No debería detectar como correcta una palabra incorrecta")

    def test_jugar_turno_letra_correcta(self):
        """
        Prueba que jugar_turno con una letra correcta actualice el estado del juego correctamente.
        """
        estado, _ = self.juego.jugar_turno("c")
        self.assertEqual(estado, EstadoJuego.SEGUIR_JUGANDO, "Debería continuar el juego")
        self.assertIn("c", self.juego.letras_adivinadas, "La letra correcta debería agregarse a letras_adivinadas")

    def test_jugar_turno_letra_incorrecta(self):
        """
        Prueba que jugar_turno con una letra incorrecta incremente los errores.
        """
        estado, _ = self.juego.jugar_turno("z")
        self.assertEqual(estado, EstadoJuego.LETRA_INCORRECTA, "Debería marcar letra incorrecta")
        self.assertIn("z", self.juego.letras_incorrectas, "La letra incorrecta debería agregarse a letras_incorrectas")
        self.assertEqual(self.juego.errores, 1, "El contador de errores debería incrementarse")

    def test_jugar_turno_palabra_completa_correcta(self):
        """
        Prueba que jugar_turno reconozca una palabra completa ingresada correctamente.
        """
        estado, puntos = self.juego.jugar_turno("cafe")
        self.assertEqual(estado, EstadoJuego.PALABRA_CORRECTA, "Debería detectar la palabra completa correcta")
        self.assertGreater(puntos, 0, "Debería asignar puntos al adivinar la palabra")

    def test_jugar_turno_palabra_completa_fuera_de_tiempo(self):
        """
        Prueba que jugar_turno marque como fuera de tiempo cuando se ingresa una palabra completa en un estado avanzado.
        """
        # Simulamos que solo quedan 2 letras restantes
        self.juego.letras_restantes = 2
        estado, _ = self.juego.jugar_turno("cafe")
        self.assertEqual(estado, EstadoJuego.PALABRA_FUERA_DE_TIEMPO, "Debería marcar como fuera de tiempo")

    def test_calcular_puntos(self):
        """
        Prueba que calcular_puntos retorne una puntuación válida.
        """
        self.juego.letras_adivinadas = set("cafe")
        self.juego.generar_avance()
        puntos = self.juego.calcular_puntos()
        self.assertGreater(puntos, 0, "La puntuación debería ser positiva")

if __name__ == "__main__":
    unittest.main()
