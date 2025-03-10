import tkinter as tk

def on_click(event):
    print("has hecho click ")

root = tk.Tk()
button = tk.Button(root, text="Haz click")
button.bind("<Button-1>", on_click)  # Asocia un clic con la función on_click
button.pack()
root.mainloop()
