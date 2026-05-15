import pandas as pd

# bDePrueba = {
#     "nombre": ["Juan", "Maria", "Pedro", "Ana", "Luis"],
#     "edad": [25, 20, 22, 19, 23],
#     "sexo": ["Masculino", "Femenino", "Masculino", "Femenino", "Masculino"],
#     "calificación": [8.5, 9.2, 7.8, 9.5, 8.9],
# }

# df_manual = pd.DataFrame(bDePrueba)
# print(df_manual) #! 'Crea' una columna con Id's

df_csv = pd.read_csv("https://drive.google.com/uc?id=1sTzcEYZlwdSprPamS810YygkHEuQ9s7h", sep=";")
# print(df_csv)
# print(df_csv.shape, "\n") #! largo y ancho (cantidad de columnas y filas) de el .csv  

# mayorA35 = df_csv[df_csv['Edad'] > 40]
# print(mayorA35)
# print(mayorA35.shape, "\n")  

df_csv = df_csv.rename(columns={"Rubro": "Dedicacion"}) #! Renombrar columna
# print(df_csv)