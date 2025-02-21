def cadenas():
    '''
    # print(F"") = print(f"")
    # cadena[i:j:k] = cadena desde i hasta j-1, saltando k caracteres
    '''
    print("\nTeoría de cadenas")
    cadena = "Hola soy la chuleta de Python"
    print(len(cadena))
    print(max(cadena))
    print(min(cadena))
    print(cadena.upper())
    print(cadena.lower())
    print(cadena.title())       # Primera letra de cada palabra en mayúsculas
    print(cadena.split(' '))    # Devuelve una lista
    print("{:>10}".format("derecha"))
    print("{:<10}".format("izquierda"))
    print("{:^10}".format("centro"))
    
def variables():
    '''
    # letra, número o _
    # Tipado dinámico (no hace falta declarar el tipo de variable)
    # int(x) = convierte x a entero
    # float(x) = convierte x a flotante
    # str(x) = convierte x a cadena
    # bool(x) = convierte x a booleano
    # No se pueden usar palabras reservadas
    '''
    import keyword
    print("\nPalabras reservadas")
    print(keyword.kwlist)    # Lista de palabras reservadas

def listas():
    '''
    # Más en Cositas()
    '''
    print("\nTeoría de listas") # []
    lista = list(range(1,11))
    print(f"La lista: {lista}")
    print(f"Índice 2: {lista[2]}")
    print(f"Pares: {lista[1::2]}")
    # Métodos
    print(f"Número de elementos: {len(lista)}")
    print(f"Suma de elementos: {sum(lista)}")
    print(f"Máximo: {max(lista)}")
    print(f"Mínimo: {min(lista)}")
    print(f"Todos son True: {all(lista)}")
    print(f"Alguno es True: {any(lista)}")
    print(f"Índice de 5: {lista.index(5)}")
    print(f"5 aparece {lista.count(5)} veces")
    lista.append(11)
    print(f"Lista con 11: {lista}")
    lista.extend(range(12,16))
    print(f"Lista extendida: {lista}")
    lista.insert(0, 0)
    print(f"Lista con 0: {lista}")
    lista.remove(0)
    print(f"Lista sin 0: {lista}")
    print(f"Elimina el último: {lista.pop()}")
    print(f"Lista sin el último: {lista}")
    lista.sort()
    print(f"Lista ordenada: {lista}")
    lista.reverse()
    print(f"Lista invertida: {lista}")
    
def tuplas():
    '''
    # INMUTABLE
    '''
    print("\nTeoría de tuplas") # ()
    tupla = tuple(range(1,11))
    print(f"Tupla: {tupla}")
    # Tiene los mismos métodos que las listas, excepto añadir, eliminar y modificar elementos
    # Para modificar, se puede convertir la tupla en una lista auxiliar
    aux = list(tupla)
    aux.append(11)
    tupla = tuple(aux)
    print(f"Tupla: {tupla}")

def conjuntos():
    '''
    # No tienen indices (orden aleatorio)
    # No tienen elementos repetidos
    '''
    print("\nTeoría de conjuntos") # set()
    conjunto = {8, 2, 5, 13, 20, 4}
    print(f"Conjunto: {conjunto}")
    # Métodos add / remove
    # Iterar con enumerate
    for i, valor in enumerate(conjunto):
        print(f"Índice {i}: {valor}")
        
def diccionarios():
    '''
    # Clave: valor
    '''
    print("\nTeoría de diccionarios") # {}
    diccionario = dict(Manuel = 22, Lucia = 24, Raul = 39, Blanca = 34)
    print(f"Diccionario: {diccionario}")
    print(f"Manuel: {diccionario['Manuel']}") # Acceder a un valor con clave existente
    print(f"Valor si existe: {diccionario.get('Paco', 'Por defecto')}") # Acceder a un valor con clave inexistente
    print(f"Claves: {diccionario.keys()}") # Mostrar claves
    print(f"Valores: {diccionario.values()}") # Mostrar valores
    print(f"Clave-Valor: {diccionario.items()}") # Mostrar clave-valor
    print(f"Clave existe: {'Manuel' in diccionario}") # Comprobar si una clave existe
    diccionario['Gala'] = 19 # Añadir un nuevo elemento
    print(f"Diccionario con Gala: {diccionario}")
    del diccionario['Raul'] # Eliminar un elemento
    print(f"Eliminado: {diccionario}")
    print(f"Eliminar: {diccionario.pop('Paco', 'No está')}") # Eliminar un elemento con clave sin saber si existe
    print(f"Eliminar clave-valor: {diccionario.popitem()}") # Eliminar el último
    print(f"Diccionario sin el último: {diccionario}")
    
