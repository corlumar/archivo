# Generated by Django 4.2 on 2023-04-23 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Productor',
            fields=[
                ('id', models.BigAutoField(max_length=100, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('apell_pat', models.CharField(blank=True, max_length=50, null=True)),
                ('apell_mat', models.CharField(blank=True, max_length=50, null=True)),
                ('genero', models.CharField(choices=[('H', 'Hombre'), ('M', 'Mujer')], max_length=1)),
                ('curp', models.CharField(max_length=18)),
            ],
        ),
    ]
