from django.contrib import admin

from .models import Categoria, Produto, Banner, Blog


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'criado', 'modificado', 'ativo')

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
   list_display = ('nome', 'quantidade', 'categoria', 'criado', 'modificado', 'ativo')

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('nome', 'imagem', 'criado', 'modificado', 'ativo' )
   
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('nome', 'imagem', 'criado', 'modificado', 'ativo' )
