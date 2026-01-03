# PROYECTO DEL PARCIAL 3: DIVISIBILIDAD
# MATERIA: MATEMÁTICAS DISCRETAS.
# Archivo: numeros.py

# INTEGRANTES DEL EQUIPO:
# - BRANDON ARENAS GUZMÁN.
# - JOHAN ALEJANDRO CABAÑAS BRINGAS.
# - AARON LEON CRUZ.
# - JESUS ANTONIO ROJAS RODRÍGUEZ.
# - AZAEL ALEJANDRO VAZQUEZ SEGURA.

"""
Este módulo contiene la lógica matemática pura del proyecto.
Incluye funciones para el algoritmo de la división, cambio de base,
algoritmo de Euclides (MCD) y resolución de ecuaciones diofánticas lineales.
"""

from typing import Tuple, List, Dict, Any, Union

# DIVISIÓN:

def algoritmo_division(a: int, b: int) -> Tuple[int, int, List[str]]:
    """
    Calcula el cociente y el residuo de la división entera a / b.
    Garantiza que el residuo r cumpla 0 <= r < |b|.
    
    Args:
        a (int): Dividendo.
        b (int): Divisor (debe ser distinto de 0).

    Returns:
        Tuple[int, int, List[str]]: Cociente (q), Residuo (r), Lista de pasos explicativos.

    Raises:
        ValueError: Si b es 0.
    """
    if b == 0:
        raise ValueError("El divisor 'b' no puede ser 0.")
    
    # Manejo de negativos y residuo positivo
    q = a // b
    r = a % b
    
    # En Python el operador % ya retorna el residuo con el mismo signo que el divisor (o cero).
    # Para el algoritmo de la división euclidiana estricta, queremos 0 <= r < |b|.
    # Sin embargo, a // b y a % b en Python ya manejan 'floor division'.
    # Si b > 0: r está en [0, b).
    # Si b < 0: r está en (b, 0].
    # Ajustamos para que r sea siempre no negativo si se requiere definición estricta 0 <= r < |b|.
    
    if r < 0:
        r += abs(b)
        q += 1 if b < 0 else -1 # Ajuste depende del signo, pero mejor recalculamos con la formula
        # Recalculamos q para asegurar a = b*q + r
        q = (a - r) // b

    pasos = [
        f"Dividendo (a) = {a}, Divisor (b) = {b}",
        f"Aplicando algoritmo: {a} = {b}(q) + r",
        f"Cociente (q) = {q}",
        f"Residuo (r) = {r}",
        f"Verificación: {b} * ({q}) + {r} = {b*q} + {r} = {b*q + r}"
    ]
    
    return q, r, pasos

# CAMBIO DE BASE:

def cambio_base(a: int, base: int) -> Tuple[str, str, List[str]]:
    """
    Convierte un número decimal positivo a una base dada (2 <= base <= 16).

    Args:
        a (int): Número decimal positivo.
        base (int): Base destino.

    Returns:
        Tuple[str, str, List[str]]: Representación en la nueva base, Polinomio, Lista de pasos.

    Raises:
        ValueError: Si la base no está entre 2 y 16 o si a < 0.
    """
    if not (2 <= base <= 16):
        raise ValueError("La base debe estar entre 2 y 16.")
    if a < 0:
        raise ValueError("El número debe ser no negativo.")
    
    if a == 0:
        return "0", "0", ["0 = 0"]

    digitos_map = "0123456789ABCDEF"
    residuos = []
    temp_a = a
    pasos = []

    while temp_a > 0:
        q, r = divmod(temp_a, base)
        pasos.append(f"{temp_a} = {base}({q}) + {r}  -> Dígito: {digitos_map[r]}")
        residuos.append(r)
        temp_a = q

    # Construir resultado
    res_str = "".join(digitos_map[r] for r in reversed(residuos))
    
    pol_terms = []
    for i, r in enumerate(residuos):
        if r != 0: # Opcional: mostrar solo términos no nulos
            pol_terms.append(f"{r}({base}^{i})")
    
    polinomio = " + ".join(reversed(pol_terms)) if pol_terms else "0"

    return res_str, polinomio, pasos

# MCD Y EUCLIDES EXTENDIDO:

