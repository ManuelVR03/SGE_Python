#Queremos guardar la temperatura mínima y máxima de 5 días. Realiza un programa que de la siguiente información:
#La temperatura media de cada día
#Los días con menos temperatura
#Se lee una temperatura por teclado y se muestran los días cuya temperatura máxima coincide #con ella. si no existe ningún día se muestra un mensaje de información.
def main():
    temperaturas = []
    media = []
    for i in range(5):
        temperaturas.append(int(input(f"Introduce la temperatura mínima del día {i+1}: ")))
        temperaturas.append(int(input(f"Introduce la temperatura máxima del día {i+1}: ")))
        media.append((temperaturas[i]+temperaturas[i+1])/2)
    maximas = temperaturas[1::2]
    for i in media:
        print(f"La temperatura media del día es: {i}")
    