import tkinter as tk
from tkinter import messagebox
import csv
import random

# Función para cargar preguntas desde el archivo CSV
def cargar_preguntas_desde_csv(nombre_archivo):
    preguntas = {}
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            lector_csv = csv.DictReader(archivo)
            for fila in lector_csv:
                categoria = fila["Categoría"]
                nivel = fila["Nivel"]
                pregunta = fila["Pregunta"]
                respuestas = list(fila["Opciones"].split(","))
                correcta = fila["Respuesta"]
                puntuacion = int(fila["Puntos"])
                
                if categoria not in preguntas:
                    preguntas[categoria] = {}
                if nivel not in preguntas[categoria]:
                    preguntas[categoria][nivel] = []
                
                preguntas[categoria][nivel].append({
                    "pregunta": pregunta,
                    "respuestas": respuestas,
                    "correcta": correcta,
                    "puntuacion": puntuacion
                })
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{nombre_archivo}'.")
    except ValueError:
        print(f"Error: Puntuación no válida en el archivo '{nombre_archivo}'.")
    
    return preguntas

# Función para jugar
def jugar():
    nombre_archivo = "preguntas_trivial.csv"
    preguntas = cargar_preguntas_desde_csv(nombre_archivo)
    
    if not preguntas:
        messagebox.showerror("Error", f"No se encontró el archivo '{nombre_archivo}'.")
        return
    
    puntuacion_total = 0

    # Configuración de la ventana principal de Tkinter
    root = tk.Tk()
    root.title("Trivial en Python")
    root.geometry("700x600")
    root.configure(bg="#282c34")

    # Marco para selección de categoría y nivel
    frame_seleccion = tk.Frame(root, bg="#3c4048", padx=20, pady=20)
    frame_seleccion.pack(pady=10)

    categoria_var = tk.StringVar()
    nivel_var = tk.StringVar()

    categorias = list(preguntas.keys())
    niveles = ["fácil", "medio", "difícil"]

    tk.Label(frame_seleccion, text="Selecciona una categoría:", fg="white", bg="#3c4048", font=("Arial", 12, "bold")).grid(row=0, column=0, padx=10, pady=5)
    categoria_menu = tk.OptionMenu(frame_seleccion, categoria_var, *categorias)
    categoria_menu.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(frame_seleccion, text="Selecciona una dificultad:", fg="white", bg="#3c4048", font=("Arial", 12, "bold")).grid(row=1, column=0, padx=10, pady=5)
    nivel_menu = tk.OptionMenu(frame_seleccion, nivel_var, *niveles)
    nivel_menu.grid(row=1, column=1, padx=10, pady=5)

    tk.Button(frame_seleccion, text="Comenzar", command=lambda: mostrar_pregunta(), bg="#61afef", fg="white", font=("Arial", 12, "bold")).grid(row=2, column=0, columnspan=2, pady=10)

    # Marco para preguntas y respuestas
    frame_juego = tk.Frame(root, bg="#282c34", padx=20, pady=5)
    frame_juego.pack(pady=10)

    pregunta_label = tk.Label(frame_juego, text="", fg="white", bg="#282c34", font=("Arial", 14, "bold"), wraplength=600, justify="center")
    pregunta_label.grid(row=0, column=0, columnspan=2, pady=10)

    # Botones de respuestas estilizados
    respuesta_buttons = []
    for i in range(4):
        btn = tk.Button(frame_juego, text="", font=("Arial", 12), width=40, height=2, bg="#98c379", fg="black")
        btn.grid(row=i+1, column=0, columnspan=2, pady=5)
        respuesta_buttons.append(btn)

    # Etiqueta para puntuación
    puntuacion_label = tk.Label(root, text="Puntuación total: 0", fg="white", bg="#282c34", font=("Arial", 12, "bold"))
    puntuacion_label.pack(pady=10)

    # Función para mostrar la siguiente pregunta
    def mostrar_pregunta():
        nonlocal puntuacion_total
        categoria_seleccionada = categoria_var.get()
        nivel_seleccionado = nivel_var.get()

        if categoria_seleccionada not in preguntas or nivel_seleccionado not in preguntas[categoria_seleccionada]:
            messagebox.showerror("Error", f"No hay preguntas para la categoría '{categoria_seleccionada}' y nivel '{nivel_seleccionado}'.")
            return

        pregunta = random.choice(preguntas[categoria_seleccionada][nivel_seleccionado])

        pregunta_label.config(text=pregunta["pregunta"])

        for i, respuesta in enumerate(pregunta["respuestas"]):
            respuesta_buttons[i].config(text=respuesta, command=lambda r=respuesta: verificar_respuesta(pregunta, r))

    # Función para verificar la respuesta del usuario
    def verificar_respuesta(pregunta, respuesta):
        nonlocal puntuacion_total
        if respuesta == pregunta["correcta"]:
            puntuacion_total += pregunta["puntuacion"]
            messagebox.showinfo("Correcto", f"¡Correcto! Ganaste {pregunta['puntuacion']} puntos.")
        else:
            messagebox.showinfo("Incorrecto", "¡Incorrecto!")

        puntuacion_label.config(text=f"Puntuación total: {puntuacion_total}")

        if messagebox.askyesno("Seguir jugando", "¿Quieres seguir jugando?"):
            mostrar_pregunta()
        else:
            root.destroy()

    root.mainloop()

# Iniciar el juego
jugar()
