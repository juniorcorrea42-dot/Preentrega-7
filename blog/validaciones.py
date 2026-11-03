def validar_post(post):
    errores = []
    
    if not isinstance(post, dict):
        return False, ["El post no es un diccionario."]
        
    if not post.get("titulo"):
        errores.append("El título está vacío o no existe.")
        
    if not post.get("contenido"):
        errores.append("El contenido está vacío o no existe.")
        
    autor = post.get("autor")
    if not isinstance(autor, dict):
        errores.append("El autor no es un diccionario válido.")
    elif not autor.get("nombre"):
        errores.append("El autor no tiene nombre especificado.")
        
    tags = post.get("tags")
    if not isinstance(tags, list):
        errores.append("Las etiquetas (tags) no están en formato de lista.")
        
    estado = post.get("estado")
    estados_permitidos = ["Borrador", "Publicado", "Archivado"]
    if estado not in estados_permitidos:
        errores.append(f"El estado '{estado}' no es válido.")
        
    if errores:
        return False, errores
    return True, []