def main():
    opcion = 0
    while opcion != 5:
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir.")
        print("5. Salir.")
        opcion = int(input("Introduce una opción: "))
        if opcion != 5:
            num1 = int(input("Introduce el primer número: "))
            num2 = int(input("Introduce el segundo número: "))
            if opcion == 1:
                print(f"La suma de {num1} y {num2} es {num1 + num2}.")
            elif opcion == 2:
                print(f"La resta de {num1} y {num2} es {num1 - num2}.")
            elif opcion == 3:
                print(f"La multiplicación de {num1} y {num2} es {num1 * num2}.")
            elif opcion == 4:
                if num2 != 0:
                    print(f"La división de {num1} y {num2} es {num1 / num2}.")
                else:
                    print("No se puede dividir por 0.")
            else:
                print("Opción no válida.")
                
if __name__ == "__main__":
    main()