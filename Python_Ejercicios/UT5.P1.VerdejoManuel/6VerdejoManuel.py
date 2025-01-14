def main():
    sueldo = int(input("Introduce tu sueldo: "))
    antiguedad = int(input("Introduce tu antigüedad: "))
    if sueldo < 500 and antiguedad > 10:
        print("Tu nuevo sueldo es: ", sueldo * 3)
    elif sueldo < 500 and antiguedad < 10:
        print("Tu nuevo sueldo es: ", sueldo * 2)
    else:
        print("Tu sueldo es: ", sueldo)

if __name__ == "__main__":
    main()