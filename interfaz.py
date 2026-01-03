# PROYECTO DEL PARCIAL 3: DIVISIBILIDAD
# MATERIA: MATEMÁTICAS DISCRETAS.
# Archivo: interfaz.py

#INTEGRANTES DEL EQUIPO:
#- BRANDON ARENAS GUZMÁN.
#- JOHAN ALEJANDRO CABAÑAS BRINGAS.
#- AARON LEON CRUZ.
#- JESUS ANTONIO ROJAS RODRÍGUEZ.
#- AZAEL ALEJANDRO VAZQUEZ SEGURA.

"""Esta es la segunda parte. De ese modo, nos centraremos en la parte gráfica del proyecto."""

# Importamos inicialmente el módulo tkinter renombrado como tk para crear la interfaz gráfica. Importamos especificamente tkk (widgest modernos) y
# messagebox para mostrar errores. Y de manera muy importante, importamos el módulo local numeros que contiene las funciones matemáticas.   
import tkinter as tk
from tkinter import ttk, messagebox
import numeros

# Definimos la clase principal App que hereda de tk.Tk.
class App(tk.Tk):
    
# Ahora agregamos nombre a la ventana, definimos el tamaño inicial y cambiamos el color de fondo de la ventana principal.
    def __init__(self):
        super().__init__()
        self.title("Proyecto Parcial 3 - Divisibilidad")
        self.geometry("1100x850")
        self.configure(bg="#F5F5F7") 

# Creamos un objeto de estilo para personalizar los widgets ttk. Además, usamos el tema 'clam' que es más personalizable). Configuramos el fondo del
# Notebook (pestañas). Configuramos el estilo de las pestañas: fuente, padding, color de fondo y cambiamos el color cuando una pestaña está seleccionada
# (blanco y texto azul).

        style = ttk.Style()
        style.theme_use('clam')
        
        style.configure("TNotebook", background="#F5F5F7", borderwidth=0)
        style.configure("TNotebook.Tab", 
                        font=("Times New Roman", 13, "bold"), 
                        padding=[20, 10], 
                        background="#E1E1E1")
        style.map("TNotebook.Tab", 
                  background=[("selected", "#FFFFFF")], 
                  foreground=[("selected", "#2979FF")])

# Creamos un diccionario para guardar referencias a las áreas principales y laterales de cada pestaña.
        self.nb = ttk.Notebook(self)
        self.tabs = {}

# Pasamos a definir el nombre de las pestañas.        
        nombres_pestañas = ["División", "Cambio de base", "MCD", "Diofánticas"]
        for t in nombres_pestañas:
            f = tk.Frame(self.nb, bg="white")
            self.nb.add(f, text=t)

# Dentro de cada pestaña creamos un panel lateral izquierdo para los ejemplos, un separador vertical gris y el área principal derecha donde irán los
# inputs y resultados, la personalidad de la interfaz en si.            
            side = tk.Frame(f, width=240, bg="#F8F9FA", bd=0)
            side.pack(side="left", fill="y", padx=2, pady=2)
            
            tk.Frame(f, width=1, bg="#E0E0E0").pack(side="left", fill="y")
            
            main = tk.Frame(f, bg="white")
            main.pack(side="right", expand=True, fill="both", padx=20, pady=20)
            
            tk.Label(side, text="EJEMPLOS", font=("Arial", 10, "bold"), 
                     bg="#F8F9FA", fg="#757575").pack(pady=(20, 10))
            
            self.tabs[t] = (main, side)

        self.nb.pack(expand=True, fill="both", padx=10, pady=10)
        self.setup_ui()

# Creamos un método auxiliar para crear botones de ejemplo. 
    def crear_boton_ejemplo(self, p_side, texto, comando):
        btn = tk.Button(p_side, text=texto, command=comando,
                        font=("Arial", 9), bg="#FFFFFF", fg="#424242",
                        relief="flat", overrelief="groove", cursor="hand2",
                        activebackground="#2979FF", activeforeground="white",
                        padx=10, pady=8)
        btn.pack(fill="x", padx=15, pady=5)

# Y posteriormente, el método principal de construye la interfaz de cada pestaña.
    def setup_ui(self):

# EJEMPLOS:

