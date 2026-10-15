from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
SEMILLA = 7
# Acerca del dataset: https://es.wikipedia.org/wiki/Conjunto_de_datos_flor_iris
flores_iris = load_iris()
x, y = flores_iris.data, flores_iris.target
# Regla del 80/20 para separar la información para entrenamiento y evaluación.
x_entrenamiento, x_prueba, y_entrenamiento, y_prueba = train_test_split(x, y, test_size=0.2, random_state=SEMILLA)
# Un clasificador se especializa en y cualitativo.
# Este clasificador se llama borque porque es un conjunto de árboles de decisión.
# Se llama aleatorio porque elige al azar por dónde empezar y lo que muestrear.
modelo = RandomForestClassifier(random_state=SEMILLA)
# Aprendizaje de la IA
modelo.fit(x_entrenamiento, y_entrenamiento)
# Pronóstico hecho por la IA
y_prediccion = modelo.predict(x_prueba)
# Supervisión del aprendizaje
certeza = accuracy_score(y_prueba, y_prediccion)
print(f"Certeza: {certeza * 100:.2f}%")
print("Reporte de clasificación")
print(classification_report(y_prueba, y_prediccion, target_names=flores_iris.target_names))