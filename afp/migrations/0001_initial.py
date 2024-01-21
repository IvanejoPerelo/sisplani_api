# Generated by Django 5.0.1 on 2024-01-21 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Afp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('tasa_aportes', models.FloatField()),
                ('tasa_seguros', models.FloatField()),
                ('tasa_comision_variable', models.FloatField()),
                ('max_remuneracion', models.FloatField()),
            ],
            options={
                'db_table': 'afp',
            },
        ),
    ]