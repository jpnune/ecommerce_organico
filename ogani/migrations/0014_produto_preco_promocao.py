# Generated by Django 4.1.1 on 2022-10-05 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ogani', '0013_remove_produto_preco_promocao'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='preco_promocao',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True, verbose_name='Preço'),
        ),
    ]
