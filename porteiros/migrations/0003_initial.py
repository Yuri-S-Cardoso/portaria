# Generated by Django 4.2.1 on 2023-06-20 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('porteiros', '0002_delete_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Porteiro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('matricula', models.CharField(max_length=10)),
                ('senha', models.CharField(max_length=100)),
            ],
        ),
    ]
