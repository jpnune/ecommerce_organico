# Generated by Django 4.1.1 on 2022-10-13 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ogani', '0017_carrinhocompra'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='categoria',
            field=models.CharField(max_length=100, null=True, verbose_name='Categoria'),
        ),
    ]
