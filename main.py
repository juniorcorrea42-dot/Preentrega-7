from blog.modelos import Autor, Post, Blog
from blog.datos import cargar_datos, guardar_datos

def mostrar_menu():
    print("\n--- MENU DEL BLOG DE ENERGÍAS RENOVABLES ---")
    print("1. Ver todos los posts")
    print("2. Buscar por titulo")
    print("3. Filtrar por tag")
    print("4. Crear nuevo post")
    print("5. Guardar posts en JSON")
    print("6. Salir")
    try:
        return int(input("Elige una opción (1-6): "))
    except ValueError:
        print("Error: Ingresa un número válido.")
        return 0

if __name__ == "__main__":
    mi_blog = Blog()
    cargar_datos(mi_blog)

    while True:
        opcion = mostrar_menu()
        
        if opcion == 1:
            mi_blog.listar_posts()
        elif opcion == 2:
            termino = input("Ingresa el título a buscar: ")
            resultados = mi_blog.buscar_por_titulo(termino)
            for p in resultados:
                print(f"- {p.titulo} (Autor: {p.autor.nombre})")
        elif opcion == 3:
            tag = input("Ingresa el tag para filtrar: ")
            resultados = mi_blog.filtrar_por_tag(tag)
            for p in resultados:
                print(f"- {p.titulo}")
        elif opcion == 4:
            titulo = input("Título: ")
            contenido = input("Contenido: ")
            nombre_autor = input("Autor: ")
            tags = [t.strip() for t in input("Tags (separados por coma): ").split(",")]
            
            nuevo_autor = Autor(nombre=nombre_autor, bio="Especialista en renovables")
            nuevo_post = Post(len(mi_blog.posts) + 1, titulo, contenido, nuevo_autor, tags, "publicado")
            mi_blog.agregar_post(nuevo_post)
            print("Post creado.")
        elif opcion == 5:
            guardar_datos(mi_blog)
        elif opcion == 6:
            guardar_datos(mi_blog)
            print("Saliendo...")
            break
        elif opcion != 0:
            print("Opción inválida.")