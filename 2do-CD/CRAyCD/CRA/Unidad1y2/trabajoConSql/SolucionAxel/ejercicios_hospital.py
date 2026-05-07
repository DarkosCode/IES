"""
=============================================================
  BASE DE DATOS HOSPITAL - IES Belgrano - 2do año
=============================================================

TABLAS DISPONIBLES:
  pacientes  -> id_paciente, nombre, edad, sexo, ciudad
  medicos    -> id_medico, nombre, especialidad
  consultas  -> id_consulta, id_paciente, id_medico,
                fecha, tiempo_espera, diagnostico

INSTRUCCIONES:
  1. Completá la consulta SQL en la variable CONSULTA
  2. Ejecutá el archivo: python3 ejercicios_hospital.py
  3. Vas a ver los resultados en pantalla
  4. Luego usá los datos para armar el gráfico con matplotlib
=============================================================
"""

import sqlite3
import os
import matplotlib.pyplot as plt

# ── Inicialización automática de la BD ────────────────────────────────────────

SQL_FILE = os.path.join(os.path.dirname(__file__), "hospital.sql")
DB_FILE  = os.path.join(os.path.dirname(__file__), "hospital.db")

def inicializar_db():
    if not os.path.exists(DB_FILE):
        print("Creando la base de datos...")
        with open(SQL_FILE, "r", encoding="utf-8") as f:
            sql = f.read()
        con = sqlite3.connect(DB_FILE)
        con.executescript(sql)
        con.commit()
        con.close()
        print("Base de datos lista.\n")

inicializar_db()

# ── Conexión ──────────────────────────────────────────────────────────────────

con = sqlite3.connect(DB_FILE)

#! ── 1) ESCRIBÍ TU CONSULTA SQL ACÁ ───────────────────────────────────────────
#?las 3 comillas sirven para escribir consultas largas
CONSULTA = """ 
SELECT SEXO, COUNT(*) AS total
FROM pacientes
GROUP BY SEXO
ORDER BY total DESC
"""

# ── Ejecución y muestra de resultados ─────────────────────────────────────────

cursor = con.execute(CONSULTA)
columnas = [desc[0] for desc in cursor.description]
filas    = cursor.fetchall()
con.close()

print("Resultado de la consulta:")
print("  " + " | ".join(columnas))
print("  " + "-" * 40)
for fila in filas:
    print("  " + " | ".join(str(v) for v in fila))
print(f"\n  Total: {len(filas)} fila(s)\n")

# ── 2) ARMÁ TU GRÁFICO ACÁ ────────────────────────────────────────────────────
# Usá los datos de 'columnas' y 'filas' para construir el gráfico.
# Ejemplo: si tu consulta devuelve (ciudad, total), podés hacer:
#
#   ciudades = [fila[0] for fila in filas]
#   totales  = [fila[1] for fila in filas]

ciudades = [fila[0] for fila in filas]
totales  = [fila[1] for fila in filas]

fig, ax = plt.subplots()
ax.bar(ciudades, totales)
ax.set_title("Pacientes por ciudad")
ax.set_xlabel("SEXO")
ax.set_ylabel("Total")
plt.tight_layout()
plt.show()
