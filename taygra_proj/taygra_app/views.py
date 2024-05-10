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
    context['produto'] = Produto.objects.all()

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
        
        if user:
            auth_login(request, user)
            return HttpResponseRedirect(reverse('home'))
        
        form_login = LoginForm(request.POST)

        form_login.add_error(None, ['Usuário ou senha inválidos'])

        context = {
            'form': form_login,
        }
        
        return render(request, 'login.html', context=context)
        
    if request.method == 'GET':
        login_form = LoginForm()

        context = {
            'form': login_form
        }

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

    if request.method == 'GET':
        signup_form = SignupForm()

        context = {
            'form': signup_form
        }

        return render(request, 'signup.html', context=context)

def index(request):
    produto = Produto.objects.order_by('id')
    context = {'produto': produto}
    return render(request, 'index.html', context=context)

def produtos(request):
    produto = Produto.objects.order_by('id')
    context = {'produto': produto}
    return render(request, 'produtos.html', context=context)
def cadastros(request):
    return render(request, 'cadastro.html')

def add_produto(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        categoria = request.POST.get('categoria')
        preco = request.POST.get('preco')
        quantidade = request.POST.get('quantidade')
        desconto = request.POST.get('desconto')
        imagem_path = request.POST.get('imagem_path')
        num_produto = request.POST.get('num_produto')

        produto = Produto(nome=nome, descricao=descricao, preco=preco, categoria=categoria,
                          quantidade=quantidade, desconto=desconto, imagem_path=imagem_path,
                          num_produto=num_produto)
        produto.save()

        return HttpResponseRedirect(reverse('add_produto'))

    if request.method == 'GET':
        produto_form = ProdutoForm()

        context = {
            'form': produto_form
        }

        return render(request, 'cadastros/add_produto.html', context=context)
    
def add_categoria(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')

        categoria = Categoria(nome=nome)
        categoria.save()

        return HttpResponseRedirect(reverse('add_categoria'))

    if request.method == 'GET':
        categoria_form = CategoriaForm()

        context = {
            'form': categoria_form
        }

        return render(request, 'cadastros/add_categoria.html', context=context)
    
def add_pedido(request):
    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        produtos = request.POST.get('produtos')
        data = request.POST.get('data')
        total = request.POST.get('total')
        codigo_barras = request.POST.get('codigo_barras')
        status = request.POST.get('status')

        pedido = Pedido(usuario=usuario, produtos=produtos, data=data, total=total, codigo_barras=codigo_barras, status=status)
        pedido.save()

        return HttpResponseRedirect(reverse('add_pedido'))

    if request.method == 'GET':
        pedido_form = PedidoForm()

        context = {
            'form': pedido_form
        }

        return render(request, 'cadastros/add_pedido.html', context=context)
    
def add_carrinho(request):
    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        produto = request.POST.get('produto')

        carrinho = Carrinho(usuario=usuario, produto=produto)
        carrinho.save()

        return HttpResponseRedirect(reverse('add_carrinho'))

    if request.method == 'GET':
        carrinho_form = CarrinhoForm()

        context = {
            'form': carrinho_form
        }

        return render(request, 'cadastros/add_carrinho.html', context=context)
    
def add_status(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')

        status = Status(nome=nome)
        status.save()

        return HttpResponseRedirect(reverse('add_status'))

    if request.method == 'GET':
        status_form = StatusForm()

        context = {
            'form': status_form
        }

        return render(request, 'cadastros/add_status.html', context=context)
    
def add_cep(request):
    if request.method == 'POST':
        cep = request.POST.get('cep')
        logradouro = request.POST.get('logradouro')
        bairro = request.POST.get('bairro')
        cidade = request.POST.get('cidade')
        estado = request.POST.get('estado')

        cep = CEP(cep=cep, logradouro=logradouro, bairro=bairro, cidade=cidade, estado=estado)
        cep.save()

        return HttpResponseRedirect(reverse('add_cep'))
    
    if request.method == 'GET':
        cep_form = CEPForm()

        context = {
            'form': cep_form
        }

        return render(request, 'cadastros/add_cep.html', context=context)
    
def add_endereco(request):
    if request.method == 'POST':
        logradouro = request.POST.get('logradouro')
        numero = request.POST.get('numero')
        complemento = request.POST.get('compllemento')
        cep = request.POST.get('cep')

        endereco = Endereco(logradouro=logradouro, numero=numero, complemento=complemento, cep=cep)
        endereco.save()

        return HttpResponseRedirect(reverse('add_endereco'))
    
    if request.method == 'GET':
        endereco_form = EnderecoForm()

        context = {
            'form': endereco_form
        }

        return render(request, 'cadastros/add_endereco.html', context=context)

def add_bairro(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')

        bairro = Bairro(nome=nome)
        bairro.save()

        return HttpResponseRedirect(reverse('add_bairro'))

    if request.method == 'GET':
        bairro_form = BairroForm()

        context = {
            'form': bairro_form
        }

        return render(request, 'cadastros/add_bairro.html', context=context)
    
def add_cidade(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')

        cidade = Cidade(nome=nome)
        cidade.save()

        return HttpResponseRedirect(reverse('add_cidade'))

    if request.method == 'GET':
        cidade_form = CidadeForm()

        context = {
            'form': cidade_form
        }

        return render(request, 'cadastros/add_cidade.html', context=context)
    
def add_estado(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        sigla = request.POST.get('sigla')

        estado = Estado(nome=nome, sigla=sigla)
        estado.save()

        return HttpResponseRedirect(reverse('add_estado'))

    if request.method == 'GET':
        estado_form = EstadoForm()

        context = {
            'form': estado_form
        }

        return render(request, 'cadastros/add_estado.html', context=context)
