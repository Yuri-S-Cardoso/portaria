# Generated by Django 4.2.1 on 2023-07-07 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('porteiros', '0020_alter_cadastrointerentrada_placa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadastrointerentrada',
            name='km_entrada',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='cadastrointerentrada',
            name='placa',
            field=models.CharField(max_length=20),
        ),
    ]
