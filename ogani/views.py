from unicodedata import name
from django.shortcuts import render
from django.views.generic import TemplateView, View

from .models import Categoria, Produto, Banner, Blog
import re


class HomeView(View):
    
    def get(self, request):
        name_url = request.path
        lista_categoria = Categoria.objects.all()
        lista_destaques = Produto.objects.all()
        lista_banner = Banner.objects.all()
        latest_product = Produto.objects.filter() #filtrar os 12 ultimos produtos vendidos e paginar de 3 em 3
        top_rated_product = Produto.objects.filter() #filtrar os 12 produtos mais vendidos e paginar de 3 em 3
        review_product = Produto.objects.filter() #filtrar os 12 produtos melhor desejados e paginar de 3 em 3
        top_3_artigos = Blog.objects.all()[:3] #filtrar os 3 artigos mais recentes
        context = {
            'lista_categoria': lista_categoria,
            'lista_destaques': lista_destaques,
            'name_url': name_url,
            'lista_banner': lista_banner,
            'latest_product': latest_product, 
            'top_rated_product': top_rated_product,
            'review_product': review_product,
            'top_3_artigos': top_3_artigos,
        }
        return render(request, 'index.html', context)


class ProdutosView(TemplateView):

    def get(self, request):
        lista_categoria = Categoria.objects.all()
        lista_produtos = Produto.objects.all()
        latests_products = Produto.objects.all()[:3]
        promocao = Produto.objects.filter(promocao = True)
        name_url = request.path.title().replace('/', '')
        lista_ordem = ['quantidade', 'categoria', 'preco', 'promocao']
        paginas = self.paginas(len(lista_produtos))
        context = {
            'lista_categoria': lista_categoria,
            'lista_produtos': lista_produtos,
            'latests_products':latests_products,
            'promocao':promocao,
            'name_url': name_url,
            'lista_ordem': lista_ordem,
            'paginas': range(1,paginas + 1),
            'quantidade_produtos': len(lista_produtos),
        }
        return render(request, 'produtos.html', context)

    def paginas(self, num):
        if num % 9 == 0:
            return num // 9
        else:
            return (num // 9) + 1 

    def template_produtos(self, num):
        res = self.paginas(num)
        final = num
        inicio = 0
        if num == (9 * res):
            final = 9 * res

        if num > 9:
            inicio = final -1

        return inicio, final      


class DescricaoProdutosView(TemplateView):

    def get(self, request, nome=None):
        name_url = request.path.title().replace('/Descricao-Produtos/' , 'Descrição Produtos ')
        name_url = re.findall('Descrição Produtos', name_url)[0]
        lista_produtos = Produto.objects.all()
        lista_categoria = Categoria.objects.all()
        # TODO: fazer um try exception no lugar do if
        if nome:
            busca_nome =  Produto.objects.get(nome = nome) 
            
        context = {
            'name_url': name_url,
            'lista_categoria': lista_categoria,
            'busca_nome': busca_nome,
            'lista_produtos': lista_produtos[:4]

        }
        return render(request, 'descricao_produtos.html', context)
    


class ArtigosView(TemplateView):


    def get(self, request):
        name_url = request.path.title().replace('/', '')
        context = {
            'name_url': name_url,
        }
        return render(request, 'artigos.html', context)

class CarrinhoCompraView(TemplateView):

    def get(self, request):
        name_url = request.path.title().replace('/', '').replace('-', ' ')
        dados = request.POST()
        context={
            'name_url':name_url,
        }
        return render(request, 'carrinho_de_compra.html', context)


class BlogDetailsView(TemplateView):
    template_name = 'blog_details.html'


class CheckoutView(TemplateView):
    template_name = 'checkout.html'


class ContactView(TemplateView):
    template_name = 'contact.html'








def home(request):
    #colocar lista no banco de dados
    lista_menu_suspenso = [ 'Fresh Meat', 'Vegetables', 'Fruit & Nut Gifts', 'Fresh Berries',
                            'Ocean Foods', 'Butter & Eggs', 'Fastfood', 'Fresh Onion',
                            'Papayaya & Crisps', 'Oatmeal', 'Fresh Bananas',
                        ]
    context = {
        'lista': lista_menu_suspenso
    }
    return render(request, 'index.html', context)


'''

def blog_details(request):
    return render(request, 'blog_details.html')

#def blog(request):
#    return render(request, 'blog.html')

def checkout(request):
    return render(request, 'checkout.html')

def contact(request):
    return render(request, 'contact.html')

def main(request):
    return render(request, 'main.html')

def shop_details(request):
    return render(request, 'shop-details.html')

def shop_grid(request):
    return render(request, 'shop-grid.html')

def shoping_cart(request):
    return render(request, 'shoping-cart.html')

'''
    

