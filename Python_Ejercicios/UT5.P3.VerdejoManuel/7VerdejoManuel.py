def menu():
    print("Opciones:")
    print("1. Contar")
    print("2. Modificar")
    print("3. Eliminar")
    print("4. Mostrar")
    print("5. Terminar")
    
def main():
    cadenas = []
    cadena = input("Introduce una cadena para añadir a la lista (fin): ")
    while cadena != "fin":
        cadenas.append(cadena)
        cadena = input("Introduce una cadena para añadir a la lista (fin): ")
    menu()
    opcion = int(input("Introduce una opción: "))
    while opcion != 5:
        if opcion == 1:
            cadena = input("Introduce una cadena para contar: ")
            print(f"La cadena {cadena} aparece {cadenas.count(cadena)} veces.")
        elif opcion == 2:
            cadena = input("Introduce una cadena a modificar: ")
            if cadena not in cadenas:
                print("La cadena no está en la lista.")
            else:
                nueva = input("Introduce la nueva cadena: ")
                for i in range(len(cadenas)):
                    if cadenas[i] == cadena:
                        cadenas[i] = nueva
        elif opcion == 3:
            cadena = input("Introduce una cadena a eliminar: ")
            if cadena not in cadenas:
                print("La cadena no está en la lista.")
            else:
                while cadena in cadenas:
                    cadenas.remove(cadena)
        elif opcion == 4:
            print(cadenas)
        else:
            print("Opción incorrecta")
        menu()
        opcion = int(input("Introduce una opción: "))
        
if __name__ == "__main__":
    main()