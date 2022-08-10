import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#lectura archivo
contamina=pd.read_csv("E:/Documents/teleiniformatica/proyecto/datos.csv",";")
#Diagramas de dispersion
plt.scatter(contamina['PUNT_GLOBAL'],contamina['Puntaje Socio Economico'])
plt.title('Puntaje global vs Puntaje SocioEconomico')
plt.ylabel("Puntaje SocioEconomico")
'''
plt.scatter(contamina['PUNT_GLOBAL'],contamina['Puntaje Socio Economico'])
plt.title('Puntaje global vs Puntaje SocioEconomico')
plt.ylabel("Puntaje SocioEconomico")

plt.scatter(contamina['PUNT_GLOBAL'],contamina['FAMI_TIENEINTERNET'])
plt.title('Puntaje global vs Tiene Internet')
plt.ylabel("Internet")
plt.xlabel("Puntaje Global")
plt.scatter(contamina['PUNT_GLOBAL'],contamina['FAMI_TIENESERVICIOTV'])

plt.ylabel("TV")
plt.xlabel("Puntaje Global")
plt.scatter(contamina['PUNT_GLOBAL'],contamina['FAMI_TIENECOMPUTADOR'])
plt.title('Puntaje global vs Tiene Computador')
plt.ylabel("Computador")



plt.scatter(contamina['PUNT_GLOBAL'],contamina['FAMI_TIENELAVADORA'])
plt.title('Puntaje global vs Tiene Lavadora')
plt.ylabel("Lavadora")
plt.scatter(contamina['PUNT_GLOBAL'],contamina['FAMI_TIENEHORNOMICROOGAS'])
plt.title('Puntaje global vs Tiene Microondas')
plt.ylabel("Microondas")
plt.scatter(contamina['PUNT_GLOBAL'],contamina['FAMI_TIENEAUTOMOVIL'])
plt.title('Puntaje global vs Automovil')
plt.ylabel("Automovil")

plt.scatter(contamina['PUNT_GLOBAL'],contamina['FAMI_TIENEMOTOCICLETA'])
plt.title('Puntaje global vs Motocicleta')
plt.ylabel("Motocicleta")

plt.scatter(contamina['PUNT_GLOBAL'],contamina['FAMI_TIENECONSOLAVIDEOJUEGOS'])
plt.title('Puntaje global vs Consola')
plt.ylabel("Consola")
plt.scatter(contamina['PUNT_GLOBAL'],contamina['FAMI_NUMLIBROS'])
plt.title('Puntaje global vs Cantidad Libros')
plt.ylabel("Cantidad Libros")
plt.scatter(contamina['PUNT_GLOBAL'],contamina['FAMI_COMELECHEDERIVADOS'])
plt.title('Puntaje global vs Frecuencia de Consumo de lacteos')
plt.ylabel("Frecuencia de Consumo de lacteos")
plt.scatter(contamina['PUNT_GLOBAL'],contamina['FAMI_COMECARNEPESCADOHUEVO'])
plt.title('Puntaje global vs Frecuencia de Consumo de pescado y huevo')
plt.ylabel("Frecuencia de Consumo de pescado y huevo")
plt.scatter(contamina['PUNT_GLOBAL'],contamina['FAMI_COMECEREALFRUTOSLEGUMBRE'])
plt.title('Puntaje global vs Frecuencia de Consumo de cereales, frutas y legumbres')
plt.ylabel("Frecuencia de Consumo de cereales, frutas y legumbres")
plt.scatter(contamina['PUNT_GLOBAL'],contamina['FAMI_SITUACIONECONOMICA'])
plt.title('Puntaje global vs Situación Economica familiar')
plt.ylabel("Situación Economica familiar")'''
plt.xlabel("Puntaje Global")
'''plt.show()'''

plt.show()


