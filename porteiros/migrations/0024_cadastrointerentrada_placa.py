# Generated by Django 4.2.1 on 2023-07-07 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('porteiros', '0023_remove_cadastrointerentrada_placa'),
    ]

    operations = [
        migrations.AddField(
            model_name='cadastrointerentrada',
            name='placa',
            field=models.CharField(default='placa', max_length=20),
            preserve_default=False,
        ),
    ]
