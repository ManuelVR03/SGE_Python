import time

def trivial(categoriaN, dificultadN, preguntas):
    preguntas_categoria = preguntas[categoriaN]
    if dificultadN == 'fácil':
        preguntas_categoria = preguntas_categoria[0]
    elif dificultadN == 'medio':
        preguntas_categoria = preguntas_categoria[1]
    else:
        preguntas_categoria = preguntas_categoria[2]
    print("Primera pregunta: ")
    print(preguntas_categoria[0])
    print("Opciones: ")
    for i in range(4):
        print(f"Opción {i+1}: {preguntas_categoria[1][i]}")
    respuesta = input("Introduce tu respuesta: ")
    if respuesta == preguntas_categoria[2]:
        print("Respuesta correcta")
    else:
        print("Respuesta incorrecta")
        print("La respuesta correcta es: ", preguntas_categoria[2])

def main():
    preguntas = {
    'matemáticas': [
        ('¿Cuánto es 5 + 3?', ['6', '7', '8', '9'], '8', 'fácil'),
        ('¿Cuál es la raíz cuadrada de 16?', ['10', '11', '4', '12'], '4', 'medio'),
        ('Cual es el resultado de la expresion: sen(90º)', ['180º', '0', '90', '1'], '1', 'difícil')
    ],
    'videojuegos': [
        ('¿Quién es el hermano de Mario en la saga de videojuegos de Super Mario?', ['Luigi', 'Mario', 'Wario', 'Bowser'], 'Luigi', 'fácil'),
        ('¿Qué bloque en Minecraft se utiliza para hacer un portal al Nether?', ['Diamante', 'Obsidiana', 'Oro', 'Ladrillo de piedra'], 'Obsidiana', 'medio'),
        ('¿Cuál es el nombre completo del protagonista de "The Legend of Zelda"?', ['Zelda', 'Link', 'Ganon', 'Epona'], 'Link', 'difícil')
    ],
    'literatura': [
        ('¿Quién escribió "Cien años de soledad"?', ['Gabriel García Márquez', 'Mario Vargas Llosa', 'Jorge Luis Borges', 'Isabel Allende'], 'Gabriel García Márquez', 'fácil'),
        ('¿Quien escribio el lazarillo de Tormes?', ['Anonimo', 'Sherlock Holmes', 'Philip Marlowe', 'Sam Spade'], 'Anonimo', 'medio'),
        ('¿Quién escribió la obra Romeo y Julieta?', ['William Shakespeare', 'Charles Dickens', 'Jane Austen', 'Edgar Allan Poe'], 'William Shakespeare', 'difícil')
    ],
    'mitología': [
        ('¿Quién es el dios del trueno en la mitología nórdica?', ['Loki', 'Thor', 'Odin', 'Freyr'], 'Thor', 'fácil'),
        ('¿Cuál es el equivalente griego del dios romano Júpiter?', ['Ares', 'Zeus', 'Hades', 'Poseidón'], 'Zeus', 'medio'),
        ('¿Qué función tenía Caronte en la mitología griega?', ['dios de la guerra', 'dios del vino', 'barquero que transportaba las almas al inframundo', 'Era el guardián del monte Olimpo'], 'barquero que transportaba las almas al inframundo', 'difícil')
    ],
    'música': [
        ('¿Qué género canta Bad Bunny?', ['Reguetón', 'Rock', 'Jazz', 'Blues'], 'Reguetón', 'fácil'),
        ('¿Qué estilo es famoso por su ritmo bailable y letras en español?', ['Salsa', 'Reguetón', 'Rock', 'Hip Hop'], 'Reguetón', 'medio'),
        ('¿Qué género es conocido por artistas como Billie Eilish?', ['Trap', 'Pop', 'Indie', 'R&B'], 'Indie', 'difícil')
    ],
    'tecnología': [
        ('¿Qué significa la sigla "CPU"?', ['Central Processing Unit', 'Computer Power Unit', 'Central Program Unit', 'Control Processing Unit'], 'Central Processing Unit', 'fácil'),
        ('¿En qué año se lanzó el primer iPhone?', ['2005', '2007', '2009', '2011'], '2007', 'medio'),
        ('¿Quién es el fundador de Microsoft?', ['Steve Jobs', 'Bill Gates', 'Mark Zuckerberg', 'Elon Musk'], 'Bill Gates', 'difícil')
    ]
    }
    print("Bienvenidos al Trivial de Python")
    for i in range(3):
        dificultad = input("Elige una dificultad (fácil, medio, difícil): ")
        while dificultad not in ['fácil', 'medio', 'difícil']:  
            print("Dificultad no válida")
            dificultad = input("Elige una dificultad (fácil, medio, difícil): ")
        categoria = input("Elige una categoría (matemáticas, videojuegos, literatura, mitología, música, tecnología): ")
        while categoria not in preguntas:
            print("Categoría no válida")
            categoria = input("Elige una categoría (matemáticas, videojuegos, literatura, mitología, música, tecnología): ")
        trivial(categoria, dificultad, preguntas)    
    
    
if __name__ == "__main__":
    main()