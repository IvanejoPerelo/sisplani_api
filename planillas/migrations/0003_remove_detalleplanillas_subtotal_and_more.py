# Generated by Django 5.0.1 on 2024-01-27 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planillas', '0002_detalleplanillas_valores'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detalleplanillas',
            name='subtotal',
        ),
        migrations.RemoveField(
            model_name='detalleplanillas',
            name='total',
        ),
        migrations.AddField(
            model_name='detalleplanillas',
            name='sueldo_bruto',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='detalleplanillas',
            name='sueldo_neto',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='detalleplanillas',
            name='total_afp',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='detalleplanillas',
            name='total_descuentos',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='detalleplanillas',
            name='total_ingresos',
            field=models.FloatField(null=True),
        ),
    ]
