def main():
    suma = 0
    producto = 1
    for i in range(7):
        n = int(input("Introduce un número entero: "))
        while n < 0:
            print("El número introducido no es válido.")
            n = int(input("Introduce un número entero: "))
        suma = suma + n
        producto = producto * n
    print("La suma de los números es: ", suma)
    print("El producto de los números es: ", producto)
    
if __name__ == "__main__":
    main()