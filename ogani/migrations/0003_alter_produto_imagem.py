# Generated by Django 4.1.1 on 2022-09-30 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ogani', '0002_remove_produto_descricao_produto_imagem_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='imagem',
            field=models.ImageField(null=True, upload_to='produtos/', verbose_name='Imagem'),
        ),
    ]
