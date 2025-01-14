def main():
    mayor = False
    for i in range(3):
        n = int(input("Introduce un número: "))
        if n > 10:
            mayor = True
    if mayor:
        print("Alguno de los 3 números es mayor que 10")
        
if __name__ == "__main__":
    main()