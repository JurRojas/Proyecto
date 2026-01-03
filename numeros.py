# PROYECTO DEL PARCIAL 3: DIVISIBILIDAD
# MATERIA: MATEMÁTICAS DISCRETAS.
# Archivo: numeros.py

#INTEGRANTES DEL EQUIPO:
#- BRANDON ARENAS GUZMÁN.
#- JOHAN ALEJANDRO CABAÑAS BRINGAS.
#- AARON LEON CRUZ.
#- JESUS ANTONIO ROJAS RODRÍGUEZ.
#- AZAEL ALEJANDRO VAZQUEZ SEGURA.


"""Este proyecto se divide en tres partes. De ese modo, en esta primera parte nos centraremos en la lógica pura del proyecto."""

# DIVISIÓN:

# Primero definimos la función que recibe el dividendo a y el divisor b.
def algoritmo_division(a, b):
    
    # Ahora verificamos si el divisor es menor o igual a cero.
    if b <= 0:
        
        # Si en dado caso b no es positivo lanza un error, ya que por el terorema del algoritmo de la división b > 0.
        raise ValueError("El divisor 'b' debe ser mayor a 0.")
    
    # Posteriormente, generamos una función que devuelve el cociente (q) y el residuo (r).
    q, r = divmod(a, b)
    
    # Y creamos un caso por si el residuo es negativo que suele suceder cuando 'a' es negativo.
    if r < 0:
        
        # Ajustamos el residuo para que sea positivo.
        r += abs(b)
        
        # Y posteriormente, recalculamos el cociente basado en el nuevo residuo.
        q = (a - r) // b
        
    # Ahora, para mostrar los resultados creamos una cadena de texto multílinea formateando los resultados para que el usuario vea la comprobación:
    # a = b*q + r
    proceso = (
        f">>> RESULTADOS:\n\n"
        f"Cociente (q) = {q}\nResiduo (r) = {r}\n\n"
        f"• Por algoritmo de la división sabemos que q, r son únicos tales que: a = bq + r con 0 <= r < b\n"
        f"• Los datos que tenemos son: a = {a}, b = {b}, q = {q}, r = {r}\n"
        f"• Entonces obtenemos: {a} = {b} x {q} + {r} con 0 <= {r} < {b}\n\n"
        f"Verificación: {a} = {b} x {q} + {r}\n"
        f"              {a} = {b*q} + {r}\n"
        f"              ∴ {a} = {b*q+r}"
    )
    
    # Y finalmente, devolvimos los valores calculados y el texto del procedimiento.
    return q, r, proceso

# CAMBIO DE BASE:

# Con el cambio de base empezamos definiendo la función que recibe el número en base decimal 'a' y la base 'b'.
def cambio_base(a, b):

    # Luego validamos si 'b' estaba en el rango permitido (2 <= b <= 16).
    if not (2 <= b <= 16):

        # Si en dado caso 'b' no cumple con la condición, se lanza un error que especifica que la base no cumple con lo pedido.
        raise ValueError("La base debe estar entre 2 y 16.")

    # Esto es un caso especial, pues si el número es 0 termina rápido.
    if a == 0: return "0", "0", ["0 = 0"]

    # Ahora, creamos un diccionario de caracteres para beses mayores a 10. 
    digitos = "0123456789ABCDEF"

    # Posteriormente, inicializamos listas para guardar los resultados y una copia de 'a' para no modificar la original.
    residuos = []
    temp_a = a
    pasos = []

    # Creamos un bucle que se ejecutara mientras el cociente sea mayor a 0 (para realizar las divisiones sucesivas). 
    while temp_a > 0:

        # En donde dividimos el número actual por la base.
        q, r = divmod(temp_a, b)

        # Guardamos la operación actual en una lista para mostrarla despues. 
        pasos.append(f"{temp_a} = {b}({q}) + {r}  -> Residuo: {digitos[r]}")

        # Y guardamos el residuo.
        residuos.append(r)

        # Ahora, el cociente de esta división se convierte en el dividendo de la siguiente y haci hasta cumplir con la condición ya dicha.
        temp_a = q

    # Para obtener el resultado unimos los residuos en orden inverso (de abajo hacia arriba).
    rep = "".join(digitos[residuos[i]] for i in range(len(residuos)-1, -1, -1))

    # Creamos la cadena que muestra la expanción polinomial.
    polinomio = " + ".join([f"{residuos[i]}({b}^{i})" for i in range(len(residuos)-1, -1, -1)])

    # Y finalmente, devolvimos los resultados.
    return rep, polinomio, pasos

