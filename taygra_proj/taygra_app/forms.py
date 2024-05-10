from django import forms
from .models import *

class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ['nome', 'email', 'assunto', 'mensagem']
        labels = {
            'nome': 'Nome',
            'email': 'E-mail',
            'assunto': 'Assunto',
            'mensagem': 'Mensagem'
        }
        widgets = {'email': forms.EmailInput()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['nome'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Nome Completo*', 'required': 'required'})
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'E-mail*', 'required': 'required'})
        self.fields['assunto'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Assunto*', 'required': 'required'})
        self.fields['mensagem'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Mensagem*', 'required': 'required', 'rows': '4'})

class LoginForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['username', 'password']
        labels = {
            'username': 'Usuário',
            'password': 'Senha'
        }
        widgets = {
            'password': forms.PasswordInput()
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Usuário*', 'required': 'required'})
        self.fields['password'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Senha*', 'required': 'required'})

class SignupForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['first_name', 'last_name', 'username', 'email', 'password']
        labels = {
            'first_name': 'Nome',
            'last_name': 'Sobrenome',
            'username': 'Usuário',
            'email': 'E-mail',
            'password': 'Senha'
        }
        widgets = {
            'password': forms.PasswordInput()
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Nome*', 'required': 'required'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Sobrenome*', 'required': 'required'})
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Usuário*', 'required': 'required'})
        self.fields['password'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Senha*', 'required': 'required'})
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'E-mail*', 'required': 'required'})

class CarrinhoForm(forms.ModelForm):
    class Meta:
        model = Carrinho
        fields = ['usuario', 'produto']
        labels = {
            'usuario': 'Usuário ID',
            'produtos': 'Produto ID'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['usuario'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Usuário*', 'required': 'required'})
        self.fields['produto'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Produto*', 'required': 'required'})

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome']
        labels = {
            'nome': 'Nome'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['nome'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Nome*', 'required': 'required'})

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'descricao', 'preco', 'categoria']
        labels = {
            'nome': 'Nome',
            'descricao': 'Descrição',
            'preco': 'Preço',
            'categoria': 'Categoria'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['nome'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Nome*', 'required': 'required'})
        self.fields['descricao'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Descrição*', 'required': 'required'})
        self.fields['preco'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Preço*', 'required': 'required'})
        self.fields['categoria'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Categoria*', 'required': 'required'})

class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ['nome']
        labels = {
            'nome': 'Nome'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['nome'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Nome*', 'required': 'required'})

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['usuario', 'produtos', 'total', 'codigo_barras', 'status']
        labels = {
            'usuario': 'Usuário ID',
            'produtos': 'Produto ID',
            'total': 'Total',
            'codigo_barras': 'Código de Barras',
            'status': 'Status'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['usuario'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Usuário*', 'required': 'required'})
        self.fields['produtos'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Produto*', 'required': 'required'})
        self.fields['total'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Total*', 'required': 'required'})
        self.fields['codigo_barras'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Código de Barras*', 'required': 'required'})
        self.fields['status'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Status*', 'required': 'required'})

class BairroForm(forms.ModelForm):
    class Meta:
        model = Bairro
        fields = ['nome']
        labels = {
            'nome': 'Nome'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['nome'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Nome*', 'required': 'required'})
        
class CidadeForm(forms.ModelForm):
    class Meta:
        model = Cidade
        fields = ['nome']
        labels = {
            'nome': 'Nome'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['nome'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Nome*', 'required': 'required'})

class EstadoForm(forms.ModelForm):
    class Meta:
        model = Estado
        fields = ['nome', 'sigla']
        labels = {
            'nome': 'Nome',
            'sigla': 'Sigla'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['nome'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Nome*', 'required': 'required'})
        self.fields['sigla'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Sigla*', 'required': 'required'})

class CEPForm(forms.ModelForm):
    class Meta:
        model = CEP
        fields = ['cep', 'bairro', 'cidade', 'estado']
        labels = {
            'cep': 'CEP',
            'bairro': 'Bairro ID',
            'cidade': 'Cidade ID',
            'estado': 'Estado ID'
        }

    def __init__(self, *args, **kwargs):
        self.fields['cep'].widget.attrs.update({'class': 'form-control', 'placeholder': 'CEP*', 'required': 'required'})
        self.fields['bairro'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Bairro*', 'required': 'required'})
        self.fields['cidade'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Cidade*', 'required': 'required'})
        self.fields['estado'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Estado*', 'required': 'required'})

class EnderecoForm(forms.ModelForm):
    class Meta:
        model = Endereco
        fields = ['logradouro', 'numero', 'complemento', 'cep']
        labels = {
            'logradouro': 'Logradouro',
            'numero': 'Número',
            'complemento': 'Complemento',
            'cep': 'CEP'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['logradouro'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Logradouro*', 'required': 'required'})
        self.fields['numero'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Número*', 'required': 'required'})
        self.fields['complemento'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Complemento*', 'required': 'required'})
        self.fields['cep'].widget.attrs.update({'class': 'form-control', 'placeholder': 'CEP*', 'required': 'required'})