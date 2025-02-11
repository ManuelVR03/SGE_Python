import csv
import time

def leer_preguntas():
    preguntas = {}
    with open('preguntas_trivial.csv', encoding='utf-8', mode='r') as f:
        lector = csv.DictReader(f)
        for linea in lector:
            categoria = linea['Categoría']
            linea['Opciones'] = linea['Opciones'].split(',')
            linea['Puntos'] = int(linea['Puntos'])
            del linea['Categoría']
            if categoria not in preguntas:
                preguntas[categoria] = []
            preguntas[categoria].append(linea)
    return preguntas

def trivial(pregunta, puntos):
    print(pregunta['Pregunta'])
    print()
    for i in range(4):
        print(f"Opción {i+1}: {pregunta['Opciones'][i]}")
    print()
    inicio = time.time()
    respuesta = int(input("Introduce tu respuesta: "))-1
    respondido = time.time() - inicio
    print()
    if respondido > 6:
        print("Se ha acabado el tiempo")
        print("La respuesta correcta es: ", pregunta['Respuesta'])
        return puntos
    elif pregunta['Opciones'][respuesta] == pregunta['Respuesta']:
        print("Respuesta correcta")
        puntos += pregunta['Puntos']
    else:
        print("Respuesta incorrecta")
        print("La respuesta correcta es: ", pregunta['Respuesta'])
    return puntos

def main():
    preguntas = leer_preguntas()
    puntos = 0
    salir = 's'
    dificultades = ['fácil', 'medio', 'difícil']
                    
    print("Bienvenidos al Trivial de Python")
    print()
    
    while salir != 'n':
        print("Dificultades: ")
        for i in range(3):
            print(f'{i+1}. {dificultades[i]}')
        dificultad = int(input("Elige una dificultad: "))-1
        while dificultad < 0 or dificultad > 2:  
            print("Dificultad no válida")
            dificultad = int(input("Elige una dificultad: "))-1
        print()
        
        print("Categorías: ")
        for i, c in enumerate(preguntas.keys()):
            print(f'{i+1}. {c}')
        categoria = int(input("Elige una categoría: "))-1
        while categoria < 0 or categoria > 5:
            print("Categoría no válida")
            categoria = int(input("Elige una categoría: "))-1
        categoria = list(preguntas.keys())[categoria]
        print()
        
        puntos = trivial(preguntas[categoria][dificultad], puntos)
        print()
        
        salir = input("¿Quieres seguir jugando? (s/n): ")
        print()
      
    print()  
    print("Fin del juego")
    print(f"Has conseguido {puntos} puntos")
    
if __name__ == "__main__":
    main()