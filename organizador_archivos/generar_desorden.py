import os
from pathlib import Path
import random

# Carpeta donde crearemos el desastre
carpeta_destino = Path("downloads_fake")
carpeta_destino.mkdir(exist_ok=True)

# Tipos de archivos a crear
extensiones = [
    ".jpg", ".png", ".gif",       # Imágenes
    ".pdf", ".docx", ".txt",      # Documentos
    ".mp4", ".mkv",               # Videos
    ".mp3", ".wav",               # Música
    ".zip", ".rar", ".exe"        # Otros
]

print(f"Creando archivos basura en {carpeta_destino.absolute()}...")

for i in range(20):  # Crearemos 20 archivos
    ext = random.choice(extensiones)
    nombre = f"archivo_basura_{i}{ext}"
    ruta = carpeta_destino / nombre
    
    # Crear archivo vacío
    with open(ruta, "w") as f:
        f.write("Contenido de prueba")

print("¡Desorden generado con éxito!")