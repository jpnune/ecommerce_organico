# Generated by Django 4.1.1 on 2022-10-03 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ogani', '0006_alter_categoria_nome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='nome',
            field=models.CharField(max_length=50, verbose_name='Nome'),
        ),
    ]
