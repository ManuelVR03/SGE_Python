import random

def main():
    numeros = []
    for i in range(10):
        numeros.append(random.randint(1,100))
    numeros.sort()
    print(numeros)
       
if __name__ == "__main__":
    main()