import os

def obtenerNumerosArchivo(archivo):
    if os.path.isfile(archivo):
        suma = 0
        with open(archivo, "r") as f:
            for linea in f:
                suma += int(linea)
        return suma
    else:
        print("El fichero no existe")
        return None

def main():
    archivo = input("Introduce el nombre del archivo: ")
    suma = obtenerNumerosArchivo(archivo)
    if suma > 0:
        print(f"La suma de los números del archivo es {suma}")
    
if __name__ == "__main__":
    main()
    