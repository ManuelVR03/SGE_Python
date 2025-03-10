import tkinter as tk

def on_click(event):
    print("Botón presionado")

root = tk.Tk()
button = tk.Button(root, text="Presionar")
button.bind("<Button-1>", on_click)  # Asocia un clic izquierdo con la función on_click
button.pack()
root.mainloop()
