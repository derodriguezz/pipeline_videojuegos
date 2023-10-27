!pip install matplotlib
!pip install squarify

import pandas as pd
import matplotlib.pyplot as plt
ruta_df = r"/content/Ventas_Videojuegos.xlsx"
# Carga el archivo Excel en un DataFrame de pandas
df_ventas = pd.read_excel(ruta_df)

#crear lista con nuevos nombres de columnas y asignar la lista como nombre de columnas del dataframe cargado
nuevos_nombres = ['NOMBRE_JUEGO', 'CONSOLA', 'AÑO_LANZAMIENTO', 'GENERO', 'DISTRIBUIDOR', 'NORTE_AMERICA', 'EUROPA', 'JAPON', 'OTROS', 'TOTAL']
df_ventas.columns = nuevos_nombres


#2 Limpieza
Despues de cargar los datos analizamos que datos faltan o deben ser convertidos. Aca cogimos los nombres de las columnas y los categorizamos tipo string para que puedan ser manejados mas facilmente.

#seleccionar columnas del dataframe y guardarlas como tipo de dato str
df_ventas['NOMBRE_JUEGO'] = df_ventas['NOMBRE_JUEGO'].astype(str)
df_ventas['CONSOLA'] = df_ventas['CONSOLA'].astype(str)
df_ventas['AÑO_LANZAMIENTO'] = df_ventas['AÑO_LANZAMIENTO'].astype(str)
df_ventas['GENERO'] = df_ventas['GENERO'].astype(str)
df_ventas['DISTRIBUIDOR'] = df_ventas['DISTRIBUIDOR'].astype(str)
#df_ventas = df_ventas.drop('Ventas Global', axis=1)

#Guardamos el resultado en un dataframe y exploramos nuevamente los datos en la siguiente tabla.

df_ventas
#nuevas preguntas o areas de investigación que obligan a reiniciar el analisis
#Apache dataset

df_ventas.info()

#3 Trasnformación de datos

#Empezamos con la agrupación por la columna editorial (distribuidor) y sumar las ventas, incluyendo las ventas global. Ordenamos el resultado de forma descendente por la columna ventas global.

# Agrupar por la columna "Editorial" y sumar las ventas, incluyendo "Ventas Global"
df_agrupado_ed = df_ventas.groupby('DISTRIBUIDOR').agg({'NORTE_AMERICA': 'sum', 'EUROPA': 'sum', 'JAPON': 'sum', 'OTROS': 'sum', 'TOTAL': 'sum'})

# Ordenar el resultado de forma descendente por la columna "Ventas Global"
df_agrupado_ed = df_agrupado_ed.sort_values(by='TOTAL', ascending=False).reset_index()
df_agrupado_ed = df_agrupado_ed.drop('TOTAL', axis=1)

df_agrupado_ed

# Agrupar por la columna "Editorial" y sumar las ventas, incluyendo "Ventas Global"
df_agrupado_gen = df_ventas.groupby('GENERO').agg({'NORTE_AMERICA': 'sum', 'EUROPA': 'sum', 'JAPON': 'sum', 'OTROS': 'sum', 'TOTAL': 'sum'})

# Ordenar el resultado de forma descendente por la columna "Ventas Global"
df_agrupado_gen = df_agrupado_gen.sort_values(by='TOTAL', ascending=False).reset_index()
df_agrupado_gen = df_agrupado_gen.drop('TOTAL', axis=1)

df_agrupado_gen

#A conntinuación vemos la tabla con agrupacion de datos por año de lanzamiento y la suma de todas las regiones. Ordenada de forma descendente segun el año de lanzamiento de cada juego.

# Agrupar por la columna "Editorial" y sumar las ventas, incluyendo "Ventas Global"
df_agrupado_yr = df_ventas.groupby('AÑO_LANZAMIENTO').agg({'NORTE_AMERICA': 'sum', 'EUROPA': 'sum', 'JAPON': 'sum', 'OTROS': 'sum', 'TOTAL': 'sum'})

