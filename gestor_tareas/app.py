import json
import os
from flask import Flask, request, redirect, render_template

app = Flask(__name__)

ARCHIVO_DATOS = 'tareas.json'
tareas = []
siguiente_id = 1

# --- Funciones de Persistencia (Guardar/Cargar) ---
def cargar_datos():
    global tareas, siguiente_id
    if os.path.exists(ARCHIVO_DATOS):
        with open(ARCHIVO_DATOS, 'r') as f:
            data = json.load(f)
            tareas = data.get('tareas', [])
            siguiente_id = data.get('siguiente_id', 1)

def guardar_datos():
    with open(ARCHIVO_DATOS, 'w') as f:
        json.dump({'siguiente_id': siguiente_id, 'tareas': tareas}, f)

# Cargamos los datos al iniciar la app
cargar_datos()

# --- Funciones Modificadas para Guardar ---
def agregar_tarea_lista(texto):
    global siguiente_id
    tareas.append({'id': siguiente_id, 'texto': texto, 'hecho': False})
    siguiente_id += 1
    guardar_datos() # <--- Guardamos cambios

def completar_tarea_lista(id_tarea):
    for tarea in tareas:
        if tarea['id'] == id_tarea:
            tarea['hecho'] = True
            break
    guardar_datos() # <--- Guardamos cambios

# 1. Página principal: Muestra las tareas
@app.route('/')
def index():
    # Ordenamos: primero las pendientes (False), luego las hechas (True)
    tareas_ordenadas = sorted(tareas, key=lambda t: t['hecho'])
    return render_template('index.html', tareas=tareas_ordenadas)

# 2. Ruta para recibir el formulario de nueva tarea
@app.route('/agregar', methods=['POST'])
def agregar():
    texto_tarea = request.form.get('texto_tarea')
    if texto_tarea:
        agregar_tarea_lista(texto_tarea)
    return redirect('/')

# 3. Ruta para marcar como completada
@app.route('/completar/<int:id>')
def completar(id):
    completar_tarea_lista(id)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)