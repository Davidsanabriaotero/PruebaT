# Generated by Django 4.0.4 on 2023-03-11 02:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0002_alter_detalleproductos_valoriva_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='detalleproductos',
            old_name='ValorIva',
            new_name='valorIva',
        ),
    ]