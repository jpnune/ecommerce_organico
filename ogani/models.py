from email.policy import default
from tkinter import Widget
from unittest.util import _MAX_LENGTH
import uuid
from xmlrpc.client import boolean

from django.db import models
from stdimage.models import StdImageField


class Base(models.Model):
    nome = models.CharField('Nome', max_length=50, unique= True)
    criado = models.DateField('Criação', auto_now_add=True)
    modificado = models.DateField('Atualização', auto_now = True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True

class Categoria(Base):

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        abstract = False

    def __str__(self):
        return self.nome

class Produto(Base):
    quantidade = models.IntegerField('Quantidade')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    preco = models.DecimalField('Preço', decimal_places=2, max_digits=5, default=0.00 )
    imagem = models.ImageField('Imagem', upload_to='produtos/', null=True)
    promocao = models.BooleanField('Promoção', default= False)
    preco_promocao =  models.DecimalField('Preço', decimal_places=2, max_digits=5, null=True, blank =True )
    descricao = models.TextField('Descrição', max_length='500', null=True)
    
    

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        abstract = False


    def __str__(self):
        return self.nome
 
    
    
class Banner(Base):
    
    imagem = models.ImageField('Imagem', upload_to='produtos/', null=True)

    class Meta:
        abstract = False

    def __str__(self):
        return self.nome

class Blog(Base):
    imagem = models.ImageField('Imagem', upload_to='produtos/', null=True)
    nome = models.CharField('Titulo', max_length=50)
    texto_chamada = models.CharField('texto_chamada', max_length=200)
    

    class Meta:
        abstract = False

class CarrinhoCompra(Base):
    preco = models.DecimalField('Preço', decimal_places=2, max_digits=5 )
    quantidade = models.IntegerField('Quantidade')


