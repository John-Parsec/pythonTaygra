# Generated by Django 5.0.6 on 2024-05-10 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taygra_app', '0004_remove_bairro_cidade_remove_cidade_estado_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='num_produto',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
