import uuid

from django.db import models
from stdimage.models import StdImageField


class Base(models.Model):
    criado = models.DateField('Criação', auto_now_add=True)
    modificado = models.DateField('Atualização', auto_now = True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True

    def get_file_path(_instance, filename):
        ext = filename.split('.')[-1]
        filename = f'{uuid.uuid4()}.{ext}'
        return filename

class Categoria(Base):
   
    nome_categoria = models.CharField('nome_categoria', max_length=50, null= True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        abstract = False

    def __str__(self):
        return self.nome_categoria

class Produto(Base):
    nome = models.CharField('Nome', max_length=50)
    quantidade = models.IntegerField('Quantidade')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    preco = models.DecimalField('Preço', decimal_places=2, max_digits=5, default=0.00 )
    imagem = models.ImageField('Imagem', upload_to='produtos/', null=True)  
    

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        abstract = False

        
    def __str__(self):
        return self.nome
    
    
