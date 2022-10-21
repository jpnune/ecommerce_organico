from django.contrib import admin

from .models import CarrinhoCompra, Categoria, Produto, Banner, Artigo


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'criado', 'modificado', 'ativo')

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
   list_display = ('nome', 'preco','quantidade', 'categoria','promocao', 'ativo')


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('nome', 'imagem', 'criado', 'modificado', 'ativo' )


@admin.register(Artigo)
class ArtigoAdmin(admin.ModelAdmin):
    list_display = ('id','nome', 'categoria', 'criado', 'modificado', 'ativo' )


@admin.register(CarrinhoCompra)
class CarrinhoComprasAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'quantidade', 'total', 'criado', 'modificado', 'ativo')




