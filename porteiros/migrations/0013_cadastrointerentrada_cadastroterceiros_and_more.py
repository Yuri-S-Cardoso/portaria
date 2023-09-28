# Generated by Django 4.2.1 on 2023-07-04 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('porteiros', '0012_alter_cadastrointer_especificacao_carga'),
    ]

    operations = [
        migrations.CreateModel(
            name='CadastroInterEntrada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_entrada', models.DateTimeField()),
                ('km_entrada', models.IntegerField()),
                ('lacre_entrada', models.CharField(max_length=20)),
                ('nfs_entrada', models.IntegerField()),
                ('qtde_malotes_entrada', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='CadastroTerceiros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placa_entrada', models.CharField(max_length=10)),
                ('veiculo_entrada', models.CharField(max_length=20)),
                ('data', models.DateTimeField()),
                ('cnpj', models.CharField(max_length=20)),
                ('carga', models.CharField(max_length=20)),
                ('motorista', models.CharField(max_length=50)),
                ('ajudante', models.IntegerField()),
                ('paletes', models.IntegerField()),
                ('chapelex', models.IntegerField()),
                ('nfs_prefixo', models.IntegerField()),
                ('nfs_de', models.IntegerField()),
                ('nfs_ate', models.IntegerField()),
                ('nfs_exceto', models.IntegerField()),
                ('nfs_apenas', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='cadastrointer',
            name='carga',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='cadastrointer',
            name='nfs_saida',
            field=models.IntegerField(),
        ),
    ]