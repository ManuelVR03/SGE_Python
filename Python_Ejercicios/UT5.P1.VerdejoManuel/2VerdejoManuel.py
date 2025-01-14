def main():
    base = int(input("Introduce la base: "))
    exp = int(input("Introduce el exponente: "))
    print("El resultado es: ", potencia(base, exp))
    
def potencia(base, exp):
    return base**exp

if __name__ == "__main__":
    main()