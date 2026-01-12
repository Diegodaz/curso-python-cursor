import pandas as pd
import matplotlib.pyplot as plt

# 1. Cargar datos
# 'parse_dates' convierte la columna fecha de texto a objetos de fecha reales
print("--- Cargando datos ---")
df = pd.read_csv('ventas.csv', parse_dates=['fecha'])

# Calcular columna de ingresos totales por fila
df['ingreso'] = df['cantidad'] * df['precio']

# ---------------------------------------------------------
# 2. ANÁLISIS MENSUAL
# ---------------------------------------------------------
# Convertimos la fecha a formato 'Año-Mes' (ej: 2025-01)
df['mes'] = df['fecha'].dt.to_period('M')

# Agrupamos por mes y sumamos los ingresos
ventas_por_mes = df.groupby('mes')['ingreso'].sum()

print("\n--- Ventas Totales por Mes ---")
print(ventas_por_mes)

# GRÁFICO 1: Ventas por Mes
plt.figure(figsize=(8, 5))
# Convertimos el índice a string para que matplotlib no se confunda con fechas
ventas_por_mes.index = ventas_por_mes.index.astype(str)
plt.bar(ventas_por_mes.index, ventas_por_mes.values, color='skyblue')
plt.title("Ventas Totales por Mes")
plt.xlabel("Mes")
plt.ylabel("Ingresos ($)")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig("grafico_mensual.png") # Guardamos la imagen
plt.show() # Mostramos la ventana

# ---------------------------------------------------------
# 3. ANÁLISIS POR PRODUCTO
# ---------------------------------------------------------
# Agrupamos por producto sumando cantidad e ingreso
ventas_prod = df.groupby('producto').agg({
    'cantidad': 'sum',
    'ingreso': 'sum'
})

# Encontrar los ganadores
mas_vendido = ventas_prod['cantidad'].idxmax()
mayor_ingreso = ventas_prod['ingreso'].idxmax()

print("\n--- Resultados del Análisis ---")
print(f"Producto más vendido (unidades): {mas_vendido} ({ventas_prod.loc[mas_vendido, 'cantidad']} u.)")
print(f"Producto con mayor ingreso ($):  {mayor_ingreso} (${ventas_prod.loc[mayor_ingreso, 'ingreso']:.2f})")

# GRÁFICO 2: Top 5 Productos por Ingresos
top5 = ventas_prod.nlargest(5, 'ingreso')

plt.figure(figsize=(8, 5))
plt.bar(top5.index, top5['ingreso'], color='orange')
plt.title("Top 5 Productos por Ingresos")
plt.xlabel("Producto")
plt.ylabel("Ingresos Totales ($)")
plt.tight_layout()
plt.savefig("grafico_productos.png")
plt.show()