def main():
    nota = float(input("Introduce tu nota: "))
    if nota < 3:
        print("Muy deficiente")
    elif nota < 5:
        print("Insuficiente")
    elif nota < 6:
        print("Suficiente")
    elif nota < 7:
        print("Bien")
    elif nota < 9:
        print("Notable")
    else:
        print("Sobresaliente")
        
if __name__ == "__main__":
    main()            