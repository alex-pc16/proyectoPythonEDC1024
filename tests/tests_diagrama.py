import unittest
from io import StringIO
import sys
from src.diagrama import DiagramaAhorcado  # Asegúrate de que el nombre del archivo sea correcto

class TestDiagramaAhorcado(unittest.TestCase):

    def setUp(self):
        """
        Configura una instancia de DiagramaAhorcado para cada prueba.
        """
        self.diagrama = DiagramaAhorcado()

    def test_dibujar_sin_errores(self):
        """
        Prueba que el diagrama sin errores solo muestre el poste del ahorcado.
        """
        salida_esperada = (
            "==========\n"
            "||     |\n"
            "||      \n"
            "||       \n"
            "||       \n"
            "==========\n"
        )
        self._verificar_dibujo(0, salida_esperada)

    def test_dibujar_con_un_error(self):
        """
        Prueba el diagrama con un error, donde solo debe aparecer la cabeza.
        """
        salida_esperada = (
            "==========\n"
            "||     |\n"
            "||     0\n"
            "||       \n"
            "||       \n"
            "==========\n"
        )
        self._verificar_dibujo(1, salida_esperada)

    def test_dibujar_con_dos_errores(self):
        """
        Prueba el diagrama con dos errores, donde deben aparecer la cabeza y el torso.
        """
        salida_esperada = (
            "==========\n"
            "||     |\n"
            "||     0\n"
            "||     | \n"
            "||       \n"
            "==========\n"
        )
        self._verificar_dibujo(2, salida_esperada)

    def test_dibujar_con_cinco_errores(self):
        """
        Prueba el diagrama con cinco errores, donde deben aparecer la cabeza, torso y cuatro extremidades.
        """
        salida_esperada = (
            "==========\n"
            "||     |\n"
            "||     0\n"
            "||    /|\\\n"
            "||    /  \n"
            "==========\n"
        )
        self._verificar_dibujo(5, salida_esperada)

    def test_dibujar_con_seis_errores(self):
        """
        Prueba el diagrama completo con todos los errores.
        """
        salida_esperada = (
            "==========\n"
            "||     |\n"
            "||     0\n"
            "||    /|\\\n"
            "||    / \\\n"
            "==========\n"
        )
        self._verificar_dibujo(6, salida_esperada)

    def _verificar_dibujo(self, errores, salida_esperada):
        """
        Verifica que la salida del dibujo del ahorcado coincida con la esperada.
        
        Args:
            errores (int): Número de errores a probar.
            salida_esperada (str): La salida esperada en formato de cadena.
        """
        # Redirigir la salida estándar para capturar la impresión de `dibujar`
        salida_capturada = StringIO()
        sys.stdout = salida_capturada
        self.diagrama.dibujar(errores)
        sys.stdout = sys.__stdout__  # Restaurar la salida estándar

        # Comprobar que la salida coincida con la esperada
        self.assertEqual(salida_capturada.getvalue(), salida_esperada)

if __name__ == "__main__":
    unittest.main()
