import json
import os
from blog.modelos import Post

ARCHIVO_JSON = "posts.json"

def cargar_datos(blog):
    if not os.path.exists(ARCHIVO_JSON) or os.stat(ARCHIVO_JSON).st_size == 0:
        return
    try:
        with open(ARCHIVO_JSON, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
            for item in datos:
                blog.agregar_post(Post.from_dict(item))
    except (json.JSONDecodeError, IOError) as e:
        print(f"Error al leer JSON: {e}")

def guardar_datos(blog):
    try:
        with open(ARCHIVO_JSON, "w", encoding="utf-8") as archivo:
            json.dump(blog.to_dict_list(), archivo, indent=4, ensure_ascii=False)
        print("Datos guardados en posts.json.")
    except IOError as e:
        print(f"Error al guardar: {e}")