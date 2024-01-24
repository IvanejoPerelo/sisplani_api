# Generated by Django 5.0.1 on 2024-01-24 14:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('planillas', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingresos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField(null=True)),
                ('periodo', models.PositiveIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('detallePlanilla', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='planillas.detalleplanillas')),
            ],
            options={
                'db_table': 'ingresos',
            },
        ),
    ]