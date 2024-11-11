
# Juego del ahorcado en consola

Este proyecto es un juego interactivo del ahorcado, donde los jugadores intentan adivinar una palabra letra por letra o al arriesgarse a adivinar la palabra completa. El juego se desarrolla en la consola, y se utiliza un sistema de puntos y un diagrama de ahorcado visual que se va completando con cada intento fallido.

## Estructura del proyecto

El proyecto está organizado en varios módulos para facilitar su mantenimiento y expansión:

- **`diagrama.py`**: Contiene la clase `DiagramaAhorcado`, encargada de representar el progreso visual del ahorcado según el número de intentos fallidos.
- **`interfaz.py`**: Incluye la clase `InteraccionConsola`, que gestiona la interacción con el usuario, mostrando el menú, instrucciones, y capturando las entradas del usuario.
- **`juego.py`**: Contiene la lógica principal del juego mediante la clase `Juego` y la enumeración `EstadoJuego`, la cual define los posibles estados (ganador, letra incorrecta, fuera de tiempo, etc.).
- **`palabras.py`**: Define la clase `GestorPalabras`, la cual se encarga de gestionar las palabras disponibles para el juego y agruparlas por temas.

## Funcionalidades Principales

1. **Interacción en Consola**: El usuario interactúa mediante la consola, eligiendo temas, ingresando letras, o intentando adivinar la palabra completa.
2. **Estados del Juego**: El juego maneja varios estados definidos en `EstadoJuego`, como `LETRAS_COMPLETAS`, `LETRA_INCORRECTA`, `PALABRA_CORRECTA`, etc., que controlan el flujo del juego.
3. **Sistema de Puntuación**: Los puntos se calculan en función del número de letras incorrectas, el avance en la palabra y el número de letras restantes.
4. **Normalización de Letras**: Las letras se normalizan para manejar caracteres con acentos y la letra "ñ", de manera que se eviten errores en la comparación.
5. **Dibujo del Ahorcado**: Cada vez que el jugador se equivoca, el diagrama se actualiza visualmente en la consola hasta un máximo de 6 intentos.

## Ejemplo de Uso

```python
from src.interfaz import InteraccionConsola
from src.diagrama import DiagramaAhorcado
from src.palabras import GestorPalabras
from src.juego import Juego, EstadoJuego

if __name__ == "__main__":
    # Inicializa las instancias
    interacciones = InteraccionConsola()
    interacciones.mostrar_instrucciones()
    diagrama_ahorcado = DiagramaAhorcado()
    gestor_palabras = GestorPalabras()
    
    # Selección del tema y palabra
    temas = gestor_palabras.obtener_temas()
    tema = interacciones.seleccionar_tema(temas)
    palabra = gestor_palabras.seleccionar_palabra(tema)
    
    # Inicializa el juego
    juego = Juego(palabra)
    interfaz_ahorcado = ControladorAhorcado(juego, diagrama_ahorcado, interacciones)
    interfaz_ahorcado.jugar()
```

## Requisitos

- **Python 3.x**
- Módulos estándar como `time`, `os`, `platform`, y `unicodedata`.

## Ejecución del Juego

1. **Clonar el repositorio** 
2. Ingresar la carpeta src
2. En la terminal, ejecutar el archivo principal (`interfaz.py`) con el comando:
   ```bash
   python interfaz.py
   ```
3. Seguir las instrucciones en pantalla para seleccionar un tema y comenzar a jugar.


