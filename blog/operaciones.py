def listar_posts(lista_posts):
    print("\n--- LISTA DE POSTS ---")
    if not lista_posts:
        print("No hay posts para mostrar.")
        return
    
    for i, post in enumerate(lista_posts, 1):
        titulo = post.get("titulo", "Sin título")
        autor = post.get("autor", {}).get("nombre", "Autor Desconocido")
        estado = post.get("estado", "Estado Desconocido")
        print(f"{i}. Título: {titulo} | Autor: {autor} | Estado: {estado}")

def buscar_por_titulo(lista_posts, termino):
    print(f"\n--- RESULTADOS PARA '{termino}' ---")
    encontrados = False
    for post in lista_posts:
        titulo = post.get("titulo", "")
        if termino.lower() in titulo.lower():
            print(f"- {titulo} (Estado: {post.get('estado')})")
            encontrados = True
            
    if not encontrados:
        print("No se encontraron posts que coincidan con la búsqueda.")

def filtrar_por_tag(lista_posts, tag):
    print(f"\n--- POSTS CON EL TAG '{tag}' ---")
    encontrados = False
    for post in lista_posts:
        tags = post.get("tags", [])
        if isinstance(tags, list):
            tags_lower = [t.lower() for t in tags]
            if tag.lower() in tags_lower:
                print(f"- {post.get('titulo')} (Autor: {post.get('autor', {}).get('nombre', 'Desconocido')})")
                encontrados = True
                
    if not encontrados:
        print("No se encontraron posts con ese tag.")