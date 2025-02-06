import pandas as pd
import random

def cargar_preguntas(csv_path):
    """Carga las preguntas desde un archivo CSV."""
    df = pd.read_csv(csv_path, encoding="utf-8")
    return df

def seleccionar_pregunta(df, categoria, nivel):
    """Selecciona una pregunta aleatoria de la categoría y nivel dados."""
    preguntas_filtradas = df[(df['Categoría'] == categoria) & (df['Nivel'] == nivel)]
    if preguntas_filtradas.empty:
        return None
    return preguntas_filtradas.sample(n=1).iloc[0]

def jugar(csv_path):
    """Función principal del juego."""
    df = cargar_preguntas(csv_path)
    puntuacion = 0
    
    while True:
        print("\nCategorías disponibles:")
        categorias = df['Categoría'].unique()
        for i, cat in enumerate(categorias, 1):
            print(f"{i}. {cat}")
        
        try:
            cat_index = int(input("Elige una categoría (número): ")) - 1
            if cat_index < 0 or cat_index >= len(categorias):
                print("Selección no válida.")
                continue
            categoria = categorias[cat_index]
        except ValueError:
            print("Entrada no válida.")
            continue
        
        niveles = ['fácil', 'medio', 'difícil']
        print("\nNiveles de dificultad:")
        for i, nivel in enumerate(niveles, 1):
            print(f"{i}. {nivel}")
        
        try:
            nivel_index = int(input("Elige un nivel (número): ")) - 1
            if nivel_index < 0 or nivel_index >= len(niveles):
                print("Selección no válida.")
                continue
            nivel = niveles[nivel_index]
        except ValueError:
            print("Entrada no válida.")
            continue
        
        pregunta = seleccionar_pregunta(df, categoria, nivel)
        if pregunta is None:
            print("No hay preguntas disponibles para esta selección.")
            continue
        
        print(f"\nPregunta: {pregunta['Pregunta']}")
        opciones = pregunta['Opciones'].split(', ')
        random.shuffle(opciones)
        
        for i, opcion in enumerate(opciones, 1):
            print(f"{i}. {opcion}")
        
        try:
            respuesta_index = int(input("Elige tu respuesta (número): ")) - 1
            if respuesta_index < 0 or respuesta_index >= len(opciones):
                print("Selección no válida.")
                continue
        except ValueError:
            print("Entrada no válida.")
            continue
        
        if opciones[respuesta_index] == pregunta['Respuesta']:
            print("¡Correcto!")
            puntuacion += pregunta['Puntos']
        else:
            print(f"Incorrecto. La respuesta correcta era: {pregunta['Respuesta']}")
        
        print(f"Puntuación actual: {puntuacion}")
        
        continuar = input("¿Quieres seguir jugando? (s/n): ").strip().lower()
        if continuar != 's':
            break
    
    print(f"\nJuego terminado. Puntuación final: {puntuacion}")

# Ejecutar el juego
if __name__ == "__main__":
    csv_path = "preguntas_trivial.csv"  # Asegurar que el archivo esté en el mismo directorio
    jugar(csv_path)
