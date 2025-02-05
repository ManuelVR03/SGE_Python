import os

def main():
    fichero = input("Introduce el nombre del fichero: ")
    corte = int(input("Introduce el valor de corte: "))
    if os.path.isfile(fichero):
        with open(fichero, "r") as f:
            with open("menor.txt", "w") as menor:
                with open("mayor.txt", "w") as mayor:
                    for linea in f:
                        if len(linea) < corte:
                            menor.write(linea)
                        else:
                            mayor.write(linea)
    else:
        print("El fichero no existe")
    
if __name__ == "__main__":
    main()