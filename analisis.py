import pandas as pd
import matplotlib.pyplot as plt

# Mini Análisis de Datos
# 1. Leer el archivo "datos.csv"
# 2. Calcular estadísticas básicas (media, mediana, desviación estándar) de 'x' e 'y'
# 3. Imprimir los resultados en consola
# 4. Generar y mostrar un gráfico de dispersión (scatter plot) de x vs y

# 1. Leer el archivo "datos.csv"
datos = pd.read_csv("datos.csv")

# 2. Calcular estadísticas básicas (media, mediana, desviación estándar) de 'x' e 'y'
media_x = datos["x"].mean()
media_y = datos["y"].mean()
desviacion_estandar_x = datos["x"].std()
desviacion_estandar_y = datos["y"].std()

# 3. Imprimir los resultados en consola
print(f"Media de x: {media_x}")
print(f"Media de y: {media_y}")
print(f"Desviación estándar de x: {desviacion_estandar_x}")
print(f"Desviación estándar de y: {desviacion_estandar_y}")

# 4. Generar y mostrar un gráfico de dispersión (scatter plot) de x vs y
plt.scatter(datos["x"], datos["y"])
plt.xlabel("x")
plt.ylabel("y")
plt.title("Gráfico de dispersión de x vs y")
plt.show()

