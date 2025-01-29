def main():
    estudiantes = {}
    num = int(input("Introduce el número de estudiantes (Máx 10): "))
    media = 0
    for i in range(num):
        nombre = input("Introduce el nombre del estudiante: ")
        nota = int(input("Introduce la nota del estudiante: "))
        estudiante = {"nombre": nombre, "nota": nota}
        estudiantes[i+1] = estudiante
    print("Estudiantes suspensos:")
    for valor in estudiantes.values():
        if valor["nota"] < 5:
            print(f"{valor['nombre']}")
    print("Estudiantes aprobados:")
    for valor in estudiantes.values():
        if valor["nota"] >= 5:
            print(f"{valor['nombre']}")
    for valor in estudiantes.values():
        media += valor["nota"]
    media = media / num
    print(f"La media de las notas es: {media:.2f}")
    
if __name__ == "__main__":
    main()