# PROYECTO DEL PARCIAL 3: DIVISIBILIDAD
# MATERIA: MATEMÁTICAS DISCRETAS.
# Archivo: pruebas.py

#INTEGRANTES DEL EQUIPO:
#- BRANDON ARENAS GUZMÁN.
#- JOHAN ALEJANDRO CABAÑAS BRINGAS.
#- AARON LEON CRUZ.
#- JESUS ANTONIO ROJAS RODRÍGUEZ.
#- AZAEL ALEJANDRO VAZQUEZ SEGURA.

"""Esta es la tercera parte. De ese modo, nos centraremos en la parte de comprobación unitaria del proyecto."""

# Importampos el framework unittest para crear y ejecutar pruebas e importamos el módulo numeros que contiene las funciones matemáticas.
import unittest
import numeros

"""Este archivo constituye el módulo de pruebas unitarias. Su función es garantizar la 'corrección matemática' y la 'calidad del código', verificando que
las funciones puras en numeros.py devuelvan resultados exactos antes de ser visualizados en la interfaz de usuario."""


# Definimos una clase de pruebas que hereda de unittest.TestCase. Así pues, todos los métodos que empiezen con test_ se ejecutaran como pruebas individuales. # Importamos el framework unittest para crear y ejecutar pruebas e importamos el módulo numeros que contine las funciones matemáticas a probar.
class TestDivisibilidad(unittest.TestCase):

# Llamamos a la función con valores negativos, desempaquetamos el cociente q, residuo r e ignoramos el texto explicativo con _, usamos assertEqual para
# verificar que q == -3 y r == 1 con mensaje de error personalizado si falla y verificamos manualmente la ecuación fundamental:
# a = b*q + r → -14 = 5*(-3) + 1.
    def test_algoritmo_division(self):
        """Prueba el Teorema de la División con el caso negativo del PDF."""
        # Caso: a = -14, b = 5 => q = -3, r = 1.
        q, r, _ = numeros.algoritmo_division(-14, 5)
        self.assertEqual(q, -3, "El cociente q debe ser -3")
        self.assertEqual(r, 1, "El residuo r debe ser 1 y cumplir 0 <= r < b")
        # Verificación de la igualdad a = bq + r.
        self.assertEqual(5 * (-3) + 1, -14)

# Probamos la conversión de 255 decimal a hexadecimal que debe ser "FF", verificamos la representación final (rep) y verifica que la forma polinómica
# contenga "15(16^1)" porque F = 15.

    def test_cambio_base_hexadecimal(self):
        """Verifica la conversión a base 16 y el uso de símbolos A-F."""
        # Caso: 255 en base 16 es FF.
        rep, pol, _ = numeros.cambio_base(255, 16)
        self.assertEqual(rep, "FF")
        self.assertIn("15(16^1)", pol) # Aqui verificamos la representación polinomial.

# Probamos que la función lance una excepción ValueError cuando la base está fuera del rango permitido (1 o 17 en este caso). Usamos assertRaises para
# capturar y validar la excepción esperada.
    def test_rango_bases_prohibidas(self):
        """Asegura que el programa cumpla la restricción 2 <= b <= 16."""
        with self.assertRaises(ValueError):
            numeros.cambio_base(100, 17)
        with self.assertRaises(ValueError):
            numeros.cambio_base(100, 1)
# Ahora verificamos el valor del MCD, aseguramos que haya al menos un paso en la lista de reconstrucción (recon) y verificamos la combinación lineal:
# 444*x + 370*y == 74.
    def test_mcd_euclides_reconstruccion(self):
        """Valida el MCD y la existencia de pasos de reconstrucción."""
        # Caso: MCD(444, 370) = 74.
        mcd, x, y, divs, recon = numeros.euclides_extendido(444, 370)
        self.assertEqual(mcd, 74)
        self.assertTrue(len(recon) > 0, "Debe existir una secuencia de reconstrucción")
        # Verificamos la combinación lineal: d = ax + by.
        self.assertEqual(444*x + 370*y, 74)
# Para ir cerrando, probamos indirectamente la condición de existencia de soluciones diofánticas, calculamos el MCD de 6 y 9 que debe ser 3 y verificamos que
# 5 % 3 != 0 (condición que indicara que "no hay soluciones enteras").
    def test_ecuacion_diofantica_sin_solucion(self):
        """Verifica que se identifique correctamente cuándo no hay solución."""
        # Caso: 6x + 9y = 5 (MCD es 3, y 3 no divide a 5).
        d, x0, y0, divs, recon = numeros.euclides_extendido(6, 9)
        # Y como sabemos, la lógica de solución (c % d != 0) se prueba validando el MCD.
        self.assertEqual(d, 3)
        self.assertNotEqual(5 % d, 0, "5 no es divisible entre el MCD 3")

if __name__ == "__main__":
    # Finalmente, esto descubre y ejecuta automáticamente todas las pruebas de la clase, mostrando un reporte detallado , y obtendremos un: ok/fail.
    print("Iniciando pruebas unitarias de lógica matemática...")
    unittest.main()
