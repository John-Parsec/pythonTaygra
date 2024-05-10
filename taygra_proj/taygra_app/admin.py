from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(Produto)
admin.site.register(Categoria)
admin.site.register(Usuario)
admin.site.register(Pedido)
admin.site.register(Status)
admin.site.register(Contato)
admin.site.register(Endereco)
admin.site.register(Bairro)
admin.site.register(Cidade)
admin.site.register(Estado)