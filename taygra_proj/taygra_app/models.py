from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Produto(models.Model):
    nome = models.CharField(max_length=250)
    descricao = models.TextField()
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.IntegerField(validators=[MinValueValidator(0)])
    desconto = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(60)])
    imagem_path = models.CharField(max_length=255)

    def __str__(self):
        return self.nome
    
    def preco_com_desconto(self):
        return self.preco - (self.preco * self.desconto / 100)
    
class Categoria(models.Model):
    nome = models.CharField(max_length=250)

    def __str__(self):
        return self.nome
    
class Usuario(User):
    cpf = models.CharField(max_length=11)
    telefone = models.CharField(max_length=11)
    
    def __str__(self):
        return self.username
    
class Pedido(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    produtos = models.ManyToManyField(Produto)
    data = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    codigo_barras = models.CharField(max_length=50)
    status = models.ForeignKey('Status', on_delete=models.CASCADE)
    
    def __str__(self):
        return f'Pedido de {self.usuario.username} em {self.data}'
    
    def calcular_total(self):
        total = 0
        for produto in self.produtos.all():
            total += produto.preco_com_desconto()
        return total
    
    def save(self, *args, **kwargs):
        self.total = self.calcular_total()
        super().save(*args, **kwargs)

class Carrinho(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    produtos = models.ManyToManyField(Produto)
    
    def __str__(self):
        return f'Carrinho de {self.usuario.username}'
    
    def calcular_total(self):
        total = 0
        for produto in self.produtos.all():
            total += produto.preco_com_desconto()
        return total
    
    def save(self, *args, **kwargs):
        self.total = self.calcular_total()
        super().save(*args, **kwargs)

class Status(models.Model):
    nome = models.CharField(max_length=250)
    
    def __str__(self):
        return self.nome
    
class Contato(models.Model):
    nome = models.CharField(max_length=250)
    email = models.EmailField()
    assunto = models.CharField(max_length=250)
    mensagem = models.TextField()
    
    def __str__(self):
        return self.nome
    
class Endereco(models.Model):
    logradouro = models.CharField(max_length=250)
    numero = models.IntegerField()
    complemento = models.CharField(max_length=250)
    cep = models.CharField(max_length=8)
    bairro = models.ForeignKey('Bairro', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.logradouro}, {self.numero}, {self.complemento} - {self.bairro.nome} - {self.bairro.cidade.nome} - {self.bairro.cidade.estado.sigla} - {self.cep}'
    
class Bairro(models.Model):
    nome = models.CharField(max_length=250)
    cidade = models.ForeignKey('Cidade', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nome

class Cidade(models.Model):
    nome = models.CharField(max_length=250)
    estado = models.ForeignKey('Estado', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nome
    
class Estado(models.Model):
    nome = models.CharField(max_length=250)
    sigla = models.CharField(max_length=2)
    
    def __str__(self):
        return self.sigla