# En general, añadimos los botones de ejemplo que rellenan automáticamente los campos con valores prededinidos, creamos el título de la sección, dos campos
# de entrada usando el método auxiliar, un botón grande para ejecutar el cálculo y el área de texto para mostrar el resultado detallado por cada
# pestaña.
        m, s = self.tabs["División"]
        self.crear_boton_ejemplo(s, "Caso Negativo: -14, 5", lambda: self.fill_div(-14, 5))
        self.crear_boton_ejemplo(s, "Caso Estándar: 20, 3", lambda: self.fill_div(20, 3))

        self.lbl_t1 = tk.Label(m, text="Algoritmo de la división", font=("Arial", 18, "bold"), bg="white", fg="#212121").pack(pady=10)
        self.ent_div_a = self.crear_input(m, "Dividendo (a):")
        self.ent_div_b = self.crear_input(m, "Divisor (b > 0):")
        tk.Button(m, text="CALCULAR", command=self.run_div, bg="#2979FF", fg="white", font=("Arial", 10, "bold"), padx=20, pady=10, relief="flat").pack(pady=20)
        self.txt_div = self.crear_output(m)

        m, s = self.tabs["Cambio de base"]
        self.crear_boton_ejemplo(s, "255 a Hex (16)", lambda: self.fill_base(255, 16))
        self.crear_boton_ejemplo(s, "100 a Binario (2)", lambda: self.fill_base(100, 2))
        
        tk.Label(m, text="Cambio de base", font=("Arial", 18, "bold"), bg="white").pack(pady=10)
        self.ent_bas_a = self.crear_input(m, "Número dec (a > 0):")
        self.ent_bas_b = self.crear_input(m, "Base (2 <= b <= 16):")
        tk.Button(m, text="CONVERTIR", command=self.run_base, bg="#00C853", fg="white", font=("Arial", 10, "bold"), padx=20, pady=10, relief="flat").pack(pady=20)
        self.txt_base = self.crear_output(m)

        m, s = self.tabs["MCD"]
        self.crear_boton_ejemplo(s, "MCD de 444 y 370", lambda: self.fill_mcd(444, 370))
        self.crear_boton_ejemplo(s, "MCD de 120 y 45", lambda: self.fill_mcd(120, 45))
        
        tk.Label(m, text="Máximo común divisor (MCD) - Algoritmo de Euclides y Combinación lineal", font=("Arial", 18, "bold"), bg="white").pack(pady=10)
        self.ent_mcd_a = self.crear_input(m, "1er número (a ≠ 0):")
        self.ent_mcd_b = self.crear_input(m, "2do número (b ≠ 0):")
        tk.Button(m, text="CALCULAR MCD", command=self.run_mcd, bg="#6200EA", fg="white", font=("Arial", 10, "bold"), padx=20, pady=10, relief="flat").pack(pady=20)
        self.txt_mcd = self.crear_output(m)

        m, s = self.tabs["Diofánticas"]
        self.crear_boton_ejemplo(s, "Ecuación: 5x + 3y = 10", lambda: self.fill_dio(5, 3, 10))
        self.crear_boton_ejemplo(s, "Ecuación: 140x + 370y = 74", lambda: self.fill_dio(140, 370, 74))
        
        tk.Label(m, text="Ecuaciones diofánticas lineales", font=("Arial", 18, "bold"), bg="white").pack(pady=10)
        self.ent_da = self.crear_input(m, "Coeficiente a:")
        self.ent_db = self.crear_input(m, "Coeficiente b:")
        self.ent_dc = self.crear_input(m, "Resultado c:")
        tk.Button(m, text="RESOLVER Y VERIFICAR", command=self.run_dio, bg="#FF6D00", fg="white", font=("Arial", 10, "bold"), padx=20, pady=10, relief="flat").pack(pady=20)
        self.txt_dio = self.crear_output(m)
# Ahora realizamos un método auxiliar para crear filas de entrada (etiqueta alineada a la derecha + campo de texto con borde y destaque azul al enfocarse).
    def crear_input(self, master, label_text):
        frame = tk.Frame(master, bg="white")
        frame.pack(pady=5)
        tk.Label(frame, text=label_text, font=("Arial", 10), bg="white", width=15, anchor="e").pack(side="left", padx=5)
        ent = tk.Entry(frame, font=("Arial", 11), bd=1, relief="solid", highlightthickness=1, highlightcolor="#2979FF")
        ent.pack(side="left", padx=5, ipady=3)
        return ent

