import random

def main():
    tabla = []
    for i in range(5):
        fila = []
        for j in range(5):
            fila.append(random.randint(1, 100))
        tabla.append(fila)
    for i in range(5):
        suma = 0
        for j in range(5):
            suma += tabla[i][j]
        print(f"La suma de la fila {i+1} es: {suma}")
    for j in range(5):
        suma = 0
        for i in range(5):
            suma += tabla[i][j]
        print(f"La suma de la columna {i+1} es: {suma}")

if __name__ == "__main__":
    main()