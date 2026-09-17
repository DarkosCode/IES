# Guía y Resumen del Trabajo Práctico N° 2 (POAD)

* **Institución:** Instituto de Educación Superior Manuel Belgrano
* **Carrera:** Tecnicatura Superior en Ciencia de Datos e Inteligencia Artificial
* **Espacio Curricular:** Programación Orientada al Análisis de Datos (POAD)
* **Docente:** Juan Caballero Gallar
* **Ciclo Lectivo:** 2026
* **Temática:** Global Dev Analytics — Relación entre Pobreza y Esperanza de Vida  

---

## 1. Estructura Implementada en el Repositorio

El proyecto quedó organizado en 3 archivos principales con responsabilidades aisladas:

1. **`procesamiento.py`**: Módulo enfocado 100% en **Pandas** (Rúbrica 25%).
   * Carga `life-expectancy.csv` y `pobreza.csv`.
   * Filtra registros regionales sin código ISO de país.
   * Normaliza nombres de columnas y define tipos numéricos explícitos.
   * Calcula indicadores derivados: `poblacion_total` y `pct_pobreza_extrema`.
   * Realiza la unión relacional (`merge`) por `['codigo', 'anio']`.

2. **`graficos.py`**: Módulo de **Visualizaciones** (Rúbricas 75%).
   * `crear_grafico_matplotlib(df)`: Gráfico de barras horizontales ordenado con ranking Top 10 vs Bottom 10 en longevidad. Guarda `salidas/grafico_1_matplotlib.png`.
   * `crear_grafico_seaborn(df)`: Gráfico de dispersión con línea de tendencia/regresión entre pobreza extrema y esperanza de vida. Guarda `salidas/grafico_2_seaborn.png`.
   * `crear_grafico_plotly(df)`: Gráfico interactivo exploratorio con tooltips enriquecidos. Guarda `salidas/grafico_3_plotly.html`.

3. **`main.py`**: Script orquestador simple (~35 líneas).
   * Corre el flujo completo al ejecutar `python main.py` o `python3 main.py`.

---

## 2. Salidas Generadas

Todos los artefactos visuales se guardan automáticamente en la carpeta `salidas/`:
* **`salidas/grafico_1_matplotlib.png`**: Imagen de alta resolución lista para insertar en el PDF.
* **`salidas/grafico_2_seaborn.png`**: Imagen de alta resolución lista para insertar en el PDF.
* **`salidas/grafico_3_plotly.html`**: Archivo HTML interactivo. Para la entrega, ábrelo en tu navegador favorito (Chrome, Edge, Firefox), pasa el cursor sobre algún país para desplegar el cuadro interactivo y toma una captura de pantalla.

---

## 3. Elementos Listos para Copiar al Informe PDF

La consigna pide responder en el documento con un DER o diagrama que permita ver columnas y tipos de datos, más las capturas:

### A. Esquema Relacional / DER (Copiar al documento)
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

### B. Diccionario de Datos (Copiar al documento)

| Campo | Tipo | Significado |
| :--- | :--- | :--- |
| `codigo` | `str` | Código ISO-3 identificador único del país (ej. `ARG`, `JPN`). |
| `pais` | `str` | Nombre del país. |
| `anio` | `int` | Año calendario (2010 a 2023). |
| `esperanza_vida` | `float` | Años promedio de vida al nacer. |
| `poblacion_total` | `int` | Población total sumada a través de todos los umbrales de ingresos. |
| `pobreza_extrema_menos_3` | `int` | Cantidad de personas con ingresos diarios $< \$3$ USD. |
| `pct_pobreza_extrema` | `float` | Porcentaje de personas en pobreza extrema sobre el total relevado. |
| `pct_ingreso_alto` | `float` | Porcentaje de personas con ingresos $> \$10$ USD al día. |

---

## 4. Guía de Estudio Rápida (Defensa del Trabajo Práctico)

* **¿Por qué descartamos filas sin código ISO?**  
  Porque el dataset original incluye agregados continentales y mundiales (como `"World"`, `"Africa"`, `"Latin America"`) que no tienen código ISO. Si los dejamos, distorsionarían las comparaciones entre países individuales.
* **¿Por qué la unión relacional es un `inner join` por `['codigo', 'anio']`?**  
  Porque garantiza que para cada país y cada año tengamos tanto el dato de pobreza como el dato de esperanza de vida medidos en el mismo período temporal exacto.
* **¿Por qué el eje X de Matplotlib empieza en 0?**  
  Por el principio de integridad gráfica de Edward Tufte: truncar el eje de las barras comenzando en un valor distinto de cero exagera visualmente las diferencias reales entre los países.
* **¿Qué nos indica el gráfico de Seaborn?**  
  Existe una correlación negativa lineal clara ($r = -0.63$). Los países con más del 40% de su población en pobreza extrema presentan esperanzas de vida que difícilmente superan los 65 años, mientras que aquellos con pobreza extrema casi nula superan sistemáticamente los 80 años.
