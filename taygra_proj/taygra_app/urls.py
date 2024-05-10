from django.urls import path
from taygra_app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('produtos/', views.produtos, name='produtos'),
    path('produto/<int:produto_id>/', views.produto, name='produto'),
    path('categorias/', views.categorias, name='categorias'),
    path('categoria/<int:categoria_id>/', views.categoria, name='categoria'),
    path('carrinho/', views.carrinho, name='carrinho'),
    path('pedidos/', views.pedidos, name='pedidos'),
    path('pedido/<int:pedido_id>/', views.pedido, name='pedido'),
    path('contato/', views.contato, name='contato'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('perfil/', views.perfil, name='perfil'),
    path('perfil/editar', views.editar_perfil, name='editar_perfil'),
    path('perfil/encerrar', views.encerrar_conta, name='encerrar_conta'),
    path('cadastro/user/', views.signup, name='cadastro_usuario'),

    path('cadastro/', views.cadastros, name='cadastros'),
    path('add/produto/', views.add_produto, name='add_produto'),
    path('add/categoria/', views.add_categoria, name='add_categoria'),
    path('add/pedido/', views.add_pedido, name='add_pedido'),
    path('add/carrinho/', views.add_carrinho, name='add_carrinho'),
    path('add/status/', views.add_status, name='add_status'),
    path('add/endereco/', views.add_endereco, name='add_endereco'),
    path('add/bairro/', views.add_bairro, name='add_bairro'),
    path('add/cidade/', views.add_cidade, name='add_cidade'),
    path('add/estado/', views.add_estado, name='add_estado'),
    path('add/cep/', views.add_cep, name='add_cep'),
]