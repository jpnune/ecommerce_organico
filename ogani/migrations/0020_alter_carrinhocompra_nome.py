# Generated by Django 4.1.1 on 2022-10-18 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ogani', '0019_blog_corpo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carrinhocompra',
            name='nome',
            field=models.CharField(max_length=50, verbose_name='Nome'),
        ),
    ]