# Para el MCD definimos la función que recibe los números 'a' y 'b'.
def euclides_extendido(a, b):

    # Dentro del MCD 'a' como 'b' siempre tomaran su valor absoluto, asi que, los convertimos a positivos.
    a_abs, b_abs = abs(a), abs(b)

    # Almacenamos los residuos en una lista empezando por los dos números originales.
    r = [a_abs, b_abs]
    q_list = []

    # Empezamos con las operaciones, asi que creamos un bucle que divide hasta que el último residuo agregado sea 0.
    while r[-1] != 0:

        # En esta parte dividimos el penúltimo residuo entre el último.
        q_i, r_i = divmod(r[-2], r[-1])

        # Y guardamos el cociente y el nuevo residuo.
        q_list.append(q_i)
        r.append(r_i)

    # Ahora por el algoritmo de Euclides el MCD es el último residuo antes del 0, asi seleccionamos aquel número.
    mcd = r[-2]
    pasos_div = []

    # Para seguir, creamos una lista de diccionarios con los pasos de las divisiones para la tabla. 
    for i in range(len(q_list)):
        pasos_div.append({'a': r[i], 'b': r[i+1], 'q': q_list[i], 'r': r[i+2]})

    # Y realizamos los prcedimientos para realizar la sustitución hacia atras, creamos una lista vacia donde se guardaran las cadenas de texto que aplican el
    # proceso paso a paso. 
    recon = []

    # Les otorgamos valores iniciales a las varialbles para rastrear los coheficientes.
    x0, x1, y0, y1 = 1, 0, 0, 1

    # Construimos el texto a través de un bucle.
    if len(pasos_div) > 0:
        for i in range(len(pasos_div) - 1):
            curr_r = pasos_div[i]['r']
            curr_a = pasos_div[i]['a']
            curr_b = pasos_div[i]['b']
            curr_q = pasos_div[i]['q']
    # Esta sección recorre las divisiones que se hicieron previamente en el algoritmo de Euclides para generar la explicacion visual.       
            q_val = q_list[i]
            x0, x1 = x1, x0 - q_val * x1
            y0, y1 = y1, y0 - q_val * y1
    # Ahora, en cada paso de la división, los coheficientes se actualizan. Esta fórmula permite expresar cada residuo nuevo como una combinación de los
    # anteriores.
            if i == 0:
                linea = f"{curr_r} = {curr_a} - {curr_q}({curr_b})"
            else:
                linea = f"{curr_r} = {curr_a} - {curr_q}({curr_b}) = ({x1})({a_abs}) + ({y1})({b_abs})"
            
            recon.append(linea)
            
    # Y finalmente calculamos los coheficientes finales. Este bucle es puro, pues este asegura el cálculo exacto de los valores y no el texto como el
    # anterior.
    x_final, x_next, y_final, y_next = 1, 0, 0, 1
    temp_a, temp_b = a_abs, b_abs
    while temp_b != 0:
        q_v = temp_a // temp_b
        temp_a, temp_b = temp_b, temp_a % temp_b
        x_final, x_next = x_next, x_final - q_v * x_next
        y_final, y_next = y_next, y_final - q_v * y_next
        
    # Como trabajamos con valores absolutos, esta parte corrige los signos de x e ypara que la ecuación final sea correcta con los números originales.
    x = x_final * (1 if a >= 0 else -1)
    y = y_final * (1 if b >= 0 else -1)

    # Y finalmente, devolvimos los resultados.    
    return mcd, x, y, pasos_div, recon
