from django import forms
from .models import Contato, Usuario

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
        self.fields['last_name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Sobrenome'})
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Usuário*', 'required': 'required'})
        self.fields['password'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Senha*', 'required': 'required'})
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'E-mail*', 'required': 'required'})
        