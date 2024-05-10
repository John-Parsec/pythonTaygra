# Generated by Django 5.0.3 on 2024-05-10 16:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taygra_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrinho',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('produtos', models.ManyToManyField(to='taygra_app.produto')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taygra_app.usuario')),
            ],
        ),
    ]
