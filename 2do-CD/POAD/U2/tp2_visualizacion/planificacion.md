# Planificación del Proyecto: Global Dev Analytics (Pobreza vs. Esperanza de Vida)

Proyecto integrador para la cátedra **Programación Orientada al Análisis de Datos** (Tecnicatura Superior en Ciencia de Datos e Inteligencia Artificial).

---

## 1. Alcance y Objetivos Técnicos

El propósito central es construir una solución analítica completa que procese datos socioeconómicos reales, aplique principios rigurosos de visualización cuantitativa y despliegue un cuadro de mando interactivo para la toma de decisiones.

### Rúbricas de Evaluación (Programación)
* **Pandas (25%)**: Ingesta de 2 fuentes (`.csv`), limpieza, tipado estricto, concatenación/unión relacional y cálculo de indicadores derivados.
* **Matplotlib (25%)**: 1 gráfico estático enfocado en comparación/ranking, optimizado según principios de Tufte (arranque en cero, ordenado, sin ruido visual).
* **Seaborn (25%)**: 1 gráfico estático orientado al análisis de distribución o correlación multivariante (curva de ajuste/regresión o dispersión regional).
* **Plotly + Dash (25%)**: Dashboard interactivo (`app.py`) con controles de filtrado (selectores/sliders), tarjetas de KPIs y visualización dinámica exploratoria.

---

## 2. Arquitectura del Repositorio

Estructura modular optimizada para desarrollo en Antigravity / WSL, sin carpetas auxiliares innecesarias:

```text
global_dev_analytics/
├── data/
│   ├── pobreza.csv          # Distribución por umbrales de pobreza (Banco Mundial)
│   └── esperanza_vida.csv   # Esperanza de vida al nacer (ONU / HMD)
├── src/
│   ├── __init__.py
│   ├── motor_datos.py       # Tubería ETL con Pandas (carga, limpieza, merge, métricas)
│   └── graficos.py          # Generadores de figuras para Matplotlib, Seaborn y Plotly
├── .gitignore               # Exclusión de entornos virtuales, cachés y datos pesados
├── app.py                   # Layout y callbacks del dashboard en Dash
├── requirements.txt         # Dependencias congeladas del entorno
└── README.md                # Ficha técnica, arquitectura e instrucciones de ejecución