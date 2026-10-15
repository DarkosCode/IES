from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import FunctionTransformer
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import root_mean_squared_error, r2_score
SEMILLA = 7
# as_frame=True hace que data sea pandas.DataFrame y target sea pandas.Series
casas = fetch_california_housing(as_frame=True)
x, y = casas.data, casas.target
x_entrenamiento, x_prueba, y_entrenamiento, y_prueba = train_test_split(x, y, test_size=0.2, random_state=SEMILLA)
def crear_caracteristicas(df):
    df_out = df.copy()
    # Qué raro. Abreviaron promedio como Ave en vez de Avg.
    df_out['HabitacionesPorHogar'] = df_out['AveRooms'] / df_out['AveOccup'] # habitaciones / ocupantes
    df_out['DormitoriosPorHabitacion'] = df_out['AveBedrms'] / df_out['AveRooms'] # dormitorios / habitaciones
    return df_out
# Un transformador funcional puede generar campos, filtrar, limpiar, mapear.
generador_features = FunctionTransformer(crear_caracteristicas)
# Una tubería aplica una secuencia de operaciones.
# Esta tubería secuencia el transformador generador, un selector y un regresor.
tuberia = Pipeline([
    ('ingenieria_features', generador_features),
    # Este selector filtra los 8 campos con mejor puntuación regresiva según la hipótesis F de ANOVA.
    # La puntuación aumenta cuando aumenta el estadístico F y es válida si el p-valor es menor a la significancia.
    ('seleccion_features', SelectKBest(score_func=f_regression, k=8)),
    # Un regresor se especializa en y cuantitativo.
    # n_estimators fija la cantidad de árboles en el bosque.
    # n_jobs fija la cantidad de hilos paralelos de procesamiento. -1 para que use todo lo disponible.
    ('regresor', RandomForestRegressor(n_estimators=50, random_state=SEMILLA, n_jobs=-1))
])
# Queremos conservar el as_frame de más arriba.
tuberia.set_output(transform="pandas")
# Aprendizaje supervisado.
tuberia.fit(x_entrenamiento, y_entrenamiento)
y_prediccion = tuberia.predict(x_prueba)
# R^2 es el coeficiente de determinación.
# 100% es aprendizaje perfecto.
# 0% que aprendió pésimo y siempre dice el promedio.
# Porcentaje negativo significa que ni el promedio sabe decir.
r2 = r2_score(y_prueba, y_prediccion)
print(f"Puntaje R2: {r2 * 100:.2f}%")
# RMSE = raíz cuadrada del promedio de las diferencias al cuadrado entre el valor real y el predicho.
rmse = root_mean_squared_error(y_prueba, y_prediccion)
print(f"Raíz del Error Cuadrático Medio (RMSE): ${rmse * 100_000:,.2f} USD")