# Ordenar el resultado de forma descendente por la columna "Ventas Global"
df_agrupado_yr = df_agrupado_yr.sort_values(by='TOTAL', ascending=False).reset_index()
df_agrupado_yr = df_agrupado_yr.drop('TOTAL', axis=1)

df_agrupado_yr

#Esta vez tenemos la tabla agrupada por consola, con la suma de ventas por regiones. Organizada de forma descendente y agrupada nuevamente lo que nos permite ver el ranking por consola.

# Agrupar por la columna "Editorial" y sumar las ventas, incluyendo "Ventas Global"
df_agrupado_plat = df_ventas.groupby('CONSOLA').agg({'NORTE_AMERICA': 'sum', 'EUROPA': 'sum', 'JAPON': 'sum', 'OTROS': 'sum', 'TOTAL': 'sum'})

# Ordenar el resultado de forma descendente por la columna "Ventas Global"
df_agrupado_plat = df_agrupado_plat.sort_values(by='TOTAL', ascending=False).reset_index()
df_agrupado_plat = df_agrupado_plat.drop('TOTAL', axis=1)

df_agrupado_plat

datos_faltantes = df_ventas.isna().sum()

datos_faltantes

#5 Visualizaciones
#Aca vemos diferentes graficas que nos muestran tendencias y comparaciones. Despues de ana.lizar la informacion en las tablas podemos comparar con la forma grafica.

# Agrupar por la columna "Editorial" y sumar las ventas globales
ventas_por_editorial = df_ventas.groupby('DISTRIBUIDOR')['TOTAL'].sum()

# Ordenar en orden descendente y seleccionar las 20 primeras
top_15_editoriales = ventas_por_editorial.sort_values(ascending=False).head(15)

# Crear el gráfico de barras
top_15_editoriales.plot(kind='bar', figsize=(12, 6))
plt.title('Top 15 Distribuidor por Total venta')
plt.xlabel('Distribuidor')
plt.ylabel('Venta total')
plt.xticks(rotation=90)

plt.show()

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Asegúrate de haber ejecutado previamente el código de agrupación y preparación de datos.

# Crear un gráfico de burbujas con colores y burbujas más grandes
plt.figure(figsize=(12, 8))
colors = np.random.rand(len(top_15_editoriales))
plt.scatter(top_15_editoriales.index, top_15_editoriales, s=top_15_editoriales*5, c=colors, alpha=0.6)

plt.title('Gráfico de burbujas de los 15 principales distribuidores por ventas totales')
plt.xlabel('Distribuidor')
plt.ylabel('Venta total')
plt.xticks(rotation=90)

# Añadir etiquetas a las burbujas
for i, txt in enumerate(top_15_editoriales):
    plt.annotate(txt, (top_15_editoriales.index[i], top_15_editoriales[i]), ha='center')

plt.show()

# Agrupar por la columna "Editorial" y sumar las ventas globales
ventas_por_genero = df_ventas.groupby('GENERO')['TOTAL'].sum()

# Ordenar en orden descendente y seleccionar las 20 primeras
top_15_genero = ventas_por_genero.sort_values(ascending=False).head(15)

# Crear el gráfico de barras
top_15_genero.plot(kind='bar', figsize=(12, 6))
plt.title('Top 15 Genero por Venta total')
plt.xlabel('Genero')
plt.ylabel('Venta total')
plt.xticks(rotation=90)

plt.show()

import pandas as pd
import matplotlib.pyplot as plt

# Asegúrate de haber ejecutado previamente el código de agrupación y preparación de datos.

# Crear el gráfico de barras horizontales con colores asignados y etiquetas
colors = ['#FF9999', '#FFCC99', '#FFFF99', '#CCFFCC', '#99FFFF', '#99CCFF', '#CC99FF', '#FF99FF', '#FFCCFF', '#CCCCCC', '#CC9999', '#CC6600', '#CCCC00', '#66CC66', '#99CCCC']

