import random

def main():
    numeros = []
    for i in range(10):
        numeros.append(random.randint(1,10))
        print(f"Numero: {numeros[i]} Cuadrado: {numeros[i]**2} Cubo: {numeros[i]**3}")
       
if __name__ == "__main__":
    main()
    