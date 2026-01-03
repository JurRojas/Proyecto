# Proyecto de Matemáticas Discretas: Divisibilidad

Este proyecto implementa algoritmos fundamentales de la teoría de números, incluyendo el Algoritmo de la División, Cambio de Base (bases 2 a 16), el Algoritmo de Euclides (MCD) y la resolución de Ecuaciones Diofánticas Lineales.

El sistema está diseñado con una arquitectura modular en Python, separando la lógica matemática (`numeros.py`) de la interfaz gráfica (`interfaz.py`), garantizando precisión matemática y claridad en la visualización de los pasos.

## Características

1.  **Algoritmo de la División**:
    *   Calcula cociente ($q$) y residuo ($r$) tal que $a = bq + r$.
    *   Garantiza $0 \le r < |b|$ incluso para dividendos o divisores negativos.
    *   Muestra la verificación paso a paso.

2.  **Cambio de Base**:
    *   Convierte números enteros decimales a cualquier base entre 2 y 16.
    *   Utiliza división sucesiva y notación extendida (0-9, A-F) para bases > 10.
    *   Muestra el polinomio de potencias de la base.

3.  **Algoritmo de Euclides (MCD)**:
    *   Calcula el Máximo Común Divisor mediante el algoritmo de Euclides.
    *   Calcula la combinación lineal (Identidad de Bézout) usando el algoritmo de Euclides extendido.
    *   Muestra tablas detalladas de cada paso.

4.  **Ecuaciones Diofánticas Lineales**:
    *   Resuelve ecuaciones de la forma $ax + by = c$.
    *   Determina existencia de solución comprobando si $MCD(a,b) | c$.
    *   Ofrece una solución particular ($x_0, y_0$) y la fórmula para la solución general.
    *   Verificación automática de los resultados.

## Requisitos

*   Python 3.x
*   Librería estándar `tkinter` (incluida usualmente con Python).

## Estructura del Proyecto

*   `numeros.py`: **Núcleo Lógico**. Contiene las funciones puras con anotaciones de tipo (`type hints`) y validaciones. No contiene código de interfaz.
*   `interfaz.py`: **Interfaz Gráfica**. Implementación en Tkinter que maneja la entrada de usuario, validación visual y formateo de respuestas.
*   `pruebas.py`: **Pruebas Unitarias**. Suite de pruebas usando `unittest` para verificar casos borde (negativos, cero, bases extremas).

## Ejecución

Para iniciar la aplicación principal:

```bash
python interfaz.py
```

Para ejecutar las pruebas unitarias y verificar la integridad matemática:

```bash
python pruebas.py
```

## Ejemplo de Uso

1.  **División**: Ingrese $a = -14$, $b = 5$. El programa mostrará $q = -3, r = 1$. Verifique que $5(-3) + 1 = -14$.
2.  **Cambio de Base**: Ingrese $255$ base $16$. Resultado: $FF$.
3.  **Diofánticas**: Ingrese $5x + 3y = 10$. El sistema indicará que tiene solución, calculará el MCD(5,3)=1, y mostrará $x = -10 + 3n$, $y = 20 - 5n$ (o equivalente según la solución particular hallada).

---
**Integrantes del Equipo**:
*   Brandon Arenas Guzmán
*   Johan Alejandro Cabañas Bringas
*   Aaron Leon Cruz
*   Jesus Antonio Rojas Rodríguez
*   Azael Alejandro Vazquez Segura
