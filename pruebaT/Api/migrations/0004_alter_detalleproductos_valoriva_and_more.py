# Generated by Django 4.0.4 on 2023-03-11 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0003_rename_valoriva_detalleproductos_valoriva'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detalleproductos',
            name='valorIva',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='Valor IVA'),
        ),
        migrations.AlterField(
            model_name='detalleproductos',
            name='valorTotal',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='Valor Total'),
        ),
    ]