# Y creamos el área de texto grande para mostrar resultados, con fuente monoespaciada.
    def crear_output(self, master):
        txt = tk.Text(master, font=("Consolas", 11), bg="#F1F3F4", fg="#202124", relief="flat", padx=15, pady=15)
        txt.pack(expand=True, fill="both", padx=10, pady=10)
        return txt

# Luego creamos métodos cortos que borran y rellenan los campos de entrada correspondientes cuando se pulsa un botón de ejemplo.
    def fill_div(self, a, b): self.ent_div_a.delete(0, tk.END); self.ent_div_a.insert(0, a); self.ent_div_b.delete(0, tk.END); self.ent_div_b.insert(0, b)
    def fill_base(self, a, b): self.ent_bas_a.delete(0, tk.END); self.ent_bas_a.insert(0, a); self.ent_bas_b.delete(0, tk.END); self.ent_bas_b.insert(0, b)
    def fill_mcd(self, a, b): self.ent_mcd_a.delete(0, tk.END); self.ent_mcd_a.insert(0, a); self.ent_mcd_b.delete(0, tk.END); self.ent_mcd_b.insert(0, b)
    def fill_dio(self, a, b, c): self.ent_da.delete(0, tk.END); self.ent_da.insert(0, a); self.ent_db.delete(0, tk.END); self.ent_db.insert(0, b); self.ent_dc.delete(0, tk.END); self.ent_dc.insert(0, c)

