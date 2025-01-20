def main():
    frase = input("Introduce una frase: ")
    letra = input("Introduce una letra: ")
    if letra not in frase:
        print(f"La letra {letra} no está en la frase.")
    else:
        veces = frase.count(letra)
        print(f"La letra {letra} aparece {veces} veces en la frase.")
        
if __name__ == "__main__":
    main()