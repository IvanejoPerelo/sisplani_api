# Generated by Django 5.0.1 on 2024-01-21 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aportaciones', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='aportaciones',
            name='descripcion',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='aportaciones',
            name='porcentaje_aportacion',
            field=models.FloatField(null=True),
        ),
    ]