from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.hashers import make_password
from django.apps import apps

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
    Produto = apps.get_model('taygra_app', 'Produto')
    produtos = Produto.objects.all()

    context = context_(request)

    context = {
        'produtos': produtos
    }

    return render(request, 'produtos.html', context=context)

def produto(request, produto_id):
    Produto = apps.get_model('taygra_app', 'Produto')
    produto = Produto.objects.get(id=produto_id)

    context = context_(request)

    context = {
        'produto': produto
    }

    return render(request, 'produto.html', context=context)

def categorias(request):
    Categoria = apps.get_model('taygra_app', 'Categoria')
    categorias = Categoria.objects.all()

    context = context_(request)

    context = {
        'categorias': categorias
    }

    return render(request, 'categorias.html', context=context)

def categoria(request, categoria_id):
    Categoria = apps.get_model('taygra_app', 'Categoria')
    categoria = Categoria.objects.get(id=categoria_id)

    context = context_(request)

    context = {
        'categoria': categoria
    }

    return render(request, 'categoria.html', context=context)

def carrinho(request):
    Pedido = apps.get_model('taygra_app', 'Pedido')
    pedidos = Pedido.objects.all()

    context = context_(request)

    context = {
        'pedidos': pedidos
    }

    return render(request, 'carrinho.html', context=context)

def login(request):
    if request.method == 'POST':
        Usuario = apps.get_model('taygra_app', 'Usuario')
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            auth_login(request, user)
            return HttpResponseRedirect(reverse('home'))
        
    context = {}

    return render(request, 'login.html', context=context)