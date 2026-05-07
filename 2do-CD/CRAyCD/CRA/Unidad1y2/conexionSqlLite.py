import pandas as pd
import matplotlib.pyplot as plt
import mysql.connector
import sqlite3


conexion = sqlite3.connect("ventas_relacional.db")
cursor = conexion.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS productos (
    id_producto INTEGER PRIMARY KEY,
    nombre TEXT,
    categoria TEXT,
    precio REAL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS ventas (
    id_venta INTEGER PRIMARY KEY,
    id_producto INTEGER,
    cantidad INTEGER,
    fecha TEXT
)
""")

cursor.executemany("""
INSERT INTO productos VALUES (?, ?, ?, ?)
""", [
    (1, "Laptop", "Tecnología", 1500),
    (2, "Mouse", "Accesorios", 20),
    (3, "Teclado", "Accesorios", 45),
    (4, "Monitor", "Tecnología", 300),
    (5, "Auriculares", "Audio", 80)
])

cursor.executemany("""
INSERT INTO ventas VALUES (?, ?, ?, ?)
""", [
    (1, 1, 5, "2024-01-10"),
    (2, 2, 50, "2024-01-11"),
    (3, 3, 30, "2024-01-12"),
    (4, 4, 10, "2024-01-13"),
    (5, 5, 25, "2024-01-14")
])

conexion.commit() #GUARDA DEFINITIVAMENTE LOS CAMBIOS EN LA BD.

query = """
SELECT
    p.nombre,
    p.precio,
    v.cantidad
FROM ventas v
INNER JOIN productos p
ON v.id_producto = p.id_producto;
"""

df = pd.read_sql(query, conexion) #Ejecuta la consulta SQL y guarda el resultado en un DataFrame

print(df)               #muestra tabla

plt.figure()           #se abre una hoja para dibujar el gráfico
plt.scatter(df["precio"], df["cantidad"])     # se crea los puntos en el grafico (ejes x,y)

plt.title("Precio vs Cantidad vendida")  #titulo de grafico
plt.xlabel("Precio")                     #etiquetas de los ejes
plt.ylabel("Cantidad")

for i, txt in enumerate(df["nombre"]):    # recorre la columna "nombre"
    plt.annotate(txt, (df["precio"][i], df["cantidad"][i]))  # Coloca un texto (txt) en el gráfico en la posición:x=precio, y=cantidad

plt.grid()     #agrega lineas para facilitar la lectura
plt.show()     #muestra gráfico