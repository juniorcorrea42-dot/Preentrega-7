class Autor:
    def __init__(self, nombre, bio=""):
        self.nombre = nombre
        self.bio = bio

    def to_dict(self):
        return {"nombre": self.nombre, "bio": self.bio}

    @classmethod
    def from_dict(cls, datos):
        return cls(nombre=datos.get("nombre", "Desconocido"), bio=datos.get("bio", ""))

class Post:
    def __init__(self, id_post, titulo, contenido, autor, tags, estado="borrador"):
        self.id = id_post
        self.titulo = titulo
        self.contenido = contenido
        self.autor = autor  # Instancia de Autor
        self.tags = tags
        self.estado = estado

    def to_dict(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "contenido": self.contenido,
            "autor": self.autor.to_dict(),
            "tags": self.tags,
            "estado": self.estado
        }

    @classmethod
    def from_dict(cls, datos):
        autor_obj = Autor.from_dict(datos.get("autor", {}))
        return cls(
            id_post=datos.get("id", 0),
            titulo=datos.get("titulo", ""),
            contenido=datos.get("contenido", ""),
            autor=autor_obj,
            tags=datos.get("tags", []),
            estado=datos.get("estado", "borrador")
        )

class Blog:
    def __init__(self):
        self.posts = []

    def agregar_post(self, post):
        self.posts.append(post)

    def listar_posts(self):
        if not self.posts:
            print("No hay posts.")
            return
        for post in self.posts:
            print(f"[{post.estado.upper()}] {post.titulo} - Autor: {post.autor.nombre}")

    def buscar_por_titulo(self, titulo):
        termino = titulo.lower().strip()
        return [p for p in self.posts if termino in p.titulo.lower()]

    def filtrar_por_tag(self, tag):
        tag_limpio = tag.lower().strip()
        return [p for p in self.posts if tag_limpio in [t.lower() for t in p.tags]]

    def to_dict_list(self):
        return [post.to_dict() for post in self.posts]