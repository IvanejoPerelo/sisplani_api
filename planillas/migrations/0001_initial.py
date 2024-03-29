# Generated by Django 5.0.1 on 2024-01-24 14:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('empleados', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Planillas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_planilla', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'db_table': 'planillas',
            },
        ),
        migrations.CreateModel(
            name='DetallePlanillas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subtotal', models.FloatField()),
                ('total', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empleados.empleados')),
                ('planilla', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='planillas.planillas')),
            ],
            options={
                'db_table': 'detalle_planillas',
            },
        ),
    ]
