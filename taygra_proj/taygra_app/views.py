from django.shortcuts import render

from taygra_app.models import Produto, Categoria, Pedido, Contato, Usuario, Status

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.hashers import make_password
from django.apps import apps

from taygra_app.forms import *

# Create your views here.

def context_(request):
    context = {
        'user': request.user
    }

    return context

def home(request):
    context = context_(request)

    return render(request, 'index.html', context=context)

def produtos(request):
    produtos = Produto.objects.all()

    context = context_(request)

    context = {
        'produtos': produtos
    }

    return render(request, 'produtos.html', context=context)

def produto(request, produto_id):
    produto = Produto.objects.get(id=produto_id)

    context = context_(request)

    context = {
        'produto': produto
    }

    return render(request, 'produto.html', context=context)

def categorias(request):
    categorias = Categoria.objects.all()

    context = context_(request)

    context = {
        'categorias': categorias
    }

    return render(request, 'categorias.html', context=context)

def categoria(request, categoria_id):
    categoria = Categoria.objects.get(id=categoria_id)

    context = context_(request)

    context = {
        'categoria': categoria
    }

    return render(request, 'categoria.html', context=context)

def pedidos(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))

    pedido = Pedido.objects.get(usuario=request.user)

    context = context_(request)

    context = {
        'pedido': pedido
    }

    return render(request, 'pedido.html', context=context)

def pedido(request, pedido_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    
    pedido = Pedido.objects.get(id=pedido_id)

    context = context_(request)

    context = {
        'pedido': pedido
    }

    return render(request, 'pedido.html', context=context)

def carrinho(request):
    pedidos = Pedido.objects.all()

    context = context_(request)

    context = {
        'pedidos': pedidos
    }

    return render(request, 'carrinho.html', context=context)

def contato(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        assunto = request.POST.get('assunto')
        mensagem = request.POST.get('mensagem')

        contato = Contato(nome, email, assunto, mensagem)
        contato.save()
    
    if request.method == 'GET':
        contato_form = ContatoForm()

        # context = context_(request)

        context = {
            'form': contato_form
        }

        return render(request, 'contato.html', context=context)

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            auth_login(request, user)
            return HttpResponseRedirect(reverse('home'))
        
    context = {}

    return render(request, 'login.html', context=context)

def logout(request):
    auth_logout(request)

    return HttpResponseRedirect(reverse('home'))

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password = make_password(password)
        user = Usuario(username=username, email=email, password=password)
        user.save()

        return HttpResponseRedirect(reverse('login'))

    context = {}

    return render(request, 'signup.html', context=context)