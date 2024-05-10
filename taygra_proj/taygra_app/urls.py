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
    path('cadastro/user/', views.signup, name='cadastro_usuario'),
]