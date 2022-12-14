# Generated by Django 4.1.1 on 2022-10-05 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ogani', '0009_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='preco_promocao',
            field=models.DecimalField(decimal_places=2, editable=False, max_digits=5, null=True, verbose_name='Promoção'),
        ),
        migrations.AddField(
            model_name='produto',
            name='promocao',
            field=models.BooleanField(default=False, verbose_name='Promoção'),
        ),
    ]
