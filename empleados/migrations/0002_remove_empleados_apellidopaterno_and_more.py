# Generated by Django 5.0.1 on 2024-01-25 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empleados',
            name='apellidoPaterno',
        ),
        migrations.AddField(
            model_name='empleados',
            name='apellido_paterno',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
