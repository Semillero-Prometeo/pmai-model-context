from pycocoevalcap.cider.cider import Cider

# 1. Definir los subtítulos de referencia (humanos) para una imagen
# El formato es un diccionario donde la clave es el ID de la imagen
# y el valor es una lista de descripciones.

def evaluar_cider():
    references = {
        0: [
            "un gato sentado en el sofa",
            "un gato gris esta descansando en el sillon",
            "un gato pequeño sobre un mueble"
        ]
    }

    # 2. Definir la hipótesis (subtítulo generado por la IA)
    hypothesis = {
        0: [
            "un gato sentado en el sofa"
        ]
    }

    # 3. Calcular CIDER
    cider_scorer = Cider()
    score, scores = cider_scorer.compute_score(references, hypothesis)

    print(f"Puntuación CIDER promedio: {score:.4f}")
    # print(f"Puntuaciones individuales: {scores}") # Muestra la puntuación por imagen
