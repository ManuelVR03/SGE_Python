def main():
    print("Hola mundo")
    lista = [1,4,2,6,5]
    tupla = (1,6,8,3,8)
    conjunto = {1, 5, 3, 5, 2}
    print(lista)
    print(tupla)
    print(conjunto)
    
    print(lista[1])
    print(tupla[1])
    listaConjunto = list(enumerate(conjunto))
    print(listaConjunto[1])
    
    
if __name__ == "__main__":
    main()