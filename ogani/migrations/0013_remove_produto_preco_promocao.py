# Generated by Django 4.1.1 on 2022-10-05 17:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ogani', '0012_alter_produto_preco_promocao'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produto',
            name='preco_promocao',
        ),
    ]
