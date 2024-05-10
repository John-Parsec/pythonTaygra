# Generated by Django 5.0.3 on 2024-05-10 13:53

import django.contrib.auth.models
import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=254)),
                ('assunto', models.CharField(max_length=250)),
                ('mensagem', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=250)),
                ('sigla', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('cpf', models.CharField(max_length=11)),
                ('telefone', models.CharField(max_length=11)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Bairro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=250)),
                ('cidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taygra_app.cidade')),
            ],
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logradouro', models.CharField(max_length=250)),
                ('numero', models.IntegerField()),
                ('complemento', models.CharField(max_length=250)),
                ('cep', models.CharField(max_length=8)),
                ('bairro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taygra_app.bairro')),
            ],
        ),
        migrations.AddField(
            model_name='cidade',
            name='estado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taygra_app.estado'),
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=250)),
                ('descricao', models.TextField()),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantidade', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('desconto', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(60)])),
                ('imagem_path', models.CharField(max_length=255)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taygra_app.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('codigo_barras', models.CharField(max_length=50)),
                ('produtos', models.ManyToManyField(to='taygra_app.produto')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taygra_app.status')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taygra_app.usuario')),
            ],
        ),
    ]