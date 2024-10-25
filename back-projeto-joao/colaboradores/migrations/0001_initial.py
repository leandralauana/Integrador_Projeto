# Generated by Django 5.1.1 on 2024-09-24 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Colaborador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('tipo_usuario', models.CharField(choices=[('Professor', 'Professor'), ('Administrativo', 'Administrativo'), ('Grupo de Pesquisa', 'Grupo de Pesquisa')], max_length=50)),
                ('departamento', models.CharField(max_length=100)),
                ('cargo', models.CharField(max_length=100)),
                ('email_institucional', models.EmailField(max_length=254, unique=True)),
                ('email_pessoal', models.EmailField(blank=True, max_length=254, null=True)),
                ('telefone', models.CharField(blank=True, max_length=20, null=True)),
                ('foto_perfil', models.ImageField(blank=True, null=True, upload_to='fotos_colaboradores/')),
                ('redes_sociais', models.JSONField(blank=True, null=True)),
            ],
        ),
    ]
