#4.- Carga desde teclado la información de los pacientes de un determinado hospital perteneciente a una aseguradora privada. 
#Sabemos que a través del dni del paciente queremos tener acceso a: nombre, edad, si ha sido atendido previamente en ese hospital y al código #valor numérico entero) de su médico de cabecera.
#- Visualiza la información almacenada.
#- Calcula la edad media de todos los pacientes que han sido atendidos alguna vez en ese hospital.
#- Visualiza el listado de todos los pacientes de un determinado médico cuyo código se solicitará por teclado.

def menu():
    print()
    print("*** MENÚ ***")
    print("1. Añadir paciente ")
    print("2. Mostrar la base de datos ")
    print("3. Edad media de pacientes atendidos ")
    print("4. Listar pacientes por médico ")
    print("5. SALIR ")

def main():
    baseDatos = {}
    print("*** HOSPITAL SAGRADO CORAZÓN ***")
    menu()
    opcion = int(input("Introduce una opción: "))
    while opcion != 5:
        if opcion == 1:
            nombre = input("Introduce el nombre del paciente: ")
            dni = input("Introduce el DNI del paciente: ")
            edad = int(input("Introduce la edad del paciente: "))
            atendido = input("Indica si el paciente ha sido ya atendido ( si / no ): ")
            codigo = int(input("Código del médico de cabecera: "))
            paciente = {"nombre": nombre, "edad": edad, "atendido": atendido, "codigo": codigo}
            baseDatos[dni] = paciente
        elif opcion == 2:
            print(baseDatos)
        elif opcion == 3:
            media = 0
            cont = 0
            for paciente in baseDatos.values():
                if paciente["atendido"] == "si":
                    media += paciente["edad"]
                    cont += 1
            if cont > 0:
                print(f"La media de edad del hospital es {(media/cont):.2f}")
            else:
                print("No se ha atendido a ningún paciente todavía.")
        elif opcion == 4:
            codigoBuscar = int(input("Introduce el código del médico de cabecera: "))
            print(f"Pacientes del médico {codigoBuscar}:")
            for paciente in baseDatos.values():
                if paciente["codigo"] == codigoBuscar:
                    print(paciente)
        else:
            print("Opción incorrecta")
        menu()
        opcion = int(input("Introduce una opción: "))
    
if __name__ == "__main__":
    main()