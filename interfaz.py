# PROYECTO DEL PARCIAL 3: DIVISIBILIDAD
# MATERIA: MATEMÁTICAS DISCRETAS.
# Archivo: interfaz.py

# INTEGRANTES DEL EQUIPO:
# - BRANDON ARENAS GUZMÁN.
# - JOHAN ALEJANDRO CABAÑAS BRINGAS.
# - AARON LEON CRUZ.
# - JESUS ANTONIO ROJAS RODRÍGUEZ.
# - AZAEL ALEJANDRO VAZQUEZ SEGURA.

"""
Módulo de interfaz gráfica (GUI) usando Tkinter.
Se encarga de la interacción con el usuario, validación de entradas
y visualización de resultados obtenidos del módulo de lógica (numeros.py).
"""

import tkinter as tk
from tkinter import ttk, messagebox
import numeros

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Proyecto Parcial 3 - Divisibilidad")
        self.geometry("1100x850")
        self.configure(bg="#F5F5F7") 

        # Configuración de estilos
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

        self.nb = ttk.Notebook(self)
        self.tabs = {}

        nombres_pestanas = ["División", "Cambio de base", "MCD", "Diofánticas"]
        for t in nombres_pestanas:
            f = tk.Frame(self.nb, bg="white")
            self.nb.add(f, text=t)

            # Panel lateral (Ejemplos)
            side = tk.Frame(f, width=240, bg="#F8F9FA", bd=0)
            side.pack(side="left", fill="y", padx=2, pady=2)
            
            tk.Frame(f, width=1, bg="#E0E0E0").pack(side="left", fill="y")
            
            # Panel principal
            main = tk.Frame(f, bg="white")
            main.pack(side="right", expand=True, fill="both", padx=20, pady=20)
            
            tk.Label(side, text="EJEMPLOS", font=("Arial", 10, "bold"), 
                     bg="#F8F9FA", fg="#757575").pack(pady=(20, 10))
            
            self.tabs[t] = (main, side)

        self.nb.pack(expand=True, fill="both", padx=10, pady=10)
        self.setup_ui()

    def crear_boton_ejemplo(self, p_side, texto, comando):
        btn = tk.Button(p_side, text=texto, command=comando,
                        font=("Arial", 9), bg="#FFFFFF", fg="#424242",
                        relief="flat", overrelief="groove", cursor="hand2",
                        activebackground="#2979FF", activeforeground="white",
                        padx=10, pady=8)
        btn.pack(fill="x", padx=15, pady=5)

    def setup_ui(self):
        # --- PESTAÑA 1: DIVISIÓN ---
        m, s = self.tabs["División"]
        self.crear_boton_ejemplo(s, "Caso Negativo: -14, 5", lambda: self.fill_div(-14, 5))
        self.crear_boton_ejemplo(s, "Caso Estándar: 20, 3", lambda: self.fill_div(20, 3))
        self.crear_boton_ejemplo(s, "Divisor negativo: 20, -3", lambda: self.fill_div(20, -3))

        tk.Label(m, text="Algoritmo de la división", font=("Arial", 18, "bold"), bg="white", fg="#212121").pack(pady=10)
        self.ent_div_a = self.crear_input(m, "Dividendo (a):")
        self.ent_div_b = self.crear_input(m, "Divisor (b ≠ 0):")
        tk.Button(m, text="CALCULAR", command=self.run_div, bg="#2979FF", fg="white", 
                  font=("Arial", 10, "bold"), padx=20, pady=10, relief="flat").pack(pady=20)
        self.txt_div = self.crear_output(m)

        # --- PESTAÑA 2: CAMBIO DE BASE ---
        m, s = self.tabs["Cambio de base"]
        self.crear_boton_ejemplo(s, "255 a Hex (16)", lambda: self.fill_base(255, 16))
        self.crear_boton_ejemplo(s, "100 a Binario (2)", lambda: self.fill_base(100, 2))
        
        tk.Label(m, text="Cambio de base", font=("Arial", 18, "bold"), bg="white").pack(pady=10)
        self.ent_bas_a = self.crear_input(m, "Número dec (a ≥ 0):")
        self.ent_bas_b = self.crear_input(m, "Base (2 ≤ b ≤ 16):")
        tk.Button(m, text="CONVERTIR", command=self.run_base, bg="#00C853", fg="white", 
                  font=("Arial", 10, "bold"), padx=20, pady=10, relief="flat").pack(pady=20)
        self.txt_base = self.crear_output(m)

        # --- PESTAÑA 3: MCD ---
        m, s = self.tabs["MCD"]
        self.crear_boton_ejemplo(s, "MCD de 444 y 370", lambda: self.fill_mcd(444, 370))
        self.crear_boton_ejemplo(s, "MCD de 120 y 45", lambda: self.fill_mcd(120, 45))
        
        tk.Label(m, text="Algoritmo de Euclides y Combinación lineal", font=("Arial", 18, "bold"), bg="white").pack(pady=10)
        self.ent_mcd_a = self.crear_input(m, "1er número (a):")
        self.ent_mcd_b = self.crear_input(m, "2do número (b):")
        tk.Button(m, text="CALCULAR MCD", command=self.run_mcd, bg="#6200EA", fg="white", 
                  font=("Arial", 10, "bold"), padx=20, pady=10, relief="flat").pack(pady=20)
        self.txt_mcd = self.crear_output(m)

        # --- PESTAÑA 4: DIOFÁNTICAS ---
        m, s = self.tabs["Diofánticas"]
        self.crear_boton_ejemplo(s, "5x + 3y = 10", lambda: self.fill_dio(5, 3, 10))
        self.crear_boton_ejemplo(s, "140x + 370y = 74", lambda: self.fill_dio(140, 370, 74))
        self.crear_boton_ejemplo(s, "Sin Solución: 6x + 9y = 5", lambda: self.fill_dio(6, 9, 5))
        
        tk.Label(m, text="Ecuaciones diofánticas lineales: ax + by = c", font=("Arial", 18, "bold"), bg="white").pack(pady=10)
        self.ent_da = self.crear_input(m, "Coeficiente a:")
        self.ent_db = self.crear_input(m, "Coeficiente b:")
        self.ent_dc = self.crear_input(m, "Resultado c:")
        tk.Button(m, text="RESOLVER Y VERIFICAR", command=self.run_dio, bg="#FF6D00", fg="white", 
                  font=("Arial", 10, "bold"), padx=20, pady=10, relief="flat").pack(pady=20)
        self.txt_dio = self.crear_output(m)

    def crear_input(self, master, label_text):
        frame = tk.Frame(master, bg="white")
        frame.pack(pady=5)
        tk.Label(frame, text=label_text, font=("Arial", 10), bg="white", width=20, anchor="e").pack(side="left", padx=5)
        ent = tk.Entry(frame, font=("Arial", 11), bd=1, relief="solid", highlightthickness=1, highlightcolor="#2979FF")
        ent.pack(side="left", padx=5, ipady=3)
        return ent

    def crear_output(self, master):
        txt = tk.Text(master, font=("Consolas", 11), bg="#F1F3F4", fg="#202124", relief="flat", padx=15, pady=15)
        txt.pack(expand=True, fill="both", padx=10, pady=10)
        return txt

    # Helpers de llenado
    def fill_div(self, a, b): self.ent_div_a.delete(0, tk.END); self.ent_div_a.insert(0, a); self.ent_div_b.delete(0, tk.END); self.ent_div_b.insert(0, b)
    def fill_base(self, a, b): self.ent_bas_a.delete(0, tk.END); self.ent_bas_a.insert(0, a); self.ent_bas_b.delete(0, tk.END); self.ent_bas_b.insert(0, b)
    def fill_mcd(self, a, b): self.ent_mcd_a.delete(0, tk.END); self.ent_mcd_a.insert(0, a); self.ent_mcd_b.delete(0, tk.END); self.ent_mcd_b.insert(0, b)
    def fill_dio(self, a, b, c): self.ent_da.delete(0, tk.END); self.ent_da.insert(0, a); self.ent_db.delete(0, tk.END); self.ent_db.insert(0, b); self.ent_dc.delete(0, tk.END); self.ent_dc.insert(0, c)

    # --- LÓGICA DE EJECUCIÓN ---

    def run_div(self):
        try:
            a_val = int(self.ent_div_a.get())
            b_val = int(self.ent_div_b.get())
            
            q, r, pasos = numeros.algoritmo_division(a_val, b_val)
            
            self.txt_div.delete("1.0", tk.END)
            res = f">>> RESULTADOS:\n\n"
            res += f"Cociente (q) = {q}\nResiduo (r) = {r}\n\n"
            res += "\n".join(pasos)
            res += f"\n\nExplicación final:\n{a_val} = {b_val} x {q} + {r}, donde 0 <= {r} < |{b_val}|"
            
            self.txt_div.insert(tk.END, res)
        except ValueError as e:
            messagebox.showerror("Error Matemático", str(e))
        except Exception:
            messagebox.showerror("Error", "Entrada inválida. Ingrese números enteros.")

    def run_base(self):
        try:
            val = int(self.ent_bas_a.get())
            base = int(self.ent_bas_b.get())
            
            rep, pol, pasos = numeros.cambio_base(val, base)
            
            self.txt_base.delete("1.0", tk.END)
            res = (f">>> RESULTADOS:\n\n"
                   f"Número decimal: {val}\n"
                   f"Base destino: {base}\n\n"
                   f"REPRESENTACIÓN FINAL: ({rep}) base {base}\n"
                   f"Forma Polinomial: {pol}\n\n"
                   f"--- PASOS (Divisiones sucesivas) ---\n")
            res += "\n".join(pasos)
            res += f"\n\nLectura de residuos de abajo hacia arriba nos da: {rep}"
            
            self.txt_base.insert(tk.END, res)
        except ValueError as e:
            messagebox.showerror("Error", str(e))
        except Exception:
            messagebox.showerror("Error", "Entrada inválida.")

    def run_mcd(self):
        try:
            val_a = int(self.ent_mcd_a.get())
            val_b = int(self.ent_mcd_b.get())
            
            mcd, x, y, divs, recon = numeros.euclides_extendido(val_a, val_b)
            
            self.txt_mcd.delete("1.0", tk.END)
            res = f">>> RESULTADOS:\n\nMCD({val_a}, {val_b}) = {mcd}\n\n"
            
            res += "--- TABLA DE ALGORITMO DE EUCLIDES ---\n"
            for p in divs:
                res += f"{p['a']} = {p['b']}({p['q']}) + {p['r']}\n"
            
            res += "\n--- COMBINACIÓN LINEAL (Identidad de Bézout) ---\n"
            res += f"Buscamos x, y tales que: {val_a}x + {val_b}y = {mcd}\n"
            
            if recon:
                res += "Sustitución hacia atrás (conceptual):\n" + "\n".join(recon) + "\n\n"

            res += f"Resultado de coeficientes: x = {x}, y = {y}\n"
            res += f"Verificación: {val_a}({x}) + {val_b}({y}) = {val_a*x} + {val_b*y} = {val_a*x + val_b*y}"
            
            self.txt_mcd.insert(tk.END, res)
        except Exception:
            messagebox.showerror("Error", "Entrada inválida.")

    def run_dio(self):
        try:
            a = int(self.ent_da.get())
            b = int(self.ent_db.get())
            c = int(self.ent_dc.get())
            
            resultado = numeros.resolver_diofantica(a, b, c)
            
            self.txt_dio.delete("1.0", tk.END)
            
            res = f">>> ANÁLISIS DE LA ECUACIÓN: {a}x + {b}y = {c}\n\n"
            res += f"1. Calculamos MCD({a}, {b}) = {resultado['mcd']}\n"
            
            if not resultado['tiene_solucion']:
                res += f"2. Verificamos divisibilidad: {resultado['mcd']} NO divide a {c}.\n"
                res += "\nCONCLUSIÓN: La ecuación NO tiene soluciones enteras."
            else:
                res += f"2. Verificamos divisibilidad: {resultado['mcd']} divide a {c}. ¡Tiene infinitas soluciones!\n\n"
                res += f"--- SOLUCIÓN PARTICULAR ---\n"
                res += f"x0 = {resultado.get('x0')}\n"
                res += f"y0 = {resultado.get('y0')}\n\n"
                
                res += f"--- SOLUCIÓN GENERAL ---\n"
                res += resultado.get('solucion_general', '')
                
                res += f"\n\n--- VERIFICACIÓN ---\n"
                res += resultado.get('verificacion', '')
            
            self.txt_dio.insert(tk.END, res)
            
        except Exception as e:
            messagebox.showerror("Error", f"Entrada inválida o error de cálculo: {e}")

if __name__ == "__main__":
    App().mainloop()
