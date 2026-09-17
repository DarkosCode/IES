# Trabajo Práctico N° 2: Visualización de Datos

* **Institución:** Instituto de Educación Superior Manuel Belgrano
* **Carrera:** Tecnicatura Superior en Ciencia de Datos e Inteligencia Artificial
* **Espacio Curricular:** Programación Orientada al Análisis de Datos (POAD)
* **Docente:** Juan Caballero Gallar
* **Ciclo Lectivo:** 2026

---

## 1. Temática y Alcance del Proyecto

El proyecto analiza la relación socioeconómica global entre los **niveles de pobreza monetaria diaria** y la **esperanza de vida al nacer**, integrando datos provenientes de dos fuentes internacionales de referencia:
1. **Banco Mundial:** Distribución poblacional por tramos de ingresos diarios (`pobreza.csv`).
2. **Naciones Unidas / Our World in Data:** Esperanza de vida al nacer por país y año (`life-expectancy.csv`).

---

## 2. Diagrama de Entidad-Relación (DER) y Diccionario de Datos

Para responder a la consigna de modelado y esquema relacional del informe:

### Diagrama Lógico / Relacional
```text
+-----------------------+              +------------------------------+
|   ESPERANZA DE VIDA   |              |           POBREZA            |
+-----------------------+              +------------------------------+
| * codigo (ISO-3) [PK] |              | * codigo (ISO-3) [PK]        |
| * anio           [PK] |              | * anio           [PK]        |
|   pais                |              |   pais                       |
|   esperanza_vida      |              |   ingreso_alto_mas_10        |
+-----------+-----------+              |   ingreso_medio_8_10         |
            |                          |   ingreso_medio_4_8          |
            |         1:1 (por año)    |   pobreza_moderada_3_4       |
            +------------ MERGE -------+   pobreza_extrema_menos_3    |
                                       +--------------+---------------+
                                                      |
                                                      v
                                       +------------------------------+
                                       |      DATASET UNIFICADO       |
                                       +------------------------------+
                                       | * codigo (ISO-3)     (str)   |
                                       | * anio               (int)   |
                                       |   pais               (str)   |
                                       |   esperanza_vida     (float) |
                                       |   poblacion_total    (int)   |
                                       |   pct_pobreza_ext    (float) |
                                       |   pct_ingreso_alto   (float) |
                                       +------------------------------+
```

### Diccionario de Datos del DataFrame Procesado

| Columna | Tipo de Dato | Descripción |
| :--- | :--- | :--- |
| `codigo` | `str` (3 caracteres) | Código ISO-3 identificador único del país (ej. `ARG`, `JPN`, `ZWE`). |
| `pais` | `str` | Nombre de la entidad nacional. |
| `anio` | `int` | Año calendario de relevamiento (2010 - 2023). |
| `esperanza_vida` | `float` | Años promedio de vida al nacer calculados por la ONU. |
| `poblacion_total` | `int` | Población total sumada a través de todos los umbrales de ingresos relevados. |
| `pobreza_extrema_menos_3` | `int` | Cantidad de personas que subsisten con menos de $3 USD al día. |
| `pct_pobreza_extrema` | `float` | Métrica derivada: porcentaje de personas en pobreza extrema sobre el total relevado. |
| `pct_ingreso_alto` | `float` | Métrica derivada: porcentaje de personas con ingresos mayores a $10 USD diarios. |

---

## 3. Estructura Modular del Proyecto

El código está estructurado con el principio de responsabilidad única para maximizar la legibilidad y facilitar su comprensión:

```text
tp2_visualizacion/
├── life-expectancy.csv     # Fuente 1: Datos de esperanza de vida
├── pobreza.csv             # Fuente 2: Datos de umbrales de pobreza
├── procesamiento.py        # [PANDAS 25%] Ingesta, limpieza, normalización, cálculo y merge
├── graficos.py             # [VISUALIZACIÓN 75%] Funciones de Matplotlib, Seaborn y Plotly
├── main.py                 # [ORQUESTADOR] Script de ejecución principal
├── requirements.txt        # Dependencias congeladas del entorno
├── .gitignore              # Reglas de exclusión para Git (mantiene los CSVs incluidos)
└── salidas/                # Carpeta generada automáticamente
    ├── grafico_1_matplotlib.png   # Gráfico 1: Ranking comparativo Top 10 vs Bottom 10
    ├── grafico_2_seaborn.png      # Gráfico 2: Dispersión con regresión lineal
    └── grafico_3_plotly.html      # Gráfico 3: Visualización interactiva con tooltips
```

---

## 4. Requisitos e Instalación

Las dependencias requeridas son estándar en ciencia de datos:
* `pandas >= 2.0.0`
* `matplotlib >= 3.7.0`
* `seaborn >= 0.12.0`
* `plotly >= 5.15.0`

Para instalarlas en un entorno nuevo:
```bash
pip install -r requirements.txt
```

---

## 5. Instrucciones de Ejecución

Para ejecutar el pipeline completo y generar todas las visualizaciones:

### Desde Windows (PowerShell o CMD):
```powershell
python main.py
```

### Desde Linux / WSL (con el entorno virtual activo):
```bash
python3 main.py
```

Al finalizar la ejecución, los archivos de imagen y el interactivo estarán disponibles en la carpeta `salidas/`.

---

## 6. Justificación y Explicación de las Visualizaciones

### 1. Matplotlib (`grafico_1_matplotlib.png`)
* **Consigna:** Comparación / Ranking cuantitativo.
* **Decisión de diseño:** Gráfico de barras horizontales ordenado de forma ascendente, contrastando los 10 países con mayor esperanza de vida y los 10 con menor esperanza de vida.
* **Principios aplicados:**
  * El eje horizontal comienza en 0 para mantener la integridad proporcional (evita exagerar diferencias artificialmente, según los principios de Edward Tufte).
  * Se incluye la línea vertical de referencia con el promedio del grupo analizado (76.7 años).
  * Uso de paleta de colores semántica (azul para longevidad sobre el promedio, coral/rojo para países rezagados).
  * Eliminación de bordes o espinas superiores y derechas para reducir la relación tinta-datos (*data-ink ratio*).

### 2. Seaborn (`grafico_2_seaborn.png`)
* **Consigna:** Correlación y distribución multivariante.
* **Decisión de diseño:** Gráfico de dispersión con ajuste de regresión lineal (`regplot`) entre el porcentaje de población en pobreza extrema ($< \$3$ USD diarios) y la esperanza de vida al nacer.
* **Hallazgos:** Se observa una marcada correlación negativa ($r = -0.63$ a $-0.75$ según el período). Los países con más del 40% de su población en pobreza extrema presentan esperanzas de vida que difícilmente superan los 65 años, mientras que aquellos con pobreza extrema casi nula superan sistemáticamente los 80 años.

### 3. Plotly Express (`grafico_3_plotly.html`)
* **Consigna:** Visualización interactiva.
* **Decisión de diseño:** Diagrama de dispersión interactivo exportado en HTML autónomo.
* **Interactividad:**
  * Al posar el cursor sobre cualquier burbuja, se despliega un cuadro con el nombre del país, el código ISO, el año analizado, la tasa de pobreza extrema y la esperanza de vida precisa.
  * Permite zoom, paneo y aislamiento de puntos directamente desde el navegador web.