plt.figure(figsize=(10,8))
top_15_genero.sort_values().plot(kind='barh', color=colors)
plt.title('Top 15 Género por Venta total')
plt.xlabel('Venta total')
plt.ylabel('Género')

# Agregar etiquetas a las barras
for index, value in enumerate(top_15_genero.sort_values()):
    plt.text(value, index, str(round(value, 2)))

plt.show()

# Agrupar por la columna "Editorial" y sumar las ventas globales
ventas_por_anio = df_ventas.groupby('AÑO_LANZAMIENTO')['TOTAL'].sum()

# Ordenar en orden descendente y seleccionar las 20 primeras
top_15_anio = ventas_por_anio.sort_values(ascending=False).head(15)

# Crear el gráfico de barras
top_15_anio.plot(kind='bar', figsize=(12, 6))
plt.title('Top 15 Años por Venta total')
plt.xlabel('Año de lanzamiento')
plt.ylabel('Ventas Globales')
plt.xticks(rotation=90)

plt.show()

import pandas as pd
import matplotlib.pyplot as plt
import squarify

# Asegúrate de haber ejecutado previamente el código de agrupación y preparación de datos.

# Supongamos que el código previo ha creado top_15_anio correctamente
# Definir top_15_anio como un diccionario para simular el caso
top_15_anio = {
    2010: 500,
    2011: 700,
    2012: 900,
    2013: 800,
    2014: 1200,
    2015: 1500,
    2016: 1700,
    2017: 1900,
    2018: 2000,
    2019: 2200,
    2020: 2400,
    2021: 2500
}

# Preparar los datos para el treemap
df = pd.DataFrame(list(top_15_anio.items()), columns=['Año de Lanzamiento', 'Ventas Globales'])
df = df.sort_values('Ventas Globales', ascending=False)

# Crear el gráfico de treemap
plt.figure(figsize=(10, 6))
squarify.plot(sizes=df['Ventas Globales'], label=df.apply(lambda x: f"{x[0]}\n({x[1]})", axis=1), alpha=0.6)
plt.title('Gráfico de Treemap de Ventas Globales por Año de Lanzamiento')
plt.axis('off')
plt.show()

# Agrupar por la columna "Editorial" y sumar las ventas globales
ventas_por_plat = df_ventas.groupby('CONSOLA')['TOTAL'].sum()

# Ordenar en orden descendente y seleccionar las 20 primeras
top_15_plat = ventas_por_plat.sort_values(ascending=False).head(15)

# Crear el gráfico de barras
top_15_plat.plot(kind='bar', figsize=(12, 6))
plt.title('Top 15 Consolas por Venta total')
plt.xlabel('Consola')
plt.ylabel('Venta total')
plt.xticks(rotation=90)

plt.show()

import pandas as pd
import matplotlib.pyplot as plt

# Asegúrate de haber ejecutado previamente el código de agrupación y preparación de datos.

# Supongamos que el código previo ha creado top_15_plat correctamente
# Definir top_15_plat como un diccionario para simular el caso
top_15_plat = {
    'PlayStation': 5000,
    'Xbox': 4500,
    'Nintendo': 4000,
    'PC': 3800,
    'Mobile': 3000,
    'Other': 2000,
    'Sega': 1500,
    'Atari': 1000,
    'Intellivision': 800,
    'NeoGeo': 700,
    'Commodore': 600,
    'Amstrad': 500,
    'Ouya': 400,
    '3DO': 300,
    'Jaguar': 200
}

# Crear el gráfico circular con etiquetas
plt.figure(figsize=(8, 8))
plt.pie(top_15_plat.values(), labels=top_15_plat.keys(), autopct='%1.1f%%', colors=plt.cm.Paired.colors)
plt.title('Gráfico Circular de Venta Total por Consola')
plt.show()




