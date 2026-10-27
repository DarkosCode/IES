from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report
SEMILLA = 7
flores_iris = load_iris()
x, y = flores_iris.data, flores_iris.target
# Regla del 80/20 estratificada explícitamente para que no sea solo por muestreo aleatorio.
x_entrenamiento, x_prueba, y_entrenamiento, y_prueba = \
    train_test_split(x, y, test_size=0.2, random_state=SEMILLA, stratify=y)
# Un escalador ajusta media y desviación estándar a la información del entrenamiento.
escalador = StandardScaler()
x_entrenamiento_escalado = escalador.fit_transform(x_entrenamiento)
# fit_transform aprende media y desviación estándar de entrenamiento, transform los espera en la evaluación.
x_prueba_escalado = escalador.transform(x_prueba)
# SVC es un clasificador vectorial. Los vectores conforman un espacio clasificador.
# Su núcleo puede ser lineal, polinómico, gaussiano, sigmoidal o personalizado (con matriz cuadrada).
# Como la función de aceptación de un perceptrón, pero maximiza el margen en vez de contentarse al primer éxito.
modelo = SVC(kernel='rbf', random_state=SEMILLA)
# Aprendizaje supervisado de la IA.
modelo.fit(x_entrenamiento_escalado, y_entrenamiento)
y_prediccion = modelo.predict(x_prueba_escalado)
certeza = accuracy_score(y_prueba, y_prediccion)
print(f"Certeza: {certeza * 100:.2f}%")
print("Reporte de clasificación")
# Este reporte tendrá las flores en cantidades equitativas.
print(classification_report(y_prueba, y_prediccion, target_names=flores_iris.target_names))