"""
MÓDULO 2: VISUALIZACIÓN DE DATOS
================================
Trabajo Práctico N° 2 - Programación Orientada al Análisis de Datos (POAD)
Cátedra: Tecnicatura Superior en Ciencia de Datos e Inteligencia Artificial

Este módulo cumple con las consignas de visualización:
- Matplotlib (25%): Gráfico de barras horizontal ordenado (ranking comparativo Top 10 vs Bottom 10).
- Seaborn (25%): Gráfico de dispersión con línea de tendencia/regresión (correlación pobreza vs esperanza de vida).
- Plotly Express (25%): Gráfico interactivo con tooltips detallados, guardado en HTML.
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Directorio de salida para guardar las imágenes y el HTML
CARPETA_SALIDAS = "salidas"


def asegurar_carpeta_salidas():
    """Crea la carpeta de salidas si no existe."""
    if not os.path.exists(CARPETA_SALIDAS):
        os.makedirs(CARPETA_SALIDAS)


def crear_grafico_matplotlib(df: pd.DataFrame, anio_referencia: int = 2019):
    """
    CONSIGNA MATPLOTLIB: Gráfico de comparación / ranking.
    Genera un gráfico de barras horizontales ordenado comparando los 10 países
    con mayor esperanza de vida y los 10 países con menor esperanza de vida.
    """
    asegurar_carpeta_salidas()
    
    # Filtramos por el año de referencia seleccionado
    df_anio = df[df["anio"] == anio_referencia].copy()
    
    # Obtenemos los 10 países con mayor y menor esperanza de vida
    top_10 = df_anio.sort_values(by="esperanza_vida", ascending=False).head(10)
    bottom_10 = df_anio.sort_values(by="esperanza_vida", ascending=True).head(10)
    
    # Combinamos y ordenamos ascendentemente para que las barras se dibujen de abajo hacia arriba
    df_ranking = pd.concat([bottom_10, top_10]).sort_values(by="esperanza_vida", ascending=True)
    
    # Asignamos colores: azul para los más altos, coral para los más bajos
    promedio_global = df_anio["esperanza_vida"].mean()
    colores = ["#e74c3c" if v < promedio_global else "#2980b9" for v in df_ranking["esperanza_vida"]]
    
    # Configuración de la figura
    fig, ax = plt.subplots(figsize=(10, 8))
    barras = ax.barh(df_ranking["pais"], df_ranking["esperanza_vida"], color=colores, edgecolor="none", height=0.7)
    
    # Etiquetas de datos en cada barra
    ax.bar_label(barras, fmt="%.1f años", padding=5, fontsize=9, color="#2c3e50", weight="bold")
    
    # Línea de referencia del promedio
    ax.axvline(promedio_global, color="#7f8c8d", linestyle="--", linewidth=1.2, label=f"Promedio del grupo ({promedio_global:.1f} años)")
    
    # Personalización de títulos y ejes
    ax.set_title(f"Ranking de Esperanza de Vida al Nacer ({anio_referencia})\nComparativa: 10 países con mayor vs. menor longevidad", fontsize=13, weight="bold", pad=15)
    ax.set_xlabel("Esperanza de vida (años)", fontsize=11, labelpad=10)
    ax.set_xlim(0, 100)  # Inicio en 0 para no distorsionar la proporción visual (principio de Tufte)
    ax.grid(axis="x", linestyle=":", alpha=0.6)
    ax.legend(loc="lower right")
    
    # Limpieza de espinas (bordes superfluos)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    
    plt.tight_layout()
    ruta_salida = os.path.join(CARPETA_SALIDAS, "grafico_1_matplotlib.png")
    fig.savefig(ruta_salida, dpi=300)
    plt.close(fig)
    print(f"[Matplotlib] Gráfico guardado exitosamente en: {ruta_salida}")


def crear_grafico_seaborn(df: pd.DataFrame, anio_referencia: int = 2019):
    """
    CONSIGNA SEABORN: Gráfico de correlación / distribución.
    Genera un gráfico de dispersión con línea de regresión para evidenciar
    la relación inversa entre la pobreza extrema y la esperanza de vida.
    """
    asegurar_carpeta_salidas()
    
    df_anio = df[df["anio"] == anio_referencia].copy()
    
    # Configuración del estilo visual con Seaborn
    sns.set_theme(style="whitegrid", font="sans-serif")
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Gráfico de dispersión con regresión lineal
    sns.regplot(
        data=df_anio,
        x="pct_pobreza_extrema",
        y="esperanza_vida",
        scatter_kws={"alpha": 0.7, "color": "#2c3e50", "s": 60},
        line_kws={"color": "#e74c3c", "linewidth": 2, "label": "Tendencia lineal"},
        ax=ax
    )
    
    # Anotación explicativa de la correlación
    correlacion = df_anio["pct_pobreza_extrema"].corr(df_anio["esperanza_vida"])
    texto_resumen = f"Correlación (Pearson): {correlacion:.2f}\n(A mayor pobreza extrema, menor esperanza de vida)"
    ax.text(
        0.95, 0.90, texto_resumen,
        transform=ax.transAxes,
        fontsize=10,
        verticalalignment="top",
        horizontalalignment="right",
        bbox=dict(boxstyle="round,pad=0.5", facecolor="#ecf0f1", edgecolor="#bdc3c7", alpha=0.9)
    )
    
    # Títulos y etiquetas de los ejes
    ax.set_title(f"Relación entre Pobreza Extrema y Esperanza de Vida ({anio_referencia})", fontsize=13, weight="bold", pad=15)
    ax.set_xlabel("Población en Pobreza Extrema (< $3 USD diarios) [%]", fontsize=11, labelpad=10)
    ax.set_ylabel("Esperanza de vida (años)", fontsize=11, labelpad=10)
    ax.set_ylim(50, 90)
    ax.legend(loc="lower left")
    
    plt.tight_layout()
    ruta_salida = os.path.join(CARPETA_SALIDAS, "grafico_2_seaborn.png")
    fig.savefig(ruta_salida, dpi=300)
    plt.close(fig)
    print(f"[Seaborn] Gráfico guardado exitosamente en: {ruta_salida}")


def crear_grafico_plotly(df: pd.DataFrame, anio_referencia: int = 2019):
    """
    CONSIGNA PLOTLY: Gráfico interactivo con Plotly Express.
    Genera un scatter plot interactivo donde el usuario puede pasar el cursor
    sobre cada país para inspeccionar los valores exactos.
    Se guarda como archivo HTML autónomo para visualización en el navegador.
    """
    asegurar_carpeta_salidas()
    
    df_anio = df[df["anio"] == anio_referencia].copy()
    
    # Creación del gráfico interactivo con Plotly Express
    fig = px.scatter(
        df_anio,
        x="pct_pobreza_extrema",
        y="esperanza_vida",
        color="esperanza_vida",
        color_continuous_scale="Viridis",
        hover_name="pais",
        hover_data={
            "pct_pobreza_extrema": ":.2f",
            "esperanza_vida": ":.1f",
            "poblacion_total": ":,",
            "codigo": True
        },
        labels={
            "pct_pobreza_extrema": "% Pobreza Extrema (< $3 al día)",
            "esperanza_vida": "Esperanza de Vida (Años)",
            "poblacion_total": "Población Relevada",
            "codigo": "Código ISO"
        },
        title=f"Explorador Interactivo: Pobreza vs. Esperanza de Vida ({anio_referencia})"
    )
    
    # Personalización del diseño (layout)
    fig.update_layout(
        template="plotly_white",
        title_font_size=16,
        xaxis_title="% Población en Pobreza Extrema (< $3 al día)",
        yaxis_title="Esperanza de Vida (Años)",
        hoverlabel=dict(bgcolor="white", font_size=12)
    )
    
    ruta_salida = os.path.join(CARPETA_SALIDAS, "grafico_3_plotly.html")
    fig.write_html(ruta_salida)
    print(f"[Plotly] Gráfico interactivo guardado exitosamente en: {ruta_salida}")


if __name__ == "__main__":
    from procesamiento import preparar_datos
    datos = preparar_datos()
    crear_grafico_matplotlib(datos)
    crear_grafico_seaborn(datos)
    crear_grafico_plotly(datos)
