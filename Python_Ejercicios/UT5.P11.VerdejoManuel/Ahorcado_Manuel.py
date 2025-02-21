import csv, random

def menu():
    print(F"\n{'Menú':^30}")
    print("1. Añadir palabra")
    print("2. Introduce nombre para jugar")
    print("3. Jugar")
    print("4. Salir")
    
def dibujitos(intentos):
    print()
    if intentos == 6:
        print("           ------")
        print("           |    |")
        print("           |")
        print("           |")
        print("           |")
        print("           |")
        print("        --------\n\n")
    elif intentos == 5:
        print("           ------")
        print("           |    |")
        print("           |    O")
        print("           |")
        print("           |")
        print("           |")
        print("        --------\n\n")
    elif intentos == 4:
        print("           ------")
        print("           |    |")
        print("           |    O")
        print("           |    |")
        print("           |")
        print("           |")
        print("        --------\n\n")
    elif intentos == 3:
        print("           ------")
        print("           |    |")
        print("           |    O")
        print("           |   /|")
        print("           |")
        print("           |")
        print("        --------\n\n")
    elif intentos == 2:
        print("           ------")
        print("           |    |")
        print("           |    O")
        print("           |   /|\\")
        print("           |")
        print("           |")
        print("        --------\n\n")
    elif intentos == 1:
        print("           ------")
        print("           |    |")
        print("           |    O")
        print("           |   /|\\")
        print("           |   /")
        print("           |")
        print("        --------\n\n")
    else:
        print("           ------")
        print("           |    |")
        print("           |    O")
        print("           |   /|\\")
        print("           |   / \\")
        print("           |")
        print("        --------\n\n")
 
def puntuacion(intentos):
    if intentos == 6:
        return 150
    elif intentos == 5:
        return 100
    elif intentos == 4:
        return 75
    elif intentos == 3:
        return 50
    elif intentos == 2:
        return 25
    else:
        return 10
    
def puntuacionMaxima():
    jugadores = {}
    with open("puntuaciones.csv") as f:
        lector = csv.DictReader(f, fieldnames=["Jugador", "Puntos"])
        for fila in lector:
            jugadores[fila["Jugador"]] = int(fila["Puntos"])
    puntosMax = max(jugadores.values())
    for j in jugadores.keys():
        if jugadores[j] == puntosMax:
            print(f"\nEl jugador con la máxima puntuación hasta ahora es {j} con {jugadores[j]} puntos.")

def agregar_palabra():
    palabra = input("Introduce la palabra a añadir: ")
    with open("palabras.csv", "a") as f:
        escritor = csv.writer(f)
        escritor.writerow([palabra])
    print(f"Palabra '{palabra}' añadida al fichero.")
        
def identificacion():
    jugador = input("Introduce tu nombre: ")
    return jugador

def jugar(jugador):
    palabras = []
    letras = set()
    intentos = 6
    puntos = 0
    
    with open("palabras.csv") as f:
        lector = csv.reader(f)
        for fila in lector:
            palabras.append(fila[0])
        
    palabra = random.choice(palabras)
    palabraOculta = "_ " * len(palabra)
    palabraOculta = palabraOculta.split()
    
    print(f"\n¡Bienvenido {jugador}! Vamos a jugar.")
    
    while intentos > 0:
        dibujitos(intentos)
        print(f"Palabra a adivinar: {' '.join(palabraOculta)}")
        print(f"Letras que no están: {', '.join(letras) if letras else ''}")
        print(f"Intentos restantes: {intentos}")
        letra = input("Introduce una letra: ")
        if letra in palabra:
            for i, l in enumerate(palabra):
                if l == letra:
                    palabraOculta[i] = letra
        elif letra in letras:
            print(f"La letra '{letra}' ya ha sido introducida.")
        else:
            letras.add(letra)
            intentos -= 1
        if "_" not in palabraOculta:
            print(f"\n¡Felicidades {jugador}! Has adivinado la palabra: {palabra}")
            puntos = puntuacion(intentos)
            print(f"Has obtenido una puntuación de: {puntos} puntos.")
            break
    
    if intentos == 0:
        dibujitos(intentos)
        print(f"\n{jugador}, has perdido. La palabra era: {palabra}")
    else:
        with open("puntuaciones.csv", "a") as f:
            escritor = csv.writer(f)
            escritor.writerow([jugador, puntos])
        puntuacionMaxima()    

def main():
    jugador = ""
    print("Bienvenido al juego del ahorcado")
    menu()
    opcion = int(input("Introduce una opción: "))
    while opcion != 4:
        if opcion == 1:
            agregar_palabra()
        elif opcion == 2:
            jugador = identificacion()
        elif opcion == 3:
            jugar(jugador)
        else:
            print("Opción incorrecta")
        menu()
        opcion = int(input("Introduce una opción: "))
    
if __name__ == "__main__":
    main()