"""
PROGRAMA PRINCIPAL: TRABAJO PRÁCTICO N° 2 (POAD)
================================================
Cátedra: Programación Orientada al Análisis de Datos
Carrera: Tecnicatura Superior en Ciencia de Datos e IA - IES Manuel Belgrano
Temática: Pobreza vs. Esperanza de Vida (Desarrollo Socioeconómico Global)

Este script ejecuta el flujo completo de análisis:
1. Ingesta, limpieza y transformación con Pandas (procesamiento.py)
2. Generación y exportación de gráficos con Matplotlib, Seaborn y Plotly (graficos.py)
"""

from procesamiento import preparar_datos
from graficos import (
    crear_grafico_matplotlib,
    crear_grafico_seaborn,
    crear_grafico_plotly
)


def main():
    print("=" * 65)
    print("  TRABAJO PRÁCTICO N° 2: VISUALIZACIÓN DE DATOS (POAD)")
    print("=" * 65)

    # Paso 1: Ingesta y limpieza de datos (Consigna Pandas)
    print("\n[1/4] Procesando fuentes de datos con Pandas...")
    df = preparar_datos()
    print(f"      [OK] Datos integrados exitosamente: {len(df)} registros totales.")
    print(f"      [OK] Rango temporal cubierto: {df['anio'].min()} a {df['anio'].max()}.")

    # Paso 2: Gráficos de visualización (Consignas Matplotlib, Seaborn y Plotly)
    print("\n[2/4] Generando gráfico de comparación (Matplotlib)...")
    crear_grafico_matplotlib(df, anio_referencia=2019)

    print("\n[3/4] Generando gráfico de correlación con regresión (Seaborn)...")
    crear_grafico_seaborn(df, anio_referencia=2019)

    print("\n[4/4] Generando gráfico interactivo exploratorio (Plotly Express)...")
    crear_grafico_plotly(df, anio_referencia=2019)

    print("\n" + "=" * 65)
    print("  ¡PROCESO COMPLETADO EXITOSAMENTE!")
    print("  Las visualizaciones se encuentran en la carpeta 'salidas/':")
    print("    - grafico_1_matplotlib.png (Para el informe PDF)")
    print("    - grafico_2_seaborn.png    (Para el informe PDF)")
    print("    - grafico_3_plotly.html    (Abrir en navegador para interactuar y capturar)")
    print("=" * 65)


if __name__ == "__main__":
    main()
