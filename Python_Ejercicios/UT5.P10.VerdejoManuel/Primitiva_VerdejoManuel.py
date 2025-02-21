import random, csv, os

def menu():
    print("***** Menú *****")
    print("1. Añadir jugadores")
    print("2. Generar una combinación ganadora")
    print("3. Mostrar los jugadores con sus números")
    print("4. Mostrar los ganadores")
    print("5. Ordenar el fichero por el apellido")
    print("6. Salir")
    
def premio(aciertos):
    if aciertos == 2:
        return "2 números acertados: 1.000 euros"
    elif aciertos == 3:
        return "3 números acertados: 8.000 euros"
    elif aciertos == 4:
        return "4 números acertados: 20.000 euros"
    elif aciertos == 5:
        return "5 números acertados: 150.000 euros"
    else:
        return "6 números acertados: 1.000.000 euros"
        

def agregar_jugadores():
    with open("jugadores.csv", "a", encoding="utf-8") as fichero:
        nombre = input("Introduce el nombre: ")
        apellido = input("Introduce el apellido: ")
        linea = f"{nombre},{apellido}"
        numeros = random.sample(range(1, 50), 7)
        numeros.sort()
        for n in numeros:
            linea += f",{n}"
        fichero.write(f"{linea}\n")
        print(f"{nombre} {apellido} agregado con los números: {numeros}")

def generar_combinacion():
    ganadora = random.sample(range(1, 50), 6)
    ganadora.sort()
    print(f"La combinación ganadora es: {ganadora}")
    return ganadora

def mostrar_jugadores():
    if os.path.isfile("jugadores.csv"):
        with open("jugadores.csv", "r", encoding="utf-8") as fichero:
            lector = csv.DictReader(fichero, fieldnames=["nombre","apellido1","num1","num2","num3","num4","num5","num6","num7"])
            for linea in lector:
                print(f"{linea['nombre']} {linea['apellido1']}: {linea['num1']}, {linea['num2']}, {linea['num3']}, {linea['num4']}, {linea['num5']}, {linea['num6']}, {linea['num7']}")
    else:
        print("No hay jugadores")

def mostrar_ganadores(ganadora):
    if os.path.isfile("jugadores.csv"):
        if len(ganadora) == 0:
            print("No hay combinación ganadora")
            return
        ganadores = False
        with open("jugadores.csv", "r", encoding="utf-8") as fichero:
            lector = csv.DictReader(fichero, fieldnames=["nombre","apellido1","num1","num2","num3","num4","num5","num6","num7"])
            for linea in lector:
                aciertos = 0
                for i in range(1, 8):
                    if int(linea[f"num{i}"]) in ganadora:
                        aciertos += 1
                if aciertos > 1:
                    ganadores = True
                    print(f"{linea['nombre']} {linea['apellido1']} {premio(aciertos)}")
        if not ganadores:
            print("No hay ganadores")
    else:
        print("No hay jugadores")

def ordenar_fichero():
    if os.path.isfile("jugadores.csv"):
        jugadores = []
        with open("jugadores.csv", "r", encoding="utf-8") as fichero:
            lector = csv.DictReader(fichero, fieldnames=["nombre","apellido1","num1","num2","num3","num4","num5","num6","num7"])
            for linea in lector:
                lista = [linea["apellido1"], linea["nombre"], linea["num1"], linea["num2"], linea["num3"], linea["num4"], linea["num5"], linea["num6"], linea["num7"]]
                jugadores.append(lista)
        jugadores.sort()
        for j in jugadores:
            print(f"{j[1]} {j[0]}: {j[2]}, {j[3]}, {j[4]}, {j[5]}, {j[6]}, {j[7]}, {j[8]}")
    else:
        print("No hay jugadores")    
            
def main():
    ganadora = []
    menu()
    opcion = int(input("Introduce una opción: "))
    print()
    while opcion != 6:
        if opcion == 1:
            agregar_jugadores()
        elif opcion == 2:
            ganadora = generar_combinacion()
        elif opcion == 3:
            mostrar_jugadores()
        elif opcion == 4:
            mostrar_ganadores(ganadora)
        elif opcion == 5:
            ordenar_fichero()
        else:
            print("Opción incorrecta")
        print()
        menu()
        opcion = int(input("Introduce una opción: "))
        print()
    
if __name__ == "__main__":
    main()