def cositas():
    '''
    # range(n) = 0, 1, 2, ..., n-1
    # range(i, j) = i, i+1, ..., j-1
    # range(i, j, k) = i, i+k, ..., j-1
    '''
    print("\nCositas")
    import random
    print('-> Random')
    print(f"Aleatorio [0,1): {random.random():.2f}")
    print(f"Aleatorio [1,10]: {random.randint(1,10)}")
    print(f"Aleatorio decimal [1,10]: {random.uniform(1,10):.2f}")
    print(f"Aleatorios sin repetir: {random.sample(range(1,11), 5)}")
    print(f"Aleatorio con sequencia: {random.choice(['a', 'b', 'c'])}") # choices(seq, k)
    import copy
    print('-> Copias')
    lista = [1, 2, [3, 4], [5, [6, 7]]]
    print(f"Lista: {lista}")
    lista2 = lista                  # Misma lista con distintas referencias
    lista3 = list(lista)            # Nueva lista con los mismos valores
    # list(lista) = lista.copy()
    # Copias superficiales y profundas
    # Influyen si hay secuencias anidadas
    lista4 = lista.copy()           # Copia superficial
    lista5 = copy.deepcopy(lista)   # Copia profunda
    lista[2][0] = 10
    lista[3][1][1] = 20
    print(f"Lista modificada: {lista}")
    print(f"Lista misma referencia: {lista2}")
    print(f"Lista con mismos valores: {lista3}")
    print(f"Lista copia superficial: {lista4}")
    print(f"Lista copia profunda: {lista5}")
    
def ficheros():
    '''
    # f = open('fichero.txt') / f.close()
    # mode:
            - r -> solo lectura
            - w -> solo escritura, sobreescribe, borra el contenido.
            - a -> solo escritura, añade al final
            - r+ -> lectura y escritura sin borrar, sobreescribe al principio.
            - w+ -> lectura y escritura borrando el contenido.
            - a+ -> lectura y escritura al final

    # CSV
    # f.write() -> escribe en el fichero (salto de linea manual)
    # lector = f.read() -> lee igual como si fuera txt sin tener en cuenta csv.
    # lector = csv.DictReader(f, fieldnames=[]) -> pasando el nombre de cada columna
    
    # Otros métodos:
    # fichero.tell() -> posicion del puntero
    # fichero.seek() -> movel el puntero
        seek(n) -> al principio
        seek(n, 1) -> desde la posición actual
        seek(n, 2) -> al final
    '''
    print("\n***** Teoría de ficheros *****")
    ruta = 'Ejemplo.txt'
    import os
    if os.path.isfile(ruta):
        print("-> El fichero existe")
    else:
        print("-> El fichero no existe")
        
    print("\nFichero de texto")
    # Escritura
    with open(ruta, encoding='utf-8', mode='w') as f:
        f.write("Hola\nsoy\nla\nchuleta\nde\nPython")
        f.writelines(['\nSuerte', '\ncon', '\nel', '\nexamen.'])
        
    print("\n-> Lectura")
    with open(ruta, encoding='utf-8', mode='r') as f:
        contenido = f.read()
        print(contenido)
        
    print("\n-> Lectura línea a línea con readline")
    with open(ruta, encoding='utf-8', mode='r') as f:
        contenido = f.readline()
        while contenido:
            print(contenido, end='')
            contenido = f.readline()
        
    print("\n\n-> Lectura línea a línea con readlines")
    with open(ruta, encoding='utf-8', mode='r') as f:
        contenido = f.readlines()
        print(contenido)
        
    import csv
    print("\nFichero CSV")
    ruta = 'Ejemplo.csv'
    # Escritura
    with open(ruta, encoding='utf-8', mode='w', newline='') as f:
        escritor = csv.writer(f)
        escritor.writerow(['Nombre', 'Edad', 'Sexo'])
        escritor.writerow(['Manuel', 22, 'Hombre'])
        escritor.writerow(['Lucia', 24, 'Mujer'])
        escritor.writerows([['Patri', 19, 'Mujer'], ['Tina', 10, 'Gata']])
    
    print("\n-> Lectura")
    with open(ruta, encoding='utf-8', mode='r') as f:
        lector = csv.reader(f)
        next(lector) # Saltar la cabecera
        for fila in lector:
            print(fila) # Devuelve una lista
    
    print("\n-> Lectura con diccionario")
    with open(ruta, encoding='utf-8', mode='r') as f:
        lector = csv.DictReader(f)
        for fila in lector:
            print(fila) # Devuelve un diccionario
    
def main():
    print("Teoría de Python")
    cadenas()
    variables()
    listas()
    tuplas()
    conjuntos()
    diccionarios()
    cositas()
    ficheros()
     
if __name__ == "__main__":
    main()