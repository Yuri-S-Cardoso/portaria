# Generated by Django 4.2.1 on 2023-07-07 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('porteiros', '0018_cadastrointerentrada_placa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadastrointerentrada',
            name='placa',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
    ]
