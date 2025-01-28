def menu():
    print()
    print("***** MENU *****")
    print("1. Añadir")
    print("2. Listar")
    print("3. Eliminar")
    print("4. Buscar")
    print("5. Listar claves")
    print("6. Listar valores")
    print("7. Listar claves y valores")
    print("8. Comprobar si la clave existe")
    print("9. Calcular suma de valores")
    print("10. Clave máxima y mínima")
    print("11. Total de elementos")
    print("12. Salir")
    
def main():
    diccionario = {}
    clave = ""
    valor = 0
    menu()
    opcion = int(input("Introduce una opción: "))
    while(opcion != 12):
        if opcion == 1:
            clave = input("Introduce la clave: ")
            valor = int(input("Introduce el valor: "))
            diccionario[clave] = valor
        elif opcion == 2:
            print(diccionario)
        elif opcion == 3:
            clave = input("Introduce la clave a eliminar: ")
            del diccionario[clave]
        elif opcion == 4:
            clave = input("Introduce la clave a buscar: ")
            print(diccionario.get(clave, "No existe la clave"))
        elif opcion == 5:
            print(diccionario.keys())
        elif opcion == 6:
            print(diccionario.values())
        elif opcion == 7:
            print(diccionario.items())
        elif opcion == 8:
            clave = input("Introduce la clave a buscar: ")
            print(clave in diccionario)
        elif opcion == 9:
            print(sum(diccionario.values()))
        elif opcion == 10:
            print("Clave máxima: ", max(diccionario.keys()))
            print("Clave mínima: ", min(diccionario.keys()))
        elif opcion == 11:
            print("Total de elementos: ", len(diccionario))
        else:
            print("Opción no válida")
        menu()
        opcion = int(input("Introduce una opción: "))
    
if __name__ == "__main__":
    main()