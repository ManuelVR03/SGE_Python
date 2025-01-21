def main():
    notas = []
    for i in range(5):
        notas.append(int(input(f"Introduce la nota {i+1}: ")))
    print(f"Las notas son: {notas}")
    print(f"La nota media es: {sum(notas)/len(notas)}")
    print(f"La nota más alta es: {max(notas)}")
    print(f"La nota más baja es: {min(notas)}")

if __name__ == "__main__":
    main()