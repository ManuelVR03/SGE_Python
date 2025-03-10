import tkinter as tk

def saludo():
    print("¡¡¡Hola, mis alumn@s de DAM2 ¡¡¡")

def cerrar_ventana():
    root.destroy()  # Esto cierra la ventana y termina el bucle principal

root = tk.Tk()
root.title("Ejemplo de Callback")

# Aquí, 'saludo' es la función callback que se ejecutará al hacer clic en el botón.
boton = tk.Button(root, text="Chic@s haced click aquí", command=saludo)
boton.pack()

boton_salir = tk.Button(root, text="Salir", command=cerrar_ventana)
boton_salir.pack()

root.mainloop()

print("La ventana de la GUI se ha cerrado. Ahora se devuelve el control a la terminal.")