# En general para run_div, base, mcd y dio, ya al pulsar calcular esta sección convierte los textos a enteros, llama a la función del módulo numeros,
# muestra el proceso detallado devuelto y si hay error, muestra el mensaje de error.
    def run_div(self):
        try:
            q, r, proc = numeros.algoritmo_division(int(self.ent_div_a.get()), int(self.ent_div_b.get()))
            self.txt_div.delete("1.0", tk.END); self.txt_div.insert(tk.END, proc)
        except Exception as e: messagebox.showerror("Error", "Ingrese números enteros válidos o es posible que el divisor                                       'b' sea menor a 0.")
        
    def run_base(self):
        try:
            val = int(self.ent_bas_a.get())
            base = int(self.ent_bas_b.get())
            rep, pol, pasos = numeros.cambio_base(val, base)
            self.txt_base.delete("1.0", tk.END)
            self.txt_base.insert(tk.END, f">>> RESULTADOS:\n" + f"\nFORMA POLINOMIAL:\n{val} = {pol}\n\n•Por el algoritmo de la división:\n\nDIVISIONES SUCESIVAS:\n" + f"\n".join(pasos))
            self.txt_base.insert(tk.END, f"\n\n• Ahora, leemos los residuos resultantes de abajo hacia arriba:")
            self.txt_base.insert(tk.END, f"\n\n∴ ({val}) en base 10 = ({rep}) en base {base}")
        except Exception as e: messagebox.showerror("Error", "Ingrese números enteros validos o es posible que 'b' no                                cumpla con estar entre 2 y 16.")

    def run_mcd(self):
        try:
            m, x, y, divs, recon = numeros.euclides_extendido(int(self.ent_mcd_a.get()), int(self.ent_mcd_b.get()))
            self.txt_mcd.delete("1.0", tk.END)
            res = f">>> RESULTADOS:\n\n"
            res += "MÁXIMO COMÚN DIVISOR: \n\n"
            res += f"• Primero, para encontrar el mcd de {int(self.ent_mcd_a.get())} y {int(self.ent_mcd_b.get())} debemos aplicar el algoritmo de Euclides:\n"
            res += "\nTABLA DE RESIDUOS(ALGORITMO DE EUCLIDES):\n"
            res += "\n".join([f"{p['a']} = {p['b']}({p['q']}) + {p['r']}" for p in divs])
            res += f"\n\n• Por el Algoritmo de Euclides el mcd de {int(self.ent_mcd_a.get())} y {int(self.ent_mcd_b.get())} es el último residuo distinto de cero, entonces:\n"
            res += f"\n∴ {m} = mcd({int(self.ent_mcd_a.get())}, {int(self.ent_mcd_b.get())})\n"
            res += "\n\nCOMBINACIÓN LINEAL: \n\n"
            res += f"• Ahora, para expresar el máximo común divisor de {int(self.ent_mcd_a.get())} y {int(self.ent_mcd_b.get())} como combinación lineal (ax + by) de dichos números, del ejemplo\nanterior tenemos que:\n"
            res += "\nSUSTITUCIÓN HACIA ATRÁS DE EUCLIDES: \n"
            for paso in recon:
                res += f"{paso}\n"
            res += f"\nAsí pues, podemos ver que x = {x} y y = {y} tales que:"
            res += f"\n\n∴ El mcd({int(self.ent_mcd_a.get())}, {int(self.ent_mcd_b.get())}) = {int(self.ent_mcd_a.get())}({x}) + {int(self.ent_mcd_b.get())}({y})"
            res += f", es decir: {int(self.ent_mcd_a.get())}({x}) + {int(self.ent_mcd_b.get())}({y}) = {m}."
            self.txt_mcd.insert(tk.END, res)
        except: messagebox.showerror("Error", "Ingresa números válidos.")

    def run_dio(self):
        try:
            a, b, c = int(self.ent_da.get()), int(self.ent_db.get()), int(self.ent_dc.get())
            d, x0_b, y0_b, divs, recon = numeros.euclides_extendido(a, b)
            self.txt_dio.delete("1.0", tk.END)
            if c % d != 0:
                self.txt_dio.insert(tk.END, f"El MCD({a}, {b}) = {d}, y {d} no divide a {c}\n\n∴ NO HAY SOLUCIONES ENTERAS.")
                return
            f = c // d
            x0, y0 = x0_b * f, y0_b * f
            n = 1
            xn = x0 + (b // d) * n
            yn = y0 - (a // d) * n
            res = f">>> RESULTADOS: \n\n"
            res += f"Ecuación diofántica dada: {int(self.ent_da.get())}x + {int(self.ent_db.get())}y = {int(self.ent_dc.get())}\n\n"
            res += f"• Sabemos que el mcd({int(self.ent_da.get())}, {int(self.ent_db.get())}) = {d}\n"
            res += "• Sea d el Máximo Común Divisor de a y b. Por definición, d puede 'sacarse como factor común' de la parte izquierda de la ecuación: d(k_1x + k_2y) = c.\nSi el lado izquierdo es un múltiplo de d, el lado derecho (c) obligatoriamente debe ser múltiplo de d. Si d no divide a c, la ecuación es imposible en números enteros."
            res += f"\n• Como {d}|{int(self.ent_dc.get())}, la ecuación tiene infinitas soluciones\n\n"
            res += f"SOLUCIÓN PARTICULAR:\nx0 = {x0}, y0 = {y0} es una solución particular\n"
            res += f"• También, todas la soluciones de la ecuación son de la forma (SOLUCIÓN GENERAL):\n\nx = {x0} + ({int(self.ent_db.get())}/{d})n, donde n ∈ ℤ\ny = {y0} - ({int(self.ent_da.get())}/{d}), donde n ∈ ℤ\n"
            res += f"\n\nVERIFICACIÓN GENERAL: Sea n={n}:\n"
            res += f"x = {x0} + ({b}/{d})({n}) = {xn}\n"
            res += f"y = {y0} - ({a}/{d})({n}) = {yn}\n\n"
            res += f"COMPROBACIÓN FINAL:\n{a}({xn}) + {b}({yn}) = {a*xn + b*yn}\n"
            res += f"{a*xn} + {b*yn} = {a*xn + b*yn}\n"
            res += f"∴ Tenemos que: {a*xn + b*yn} = {a*xn + b*yn}, por lo cual es correcto."
            self.txt_dio.insert(tk.END, res)
        except: messagebox.showerror("Error", "Ingresa números válidos.")

# Finalmente al ejecutarse directamente este archivo, se crea la aplicación y entra en el bucle principal de eventos.
if __name__ == "__main__":
    App().mainloop()
