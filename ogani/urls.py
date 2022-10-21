from django.urls import path

from .views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('artigos/<int:pagina>', ArtigosView.as_view() , name='artigos'),
    path('blog-details/<str:nome>', ArtigoDetailsView.as_view() , name='artigo_details'),
    path('detalhes-da-compra/', DetalhesCompraView.as_view() , name='detalhes_compra'),
    path('contato/', ContatoView.as_view() , name='contato'),
    path('descricao-produtos/<str:nome>', DescricaoProdutosView.as_view() , name='descricao_produto'),
    path('produtos/', ProdutosView.as_view() , name='produtos'),
    path('carrinho-de-compra/', CarrinhoCompraView.as_view() , name='carrinho_de_compra'),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

