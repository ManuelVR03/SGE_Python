import tkinter as tk

def saludo():
    print("¡¡¡Hola, mis alumn@s de DAM2 ¡¡¡")

root = tk.Tk()
root.title("Ejemplo de Callback")

# Aquí, 'saludo' es la función callback que se ejecutará al hacer clic en el botón.
boton = tk.Button(root, text="Chic@s haced click aquí", command=saludo)
boton.pack()

root.mainloop()