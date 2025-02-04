def main():
    with open("numeros.txt", "w") as f:
        for i in range(1, 101):
            f.write(f"{i}\n")
    
if __name__ == "__main__":
    main()