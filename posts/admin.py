from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    # Columnas útiles que se mostrarán en la lista del admin
    list_display = ("titulo", "autor", "estado", "fecha_creacion")
    list_filter = ("estado", "autor")
    search_fields = ("titulo", "contenido")

admin.site.register(Post, PostAdmin)