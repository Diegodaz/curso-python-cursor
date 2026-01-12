#crea un contador de palabras por consola usando un bucle for
texto = input("Ingrese un texto: ")
palabras = texto.split()
for palabra in palabras:
    print(palabra)
print(f"El texto tiene {len(palabras)} palabras")
