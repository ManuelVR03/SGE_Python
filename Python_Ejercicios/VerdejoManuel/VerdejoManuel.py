def menu():
    print()
    print("*** MENÚ ***")
    print("1. Mostrar la lista.")
    print("2. Inserta un nombre en la lista.")
    print("3. Elimina un nombre de la lista.")
    print("4. Crea una copia independiente.")
    print("5. Añade elemento a la segunda lista independiente.")
    print("6. Lista de pesos.")
    print("7. Muestra el contenido de la lista de pesos.")
    print("8. Cuántas personas pesan más de 100 kg.")
    print("9. Salir.")

def main():
    lista = []
    listaCopy = []
    pesos = []
    opt = 0
    media = 0
    cont = 0
    for i in range(5):
        lista.append(input(f"Introduce el nombre del alumno {i+1}: "))
    menu()
    opt = int(input("Introduce una opción: "))
    while opt != 9:
        if opt == 1:
            print(lista)
        elif opt == 2:
            lista.append(input("Introduce un nuevo nombre: "))
        elif opt == 3:
            nombre = input("Introduce un nombre a eliminar: ")
            if nombre not in lista:
                print("No está en la lista.")
            else:
                lista.remove(nombre)
        elif opt == 4:
            listaCopy = lista.copy()
        elif opt == 5:
            listaCopy.append(input("Introduce un nombre para la lista independiente: "))
            print(lista)
            print(listaCopy)
        elif opt == 6:
            pesos = [53.2, 141.8, 105.3, 78.2, 60.4]
        elif opt == 7:
            for i in range(5):
                media += pesos[i]
            print(f"La media de peso es {media/5:.2f}")
            print(f"El precio máximo es {max(pesos)}")
            print(f"El precio mínimo es {min(pesos)}")
        elif opt == 8:
            for i in range(5):
                if pesos[i] > 100:
                    cont += 1
            if cont > 0:
                print(f"Hay {cont} personas con sobrepeso.")
        else:
            print("La opción no es válida")
        menu()
        opt = int(input("Introduce una opción: "))
    

if __name__ == "__main__":
    main()