import pandas as pd
import random
from datetime import datetime, timedelta

# Configuración
productos = ['Laptop', 'Mouse', 'Teclado', 'Monitor', 'Cable HDMI']
precios = {'Laptop': 800, 'Mouse': 20, 'Teclado': 40, 'Monitor': 200, 'Cable HDMI': 10}
n_registros = 100  # Generaremos 100 ventas

datos = []
fecha_inicio = datetime(2025, 1, 1)

print("Generando datos sintéticos...")

for _ in range(n_registros):
    # Fecha aleatoria en los primeros 4 meses de 2025
    dias_random = random.randint(0, 120)
    fecha = fecha_inicio + timedelta(days=dias_random)
    
    prod = random.choice(productos)
    cantidad = random.randint(1, 5) # Venta de 1 a 5 unidades
    precio_unitario = precios[prod]
    
    datos.append([fecha.strftime("%Y-%m-%d"), prod, cantidad, precio_unitario])

# Crear DataFrame y guardar
df = pd.DataFrame(datos, columns=['fecha', 'producto', 'cantidad', 'precio'])
df.to_csv('ventas.csv', index=False)
print("¡Archivo 'ventas.csv' creado con éxito!")