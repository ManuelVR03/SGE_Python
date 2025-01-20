def main():
    numero = int(input("Introduce un número: "))
    cadena = ""
    for i in range(numero):
        cadena += "*"
        print(cadena)
        
if __name__ == "__main__": 
    main()