def euclides_extendido(a: int, b: int) -> Tuple[int, int, int, List[Dict[str, int]], List[str]]:
    """
    Calcula el MCD(a, b) y los coeficientes x, y tales que ax + by = MCD(a, b).
    
    Returns:
        Tuple:
            - mcd (int): Máximo común divisor.
            - x (int): Coeficiente de a.
            - y (int): Coeficiente de b.
            - tabla_pasos (List[Dict]): Pasos del algoritmo de Euclides.
            - reconstruccion (List[str]): Pasos de la sustitución hacia atrás.
    """
    # Trabajamos con positivos para el algoritmo
    a_abs, b_abs = abs(a), abs(b)
    
    r_vals = [a_abs, b_abs]
    q_vals = []
    
    # Algoritmo de Euclides
    while r_vals[-1] != 0:
        q, r = divmod(r_vals[-2], r_vals[-1])
        q_vals.append(q)
        r_vals.append(r)
    
    mcd = r_vals[-2]
    
    # Generar tabla de pasos
    tabla_pasos = []
    # Los residuos relevantes son r_vals[0]...r_vals[-2] (el último es 0)
    # len(q_vals) corresponde a las divisiones
    for i in range(len(q_vals)):
        tabla_pasos.append({
            'a': r_vals[i],
            'b': r_vals[i+1],
            'q': q_vals[i],
            'r': r_vals[i+2]
        })
        
    # Algoritmo extendido iterativo puro para calcular x, y
    x0, x1 = 1, 0
    y0, y1 = 0, 1
    
    # Iteramos solo hasta el penúltimo paso para obtener coeficientes del MCD (último residuo no nulo).
    # El último cociente corresponde a la división exacta que da residuo 0.
    for q in q_vals[:-1]: 
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
        
    # x1 y y1 son los coeficientes para a_abs y b_abs
    # mcd = a_abs * x1 + b_abs * y1
    
    # Ajustamos signos para a y b originales
    signo_a = 1 if a >= 0 else -1
    signo_b = 1 if b >= 0 else -1
    
    x_final = x1 * signo_a
    y_final = y1 * signo_b
    
    # Generación de texto de reconstrucción (solo para fines educativos)
    reconstruccion = []
    if len(tabla_pasos) > 0:
        # Reconstrucción didáctica paso a paso (simplificada)
        for i, paso in enumerate(tabla_pasos):
             reconstruccion.append(f"{paso['r']} = {paso['a']} - {paso['b']}({paso['q']})")

    return mcd, x_final, y_final, tabla_pasos, reconstruccion

# ECUACIONES DIOFÁNTICAS:

def resolver_diofantica(a: int, b: int, c: int) -> Dict[str, Any]:
    """
    Resuelve la ecuación diofántica ax + by = c.

    Returns:
        Dict: Contiene:
            - 'tiene_solucion' (bool)
            - 'mcd' (int)
            - 'x0', 'y0' (int): Solución particular (si existe).
            - 'solucion_general' (str): Cadena descriptiva.
            - 'verificacion' (str): Cadena de verificación.
            - 'pasos_mcd' (List): Pasos de Euclides extendido.
    """
    mcd, x_part, y_part, pasos_mcd, recon = euclides_extendido(a, b)
    
    resultado = {
        'tiene_solucion': False,
        'mcd': mcd,
        'pasos_mcd': pasos_mcd,
        'reconstruccion_mcd': recon,
        'a': a, 'b': b, 'c': c
    }
    
    if c % mcd != 0:
        return resultado
    
    resultado['tiene_solucion'] = True
    
    # Multiplicador para escalar la solución de ax + by = mcd a ax + by = c
    factor = c // mcd
    x0 = x_part * factor
    y0 = y_part * factor
    
    resultado['x0'] = x0
    resultado['y0'] = y0
    
    # Parametros de la solución general
    # x = x0 + (b/d)n
    # y = y0 - (a/d)n
    k_x = b // mcd
    k_y = a // mcd
    
    resultado['solucion_general'] = (
        f"x = {x0} + ({k_x})n\n"
        f"y = {y0} - ({k_y})n\n"
        f"donde n ∈ ℤ"
    )
    
    # Verificación con n=1
    n = 1
    x_ver = x0 + k_x * n
    y_ver = y0 - k_y * n
    
    val_c = a * x_ver + b * y_ver
    
    resultado['verificacion'] = (
        f"Para n=1:\n"
        f"x = {x0} + ({k_x})(1) = {x_ver}\n"
        f"y = {y0} - ({k_y})(1) = {y_ver}\n"
        f"Comprobación: {a}({x_ver}) + {b}({y_ver}) = {a*x_ver} + {b*y_ver} = {val_c} (Igual a c={c})"
    )
    
    return resultado
