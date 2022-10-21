from random import sample
import django
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
from django.urls import reverse_lazy
from .form import CarrinhoCompra2
from .models import Categoria, Produto, Banner, Artigo, CarrinhoCompra
import re

class ArtigoMenuLateral(TemplateView):
    def filtro_categoria(self):
        categorias = list({cat.categoria for cat in Artigo.objects.all()})
        categorias.sort()
        dict_lista = {'Todos': len(Artigo.objects.all())}
        for item in categorias:
            dict_lista[item] = len(Artigo.objects.filter(categoria = item)) 
        return dict_lista

    def ultimos_artigos(self, quantidade=int):
        ultimos_artigos = Artigo.objects.order_by('-criado')[:quantidade]
        return ultimos_artigos


class HomeView(View):
    
    def get(self, request):
        name_url = request.path
        lista_categoria = Categoria.objects.all()
        lista_destaques = Produto.objects.all()
        lista_banner = Banner.objects.all()
        latest_product = Produto.objects.filter() #filtrar os 12 ultimos produtos vendidos e paginar de 3 em 3
        top_rated_product = Produto.objects.filter() #filtrar os 12 produtos mais vendidos e paginar de 3 em 3
        review_product = Produto.objects.filter() #filtrar os 12 produtos melhor desejados e paginar de 3 em 3
        top_3_artigos = Artigo.objects.all()[:3] #filtrar os 3 artigos mais recentes
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
        print('promo ==========',promocao)
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
    
    def post(self, request):
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
        if request.method == 'GET':
            form = CarrinhoCompra2() 
            context = {
                'name_url': name_url,
                'lista_categoria': lista_categoria,
                'busca_nome': busca_nome,
                'lista_produtos': lista_produtos[:4],
                'form' : form,

            }
            return render(request, 'descricao_produtos.html', context)
    
    def post(self, request, nome=None):
        dados = request.POST
        #nome = request.POST.get('nome_produto')
        #preco = float(request.POST.get('preco_produto').replace(',', '.'))
        #quantidade = int(request.POST.get('quantidade_produtos'))
        #total = preco * quantidade
        #print('nome  === ',nome)
        #print('preco  === ',preco)
        #print('qtdd  === ',quantidade)
        #print('carrinho == ', request.POST.get('carrinho'))
        print('dados === ',dados)

        #TODO: fazer uma verificacao se ja existe o produto e apenas somar 
        #CarrinhoCompra.objects.create(nome=nome, preco=preco, quantidade=quantidade, total=total)


        return redirect('produtos')


class CarrinhoCompraView(TemplateView):

    def get(self, request):
        name_url = request.path.title().replace('/', '').replace('-', ' ')

        dados = CarrinhoCompra.objects.all()
        
        context={
            'name_url':name_url,
            'carrinho_compra':dados,
        }
        return render(request, 'carrinho_de_compra.html', context)


class ArtigosView(ArtigoMenuLateral):
    
    def get(self, request, pagina):
        indice_pagina = int(request.path.split('/')[2])
        context = {
            'name_url': request.path.title().split('/')[1],
            'dict_lista': self.filtro_categoria(),
            'artigos_recentes': self.ultimos_artigos(5),
            'paginas': range(1, self.paginas() + 1),
            'artigos' : self.mostra_artigos(indice_pagina),
            
        }
        return render(request, 'artigos.html/', context)

    def paginas(self):
        tamanho = Artigo.objects.count()
        if tamanho % 6 == 0:
            pagina = tamanho // 6
        elif (tamanho > 6) and (tamanho % 6 != 0):
            pagina = (tamanho // 6) + 1    
        return pagina

    def mostra_artigos(self,indice_pagina):
            inicio = (indice_pagina * 6) - 6
            return Artigo.objects.all()[inicio: inicio + 6]

    


class ArtigoDetailsView(ArtigoMenuLateral):
    def get(self, request, nome):
        lista = list(Artigo.objects.exclude(nome=nome).filter(categoria = Artigo.objects.values_list('categoria', flat=True).get(nome=nome)))
        
        if len(lista) > 3:
            lista_artigos_relacionados = sample(lista,k=3)
        else:
            lista_artigos_relacionados = sample(lista, k = len(lista))
            
        

        context = {
            'artigo': Artigo.objects.filter(nome= nome ).get(),
            'artigos_recentes': self.ultimos_artigos(5),
            'dict_lista': self.filtro_categoria(),
            'lista_artigos_relacionados':lista_artigos_relacionados,
        }
        return render(request, 'artigo_details.html', context)


class DetalhesCompraView(TemplateView):


    def get(self, request):
        context = {
            'name_url': request.path.title().split('/')[1].replace('-', ' '),
        }

        return render(request, 'detalhes_compra.html', context)
    


class ContatoView(TemplateView):
    def get(sef, request):
        context = {
            'name_url': request.path.title().replace('/', ''),
        }
        return render(request,'contato.html', context)

    def post(self,request):
        print('request =======',request.POST)
        context = {
            'name_url': request.path.title().split('/')[1].replace('-', ' '),

        }
        return render(request, 'contato.html', context)


class Formulario(TemplateView):
    
    def get(self, request):
        form = CarrinhoCompra2(request.POST)
        print(form)
        context = {

        }
        return render(self, 'carrinho_de_compra.html', context )

    
    
