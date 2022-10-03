from itertools import product
from django.shortcuts import render
from django.views.generic import TemplateView, View

from .models import Categoria, Produto, Banner, Blog


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
            'lista': lista_categoria,
            'lista_destaques': lista_destaques,
            'name_url': name_url,
            'lista_banner': lista_banner,
            'latest_product': latest_product, 
            'top_rated_product': top_rated_product,
            'review_product': review_product,
            'top_3_artigos': top_3_artigos,
        }
        return render(request, 'index.html', context)



class BlogView(TemplateView):
    template_name = 'blog.html'


class BlogDetailsView(TemplateView):
    template_name = 'blog_details.html'


class CheckoutView(TemplateView):
    template_name = 'checkout.html'


class ContactView(TemplateView):
    template_name = 'contact.html'


class MainView(TemplateView):
    template_name = 'shop_details.html'


class ShopDetailsView(TemplateView):
    template_name = 'shop_grid.html'

class ShopingCartView(TemplateView):
    template_name = 'shoping_cart.html'





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
    

