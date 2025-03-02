import csv, random

def puntuacion(intento):
    if intento == 4:
        return 600
    elif intento == 3:
        return 400
    elif intento == 2:
        return 250
    else:
        return 150

def palabraAleatoria():
    palabras = []
    with open('palabras.csv', encoding='utf-8', mode='r') as f:
        lector = csv.reader(f)
        next(lector)
        for palabra in lector:
            palabras.append(palabra[0])
    palabra = random.choice(palabras)
    return palabra

def correcto(user):
    numeros = list(range(0,10))
    for i in numeros:
        if str(i) in user:
            return ""
    if " " in user:
        return ""
    return user
    
def guardaGanador(nombre, puntos):
    with open('puntuación.csv', encoding='utf-8', mode='a') as f:
        escritor = csv.writer(f)
        escritor.writerow([nombre, puntos])

def main():
    letrasNo = set()
    letrasNoPos = set()
    ganador = False
    pista = True
    user = ""
    puntos = 0
    nombre = input("Introduce el nombre del jugador: ")
    palabra = palabraAleatoria()
    adivina = ("_ "*len(palabra)).split()
    intentos = 4
    print("¡Wordle en Python!\n")
    while intentos != 0:
        print("Palabra: ", " ".join(adivina))
        print(f"Letras que no están en su posición: {', '.join(letrasNoPos) if letrasNoPos else ''}")
        print(f"Letras que no están en la palabra: {', '.join(letrasNo) if letrasNo else ''}")
        print(f"Intentos: {intentos}\n")
        if intentos < 4 and pista:
            ayuda = input("¿Quieres revelar una letra? (s / n): ")
            if ayuda == 's':
                for i, l in enumerate(adivina):
                    if adivina[i] == '_':
                        adivina[i] = palabra[i]
                        break
                print("Palabra: ", " ".join(adivina))
                pista = False
                puntos = -100
        user = input(f"\nIntroduce una palabra de {len(palabra)} letras: ")
        user = correcto(user)
        while len(user) != len(palabra):
            user = input(f"Introduce una palabra de {len(palabra)} letras (sin números ni espacios): ")
            user = correcto(user)
        for i, l in enumerate(user):
            if palabra[i] == user[i]:
                adivina[i] = l
            else:
                if l in palabra:
                    letrasNoPos.add(l)
                else:
                    letrasNo.add(l)
        if "_" in adivina:
            intentos = intentos - 1
        else:
            puntos = puntos + puntuacion(intentos)
            guardaGanador(nombre, puntos)
            ganador = True
            break
    if ganador:
        print(f"Has acertado en {5 - intentos} intentos.")
    else:
        print(f"Has perdido. La palabra correcta era: {palabra}")

if __name__ == "__main__":
    main()