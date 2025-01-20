def main():
    numero = int(input("Introduce un número: "))
    suma = 0
    cont = 1
    media = 0
    while numero != 0:
        suma += numero
        media = suma / cont
        cont += 1
        numero = int(input("Introduce un número: "))
    print(f"La suma de los números introducidos es {suma}.")
    print(f"La media de los números introducidos es {media}.")

if __name__ == "__main__":
    main()