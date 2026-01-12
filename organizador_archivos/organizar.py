from pathlib import Path
import shutil

# --- CONFIGURACIÓN ---
# Por seguridad, primero apuntamos a la carpeta falsa
# Cuando estés listo, puedes cambiar esto a Path.home() / "Downloads"
CARPETA_OBJETIVO = Path("downloads_fake")

# Definimos las categorías
CATEGORIAS = {
    "Imagenes":   [".png", ".jpg", ".jpeg", ".gif", ".bmp", ".svg"],
    "Documentos": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx"],
    "Videos":     [".mp4", ".avi", ".mkv", ".mov"],
    "Musica":     [".mp3", ".wav", ".flac"],
    "Comprimidos":[".zip", ".rar", ".7z"],
    "Ejecutables":[".exe", ".msi"]
}

def organizar():
    # 1. Crear mapa de extensiones (Diccionario invertido)
    # Resultado: {'.jpg': 'Imagenes', '.pdf': 'Documentos', ...}
    mapa_extensiones = {ext: cat for cat, exts in CATEGORIAS.items() for ext in exts}

    if not CARPETA_OBJETIVO.exists():
        print(f"La carpeta {CARPETA_OBJETIVO} no existe.")
        return

    print(f"--- Organizando {CARPETA_OBJETIVO} ---")

    # 2. Iterar sobre los archivos
    contados = 0
    for archivo in CARPETA_OBJETIVO.iterdir():
        # Ignoramos si es una carpeta o si es este mismo script
        if archivo.is_dir() or archivo.name == "organizar.py":
            continue

        # 3. Determinar categoría
        ext = archivo.suffix.lower()
        carpeta_destino_nombre = mapa_extensiones.get(ext, "Otros")
        
        # 4. Crear carpeta de destino
        carpeta_final = CARPETA_OBJETIVO / carpeta_destino_nombre
        carpeta_final.mkdir(exist_ok=True)

        # 5. Mover archivo (Manejando duplicados)
        destino = carpeta_final / archivo.name
        
        # Pequeña lógica por si el archivo ya existe en el destino
        if destino.exists():
            nombre_nuevo = f"{archivo.stem}_copia{archivo.suffix}"
            destino = carpeta_final / nombre_nuevo
        
        try:
            # Usamos shutil.move que es robusto moviendo entre discos si fuera necesario
            shutil.move(str(archivo), str(destino))
            print(f"Movido: {archivo.name} -> {carpeta_destino_nombre}/")
            contados += 1
        except Exception as e:
            print(f"Error moviendo {archivo.name}: {e}")

    print(f"\n¡Listo! Se movieron {contados} archivos.")

if __name__ == "__main__":
    organizar()