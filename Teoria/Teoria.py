def main():
    print("*****  TEORÍA DE PYTHON  *****")
    
    print("1. Listas")
    # Formas de crear una lista
    miLista = []
    miLista2 = [1, 7, 4, 6, 2]
    miLista3 = list("12345")
    # Métodos de las listas
    miLista.append(2)       # Añadir
    miLista2.remove(6)      # Eliminar
    print(miLista3)         # Mostrar
    print(miLista2[2])      # Acceder a un elemento
    # Formas de iterar una lista
    # Iterando por índice
    for i in range(len(miLista2)):
        print(miLista2[i])
        break
    
    print()
    print("2. Tuplas")
    # Formas de crear una tupla
    miTupla = ()
    miTupla2 = (1, 7, 4, 6, 2)
    miTupla3 = tuple(miLista2)
    # Métodos de las tuplas
        # Las tuplas no son mutables, por lo que no se pueden añadir o eliminar elementos
    print(miTupla3)         # Mostrar
    print(miTupla2[2])      # Acceder a un elemento
    # Formas de iterar una tupla
    for i in miTupla2:
        print(i)
        break
    
    print()
    print("3. Conjuntos")
    # A tener en cuenta: 
    #   - Los conjuntos no permiten elementos duplicados
    #   - Los conjuntos no tienen índices ni orden
    # Formas de crear un conjunto
    miConjunto = set()
    miConjunto2 = {1, 7, 4, 6, 2}
    miConjunto3 = set(miTupla2)
    # Métodos de los conjuntos
    miConjunto.add(2)       # Añadir
    miConjunto2.remove(4)   # Eliminar
    print(miConjunto3)      # Mostrar
        # No se puede acceder a un elemento de un conjunto, ya que no tiene índices ni orden
    # Formas de iterar un conjunto
    # Convirtiendo a lista
    listaConjunto = list(enumerate(miConjunto2))
    print(listaConjunto[1])
    # Usando la función enumerate para poder iterar
    for i, valor in enumerate(miConjunto2):
        print(i, valor)
        break
    
    print()
    print("4. Diccionarios")
    # Formas de crear un diccionario
    miDiccionario = {}
    miDiccionario2 = {"clave1": 1, "clave2": 2, "clave3": 3}
    miDiccionario3 = dict(clave1=1, clave2=2, clave3=3)
    # Métodos de los diccionarios   
    miDiccionario["clave4"] = 4     # Añadir
    miDiccionario2.pop("clave2")    # Eliminar
    print(miDiccionario3)           # Mostrar
    print(miDiccionario2["clave1"]) # Acceder a un elemento
    # Formas de iterar un diccionario
    # Iterando por clave
    for clave in miDiccionario2.keys():
        print(clave)
        break
    # Iterando por valor
    for valor in miDiccionario2.values():
        print(valor)
        break
    # Iterando por clave y valor
    for clave, valor in miDiccionario2.items():
        print(clave, valor)
        break
    
    
if __name__ == "__main__":
    main()