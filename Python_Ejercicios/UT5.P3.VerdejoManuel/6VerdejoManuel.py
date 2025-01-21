def main():
    numeros = []
    num = int(input("Introduce un número: "))
    while num >= 0:
        numeros.append(num)
        num = int(input("Introduce un número: "))
    numeros2 = []
    for i in numeros:
        if i not in numeros2:
            numeros2.append(i)
    print(numeros2)

if __name__ == "__main__":
    main()