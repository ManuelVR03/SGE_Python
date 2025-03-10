import tkinter as tk
from tkinter import messagebox
import csv
import random

def cargar_preguntas_desde_csv(nombre_archivo):
    preguntas = {}
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            lector_csv = csv.DictReader(archivo)
            for fila in lector_csv:
                categoria = fila["Categoría"]
                nivel = fila["Nivel"]
                pregunta = fila["Pregunta"]
                respuestas = [fila["Respuesta 1"], fila["Respuesta 2"], fila["Respuesta 3"], fila["Respuesta 4"]]
                correcta = fila["Respuesta Correcta"]
                puntuacion = int(fila["Puntuación"])

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
    except (FileNotFoundError, ValueError) as e:
        print(f"Error: {e}")
    return preguntas

def jugar():
    nombre_archivo = "trivial.csv"
    preguntas = cargar_preguntas_desde_csv(nombre_archivo)

    if not preguntas:
        messagebox.showerror("Error", f"No se encontró el archivo '{nombre_archivo}'.")
        return

    puntuacion_total = 0
    tiempo_restante = 30
    intervalo = None

    def mostrar_pregunta():
        nonlocal puntuacion_total, tiempo_restante, intervalo
        
        if intervalo:
            root.after_cancel(intervalo)

        categoria_seleccionada = categoria_var.get()
        nivel_seleccionado = nivel_var.get()

        preguntas_nivel = preguntas.get(categoria_seleccionada, {}).get(nivel_seleccionado)

        if not preguntas_nivel:
            messagebox.showerror("Error", "No hay preguntas disponibles para la selección.")
            return

        pregunta = random.choice(preguntas_nivel)
        pregunta_label.config(text=pregunta["pregunta"], fg="black")

        random.shuffle(pregunta["respuestas"])

        for i, boton in enumerate(botones_respuesta):
            boton.config(text=pregunta["respuestas"][i], command=lambda i=i: verificar_respuesta(pregunta, i))

        tiempo_restante = 30
        actualizar_tiempo()

    def actualizar_tiempo():
        nonlocal tiempo_restante, intervalo
        if tiempo_restante > 0:
            tiempo_label.config(text=f"Tiempo restante: {tiempo_restante} segundos", fg="black")
            tiempo_restante -= 1
            intervalo = root.after(1000, actualizar_tiempo)
        else:
            messagebox.showerror("Tiempo agotado", "¡Se acabó el tiempo! Respuesta incorrecta.")
            if messagebox.askyesno("¿Continuar?", "¿Quieres seguir jugando?"):
                mostrar_pregunta()
            else:
                root.destroy()

    def verificar_respuesta(pregunta, indice):
        nonlocal puntuacion_total, intervalo

        if intervalo:
            root.after_cancel(intervalo)

        if pregunta["respuestas"][indice] == pregunta["correcta"]:
            puntuacion_total += pregunta["puntuacion"]
            messagebox.showinfo("Correcto", f"¡Correcto! Ganaste {pregunta['puntuacion']} puntos.")
        else:
            messagebox.showerror("Incorrecto", "¡Respuesta incorrecta!")

        puntuacion_label.config(text=f"Puntuación total: {puntuacion_total}")

        if messagebox.askyesno("¿Continuar?", "¿Quieres seguir jugando?"):
            mostrar_pregunta()
        else:
            root.destroy()

    root = tk.Tk()
    root.title("Trivial Mejorado")
    root.geometry("800x800")
    root.config(bg="#F5F5F5")

    categoria_var = tk.StringVar()
    nivel_var = tk.StringVar()

    categorias = list(preguntas.keys())
    niveles = ["Fácil", "Medio", "Difícil"]

    titulo_label = tk.Label(root, text="¡Trivial Mejorado!", font=("Helvetica", 36, "bold"), bg="#4CAF50", fg="white")
    titulo_label.pack(pady=20)

    nombre_label = tk.Label(root, text="Manuel Verdejo Ramírez", font=("Helvetica", 14, "bold"), bg="#F0F0F0", fg="black")
    nombre_label.pack(pady=5)

    tk.Label(root, text="Selecciona una categoría:", font=("Helvetica", 14), bg="#F0F0F0", fg="black").pack(pady=5)
    categoria_menu = tk.OptionMenu(root, categoria_var, *categorias)
    categoria_menu.config(font=("Helvetica", 12), bg="#FFFFFF", fg="black")
    categoria_menu.pack(pady=10)

    tk.Label(root, text="Selecciona una dificultad:", font=("Helvetica", 14), bg="#F0F0F0", fg="black").pack(pady=5)
    nivel_menu = tk.OptionMenu(root, nivel_var, *niveles)
    nivel_menu.config(font=("Helvetica", 12), bg="#FFFFFF", fg="black")
    nivel_menu.pack(pady=10)

    tk.Button(root, text="Comenzar", command=mostrar_pregunta, font=("Helvetica", 14, "bold"), bg="#4CAF50", fg="white").pack(pady=20)

    pregunta_label = tk.Label(root, text="", wraplength=700, font=("Helvetica", 16, "bold"), bg="#F5F5F5")
    pregunta_label.pack(pady=20)

    botones_respuesta = []
    for _ in range(4):
        boton = tk.Button(root, text="", font=("Helvetica", 12), bg="#2196F3", fg="white")
        boton.pack(fill="x", padx=50, pady=5)
        botones_respuesta.append(boton)

    puntuacion_label = tk.Label(root, text="Puntuación total: 0", font=("Helvetica", 16), bg="#F5F5F5", fg="black")
    puntuacion_label.pack(pady=10)

    tiempo_label = tk.Label(root, text="Tiempo restante: 30 segundos", font=("Helvetica", 16, "bold"), bg="#F5F5F5", fg="black")
    tiempo_label.pack(pady=10)

    root.mainloop()

jugar()
