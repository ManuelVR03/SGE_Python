def main():
    temperaturas = []
    media = []
    for i in range(5):
        temperaturas.append(float(input(f"Introduce la temperatura mínima del día {i+1}: ")))
        temperaturas.append(float(input(f"Introduce la temperatura máxima del día {i+1}: ")))
        media.append((temperaturas[i]+temperaturas[i+1])/2)
    maximas = temperaturas[1::2]
    minimas = temperaturas[::2]
    minima = min(temperaturas)
    for i in range(5):
        print(f"La temperatura media del día {i+1} es: {media[i]:.2f}ºC")
    print("Los días con menos temperatura son: ")
    for i in range(5):
        if minimas[i] == minima:
            print(f"Día {i+1}")
    temperatura = float(input("Introduce una temperatura: "))
    enc = True
    for i in range(5):
        if temperatura == maximas[i]:
            print(f"El día {i+1} coincide con la temperatura máxima introducida")
            enc = False
    if enc:
        print("No hay ningún día con la temperatura máxima introducida")
        
if __name__ == "__main__":
    main()