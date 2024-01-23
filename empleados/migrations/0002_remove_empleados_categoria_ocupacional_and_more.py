# Generated by Django 5.0.1 on 2024-01-23 02:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('afp', '0003_remove_afp_max_remuneracion_remove_afp_tasa_aportes_and_more'),
        ('empleados', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empleados',
            name='categoria_ocupacional',
        ),
        migrations.RemoveField(
            model_name='empleados',
            name='fecha_ingreso',
        ),
        migrations.RemoveField(
            model_name='empleados',
            name='regimen_laboral',
        ),
        migrations.AddField(
            model_name='empleados',
            name='afp',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='afp.afp'),
        ),
        migrations.AddField(
            model_name='empleados',
            name='categoriaOcupacional',
            field=models.CharField(db_column='categoria_ocupacional', max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='empleados',
            name='fechaIngreso',
            field=models.DateField(db_column='fecha_ingreso', null=True),
        ),
        migrations.AddField(
            model_name='empleados',
            name='regimenLaboral',
            field=models.CharField(db_column='regimen_laboral', max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='empleados',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='empleados',
            name='estado',
            field=models.BooleanField(null=True),
        ),
    ]
