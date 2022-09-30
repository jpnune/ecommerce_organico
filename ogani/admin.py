from django.contrib import admin

from .models import Categoria, Produto


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome_categoria', 'criado', 'modificado', 'ativo')

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
   list_display = ('nome', 'quantidade', 'criado', 'modificado', 'ativo')
   
