# PROYECTO DEL PARCIAL 3: DIVISIBILIDAD
# MATERIA: MATEMÁTICAS DISCRETAS.
# Archivo: pruebas.py

# INTEGRANTES DEL EQUIPO:
# - BRANDON ARENAS GUZMÁN.
# - JOHAN ALEJANDRO CABAÑAS BRINGAS.
# - AARON LEON CRUZ.
# - JESUS ANTONIO ROJAS RODRÍGUEZ.
# - AZAEL ALEJANDRO VAZQUEZ SEGURA.

"""
Módulo de Pruebas Unitarias.
Verifica la corrección matemática de las funciones implementadas en numeros.py.
"""

import unittest
import numeros

class TestDivisibilidad(unittest.TestCase):

    # --- PRUEBAS DE DIVISIÓN ---

    def test_algoritmo_division_negativo(self):
        """Prueba a = -14, b = 5 => q = -3, r = 1 (0 <= r < |b|)"""
        q, r, _ = numeros.algoritmo_division(-14, 5)
        self.assertEqual(q, -3)
        self.assertEqual(r, 1)
        # Verificación: a = bq + r
        self.assertEqual(5 * (-3) + 1, -14)

    def test_algoritmo_division_divisor_negativo(self):
        """Prueba a = 20, b = -3.
        Si b < 0, |b| = 3. 0 <= r < 3.
        20 = (-3)(-6) + 2 --> q=-6, r=2.
        """
        q, r, _ = numeros.algoritmo_division(20, -3)
        self.assertEqual(20, -3 * q + r)
        self.assertTrue(0 <= r < abs(-3))

    def test_division_cero_error(self):
        """Debe lanzar ValueError si b = 0"""
        with self.assertRaises(ValueError):
            numeros.algoritmo_division(10, 0)

    # --- PRUEBAS DE CAMBIO DE BASE ---

    def test_cambio_base_hex(self):
        """255 en base 16 es 'FF'"""
        rep, pol, _ = numeros.cambio_base(255, 16)
        self.assertEqual(rep, "FF")
        # Revisamos parte de la cadena polinomial
        self.assertIn("15(16^0)", pol) # F = 15

    def test_cambio_base_binario(self):
        """5 en base 2 es '101'"""
        rep, pol, _ = numeros.cambio_base(5, 2)
        self.assertEqual(rep, "101")

    def test_cambio_base_limites(self):
        """Base 1 y Base 17 deben fallar"""
        with self.assertRaises(ValueError):
            numeros.cambio_base(10, 1)
        with self.assertRaises(ValueError):
            numeros.cambio_base(10, 17)

    # --- PRUEBAS DE MCD Y EUCLIDES ---

    def test_mcd_euclides(self):
        """MCD(444, 370) = 74"""
        mcd, x, y, _, _ = numeros.euclides_extendido(444, 370)
        self.assertEqual(mcd, 74)
        # Identidad de Bezout: 444x + 370y = 74
        self.assertEqual(444 * x + 370 * y, 74)

    def test_mcd_negativos(self):
        """MCD debe ser positivo incluso si inputs son negativos"""
        # MCD(-12, -8) = 4
        mcd, x, y, _, _ = numeros.euclides_extendido(-12, -8)
        self.assertEqual(mcd, 4)
        self.assertEqual(-12 * x + -8 * y, 4)

    # --- PRUEBAS DE ECUACIONES DIOFÁNTICAS ---

    def test_diofantica_con_solucion(self):
        """5x + 3y = 10. MCD(5,3)=1, 1|10 -> Sí hay solución"""
        res = numeros.resolver_diofantica(5, 3, 10)
        self.assertTrue(res['tiene_solucion'])
        self.assertEqual(res['mcd'], 1)
        # Validar solución particular
        x0 = res['x0']
        y0 = res['y0']
        self.assertEqual(5*x0 + 3*y0, 10)

    def test_diofantica_sin_solucion(self):
        """6x + 9y = 5. MCD(6,9)=3. 3 no divide a 5."""
        res = numeros.resolver_diofantica(6, 9, 5)
        self.assertFalse(res['tiene_solucion'])
        self.assertEqual(res['mcd'], 3)

if __name__ == "__main__":
    print("Ejecutando pruebas unitarias...")
    unittest.main()
