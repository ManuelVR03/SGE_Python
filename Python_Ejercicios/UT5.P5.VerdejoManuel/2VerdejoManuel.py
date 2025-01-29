def main():
    cadenas = []
    cadena = input("Introduce una cadena: ")
    diccionario = {}
    letras = "abcdefghijklmnñopqrstuvwxyz "
    for letra in letras:
        diccionario[letra] = 0
    while cadena != "0":
        cadenas.append(cadena)
        cadena = input("Introduce una cadena: ")
    for cadena in cadenas:
        for caracter in cadena:
                diccionario[caracter] += 1
    for clave, valor in diccionario.items():
        print(f"La letra {clave} aparece {valor} veces")
    
if __name__ == "__main__":
    main()