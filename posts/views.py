from django.shortcuts import render
from .models import Post

def inicio(request):
    return render(request, "posts/inicio.html")

def lista_posts(request):
    posts = [
        {
            "id": 1,
            "titulo": "Mi primer post",
            "autor": "Ana",
            "contenido": "Contenido del primer post.",
        },
        {
            "id": 2,
            "titulo": "Aprendiendo Django",
            "autor": "Luis",
            "contenido": "Contenido del segundo post.",
        },
        {
            "id": 3,
            "titulo": "Templates reutilizables",
            "autor": "Marta",
            "contenido": "Contenido del tercer post.",
        },
    ]

    return render(request, "posts/lista_posts.html", {"posts": posts})


def detalle_post(request, post_id):
    post = {
        "id": post_id,
        "titulo": f"Post número {post_id}",
        "autor": "Ana",
        "contenido": "Este es el contenido de ejemplo del post.",
    }

    return render(request, "posts/detalle_post.html", {"post": post})


def contacto(request):
    return render(request, "posts/contacto.html")

def acerca(request):
    return render(request, "posts/acerca.html")

def lista_posts(request):
    # Consulta a la base de datos mediante el ORM
    posts = Post.objects.filter(estado="publicado").order_by("-fecha_creacion")
    
    context = {
        "posts": posts
    }
    
    return render(request, "posts/lista_posts.html", context)