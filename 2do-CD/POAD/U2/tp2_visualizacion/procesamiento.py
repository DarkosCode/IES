"""
- Carga de 2 fuentes de datos CSV independientes.
- Limpieza y descarte de registros no válidos (agrupaciones regionales sin código ISO).
- Normalización de nombres de columnas a formato uniforme.
- Tipificación estricta de variables (enteros, flotantes, cadenas).
- Cálculo de indicadores derivados (población relevada y % de pobreza extrema).
- Unión relacional (merge) en un único DataFrame unificado.
"""

import pandas as pd

def cargar_esperanza_vida(ruta_archivo: str = "life-expectancy.csv") -> pd.DataFrame:
    """
    Carga y limpia el dataset de esperanza de vida al nacer.
    Descarta entidades supranacionales o agregados regionales sin código ISO de 3 letras.
    """
    df = pd.read_csv(ruta_archivo)
    
    # 1. Renombrar columnas para facilitar el manejo
    df = df.rename(columns={
        "Entity": "pais",
        "Code": "codigo",
        "Year": "anio",
        "Life expectancy": "esperanza_vida"
    })
    
    # 2. Descartar filas donde el código de país sea nulo (son agrupaciones como 'World', 'Africa', etc.)
    df = df.dropna(subset=["codigo"]).copy()
    
    # 3. Tipado explícito
    df["anio"] = df["anio"].astype(int)
    df["esperanza_vida"] = df["esperanza_vida"].astype(float)
    df["codigo"] = df["codigo"].astype(str).str.strip()
    df["pais"] = df["pais"].astype(str).str.strip()
    
    return df[["codigo", "pais", "anio", "esperanza_vida"]]


def cargar_pobreza(ruta_archivo: str = "pobreza.csv") -> pd.DataFrame:
    """
    Carga y limpia el dataset de distribución poblacional por umbrales de ingresos diarios.
    Calcula la población total relevada y la tasa porcentual de pobreza extrema (< $3 al día).
    """
    df = pd.read_csv(ruta_archivo)
    
    # 1. Renombrar columnas a nombres claros en español
    df = df.rename(columns={
        "Entity": "pais",
        "Code": "codigo",
        "Year": "anio",
        "Above $10 a day": "ingreso_alto_mas_10",
        "$8.30-$10 a day": "ingreso_medio_8_10",
        "$4.20-$8.30 a day": "ingreso_medio_4_8",
        "$3-$4.20 a day": "pobreza_moderada_3_4",
        "Below $3 a day": "pobreza_extrema_menos_3"
    })
    
    # 2. Descartar registros sin código de país
    df = df.dropna(subset=["codigo"]).copy()
    
    # 3. Tipado explícito de columnas numéricas
    columnas_poblacion = [
        "ingreso_alto_mas_10",
        "ingreso_medio_8_10",
        "ingreso_medio_4_8",
        "pobreza_moderada_3_4",
        "pobreza_extrema_menos_3"
    ]
    
    df["anio"] = df["anio"].astype(int)
    df["codigo"] = df["codigo"].astype(str).str.strip()
    for col in columnas_poblacion:
        df[col] = df[col].astype(int)
        
    # 4. Cálculo de indicadores derivados:
    # - Población total analizada (suma de todos los rangos)
    df["poblacion_total"] = df[columnas_poblacion].sum(axis=1)
    
    # - Tasa de pobreza extrema (%)
    df["pct_pobreza_extrema"] = (df["pobreza_extrema_menos_3"] / df["poblacion_total"]) * 100
    
    # - Tasa de ingresos altos (%)
    df["pct_ingreso_alto"] = (df["ingreso_alto_mas_10"] / df["poblacion_total"]) * 100

    columnas_finales = [
        "codigo", "anio", "poblacion_total",
        "pobreza_extrema_menos_3", "pct_pobreza_extrema", "pct_ingreso_alto"
    ]
    return df[columnas_finales]


def preparar_datos() -> pd.DataFrame:
    """
    Función principal de integración ETL:
    Ejecuta la ingesta individual y realiza la unión relacional (merge)
    por código de país y año.
    """
    df_vida = cargar_esperanza_vida()
    df_pob = cargar_pobreza()
    
    # Unión relacional interna (inner join) por clave compuesta (codigo + anio)
    df_unificado = pd.merge(df_vida, df_pob, on=["codigo", "anio"], how="inner")
    
    # Ordenamos cronológicamente y por país
    df_unificado = df_unificado.sort_values(by=["anio", "pais"]).reset_index(drop=True)
    
    return df_unificado


if __name__ == "__main__":
    # Prueba rápida unitaria del módulo
    datos = preparar_datos()
    #VISTA PREVIA DEL DATAFRAME PROCESADO
    print(f"Registros totales unidos: {len(datos)}")
    print(f"Columnas resultantes: {datos.columns.tolist()}")
    print("\nPrimeras 5 filas:")
    print(datos[["pais", "codigo", "anio", "esperanza_vida", "pct_pobreza_extrema"]].head())
