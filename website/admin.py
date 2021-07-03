from django.contrib import admin

# Register your models here.
from .models import Quizz, Author, Categoria, Paleta, Contato, Comentario

admin.site.register(Quizz)
admin.site.register(Author)
admin.site.register(Categoria)
admin.site.register(Paleta)
admin.site.register(Contato)
admin.site.register(Comentario)
