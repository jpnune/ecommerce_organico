# Generated by Django 4.1.1 on 2022-10-03 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ogani', '0005_remove_categoria_nome_categoria_banner_nome_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='nome',
            field=models.CharField(max_length=50, verbose_name='nome'),
        ),
    ]
