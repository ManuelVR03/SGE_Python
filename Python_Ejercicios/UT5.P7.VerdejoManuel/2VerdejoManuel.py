import os

def main():
    origen = input("Introduce el nombre del fichero origen: ")
    if os.path.isfile(origen):
        destino = input("Introduce el nombre del fichero destino: ")
        with open(origen, "r") as f1:
            with open(destino, "w") as f2:
                f2.write(f1.readline())
    else:
        print("El fichero no existe")
        
    
if __name__ == "__main__":
    main()