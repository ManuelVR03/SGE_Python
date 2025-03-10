import tkinter as tk

# Crear la ventana principal
root = tk.Tk()
root.title("Ejemplo de Tkinter")
root.geometry("400x400")

# Crear widgets
label = tk.Label(root, text="Etiqueta 1", bg="green")
button = tk.Button(root, text="Botón")

# Organizar widgets usando pack
label.pack(side="top", fill="x")
button.pack(side="bottom")

# Configurar un widget
label.config(text="Etiqueta Actualizada")

# Asignar un evento al botón
def on_button_click(event):
    label.config(text="¡Has hecho click en el botón!")

button.bind("<Button-1>", on_button_click)

# Iniciar el bucle principal
root.mainloop()