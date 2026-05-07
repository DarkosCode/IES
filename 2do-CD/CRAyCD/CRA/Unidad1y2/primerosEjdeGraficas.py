import matplotlib.pyplot as plt
#! ↓ para graficos tridimensionales
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

#? Primeros ejercicios con librerias de MatPlotLiB
#*1.1 Basicas
# ejeX = [1, 2, 3, 4, 5, 6, 7]
# ejeY = [10, 15, 20, 25, 30, 29, 40]

#*Etiquetando Ejes
# plt.xlabel("Duracion (horas)")
# plt.ylabel("Presupuesto (millones)")

# plt.title("Grafico de Presupuesto x Duracion de pelicula")
# #? .plot() es para grafico de linea.
# # plt.plot(ejeX, ejeY,label="imdbTop50", color="brown", linestyle="-")
# plt.legend()

# #? .scatter() es para graficos de dispersion
# plt.scatter(ejeX, ejeY, color="blue")
# plt.title("De dispersion")

# #? añadir cuadriculas al grafico
# plt.grid()

# plt.subplot(1,2,1)
# plt.plot(ejeX, ejeY)
# plt.title("G1")

# plt.subplot(1,2,2)    
# plt.bar(ejeX, ejeY) #? Grafico de barras
# plt.title("G2")

#? .hist() para graficos historiogramas
# datos = [1,2,2,2,3,3,4,4,4,4,5,5,6]
# plt.hist(datos, bins=5,color="purple")
# plt.title("Historiograma")

#? .pie() para graficos de torta
tamaños = [15,30,45,10]
etiquetas = ['A', 'B','C','D']
plt.pie(tamaños, labels=etiquetas, autopct='%1.1f%%') #autopct es para el formato del numero.
plt.title("1er Grafico de torta")



# #* Graficos TriDimensionales
# fig = plt.figure(figsize=(9, 6)) #Crea la "hoja en blanco" y le asigna un tamaño
# ax = fig.add_subplot(111, projection="3d")
# y = np.random.rand(50)
# x = np.random.rand(50)
# z = np.random.rand(50)

# ax.scatter(x,y,z) # type: ignore

# plt.savefig('nombreDelGrafico.png')

#* Mostrar el grafico en pantalla
plt.show()
