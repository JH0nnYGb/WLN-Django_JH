# Generated by Django 5.0.6 on 2024-07-11 21:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_remove_receita_alegenicos_remove_receita_ingrediente_and_more'),
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Perfil',
        ),
    ]
