from django import forms
from django.forms import ModelForm
from .models import Quizz, Contato, Comentario


class QuizzForm(ModelForm):
    class Meta:
        model = Quizz
        fields = '__all__'
        # inserção de classes CSS para formatação de cada campo do formulário
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-block info-input-group'}),
            'apelido': forms.TextInput(attrs={'class': 'form-block info-input-group'}),
            'email': forms.EmailInput(attrs={'class': 'form-block info-input-group', 'placeholder': 'abc@def.com'}),
            'pergunta1': forms.TextInput(attrs={'class': 'form-block info-input-group'}),
            'pergunta2': forms.TextInput(attrs={'class': 'form-block info-input-group'}),
            'pergunta3': forms.RadioSelect(attrs={'class': 'color-fieldset'}),
            'pergunta4': forms.RadioSelect(attrs={'class': 'color-fieldset'}),
            'pergunta5': forms.RadioSelect(attrs={'class': 'color-fieldset'}),
            'pergunta6': forms.Select(attrs={'class': 'form-block info-input-group'}),
            'pergunta7': forms.NumberInput(attrs={'class': 'form-block info-input-group', 'min': '1', 'max': '10'}),
            'pergunta8': forms.Select(attrs={'class': 'form-block info-input-group'}),
            'pergunta9': forms.Select(attrs={'class': 'form-block info-input-group'}),
        }

        # texto a exibir junto à janela de inserção
        labels = {
            'pergunta1': 'Qual a cor do centro do modelo RGB?',
            'pergunta2': 'Qual a cor do centro do modelo CMYK?',
            'pergunta3': 'Qual das opções NÃO faz parte do modelo RGB?',
            'pergunta4': 'Qual das opções NÃO faz parte do modelo CMYK?',
            'pergunta5': 'Quais das opões NÃO é uma das cores primárias?',
            'pergunta6': 'Qual das opões NÃO é um tema para paletas?',
            'pergunta7': 'Quantas cores geralmente compõem uma paleta?',
            'pergunta8': 'Qual seria a melhor categoria para uma paleta com as cores: Branco, Azul e Verde?',
            'pergunta9': 'Qual seria a melhor categoria para uma paleta com as cores: Amarelo, Laranja e Vermelho?',
        }


class ContatoForm(ModelForm):
    class Meta:
        model = Contato
        fields = '__all__'
        # inserção de classes CSS para formatação de cada campo do formulário
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-block info-input-group'}),
            'apelido': forms.TextInput(attrs={'class': 'form-block info-input-group'}),
            'telefone': forms.TextInput(attrs={'class': 'form-block info-input-group'}),
            'email': forms.EmailInput(attrs={'class': 'form-block info-input-group', 'placeholder': 'abc@def.com'}),
            'data_de_nascimento': forms.DateInput(attrs={'class': 'form-block info-input-group'}),
        }


class ComentarioForm(ModelForm):
    class Meta:
        model = Comentario
        fields = '__all__'
        # inserção de classes CSS para formatação de cada campo do formulário
        widgets = {
            'interface': forms.RadioSelect(attrs={'class': 'color-fieldset'}),
            'navegacao': forms.RadioSelect(attrs={'class': 'color-fieldset'}),
            'velocidade': forms.RadioSelect(attrs={'class': 'color-fieldset'}),
            'geral': forms.TextInput(attrs={'class': 'form-block info-input-group'}),
        }
