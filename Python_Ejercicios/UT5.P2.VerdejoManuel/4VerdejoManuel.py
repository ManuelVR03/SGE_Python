def main():
    edad = int(input("Introduce tu edad: "))
    if edad < 4:
        print("Puedes entrar gratis.")
    elif edad >= 4 and edad <= 18:
        print("Debes pagar 5€.")
    else:
        print("Debes pagar 10€.")

if __name__ == "__main__":
    main()