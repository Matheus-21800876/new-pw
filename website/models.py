from django.db import models

# Create your models here.
from django.db import models
from django.db.models import Model


def options():
    return [('1', 'Vermelho'), ('2', 'Azul'), ('3', 'Laranja')], \
           [('1', 'Magenta'), ('2', 'Roxo'), ('3', 'Amarelo')], \
           [('1', 'Vermelho'), ('2', 'Verde'), ('3', 'Azul'), ('4', 'Amarelo')], \
           [('1', 'Spring'), ('2', 'Winter'), ('3', 'Fall'), ('4', 'Azul'), ('5', 'Summer')], \
           [('1', 'Cores Frias'), ('2', 'Cores Quentes')], \
           [('1', 'Claro'), ('2', 'Médio'), ('3', 'Ruim')]


class Quizz(models.Model):
    nome = models.CharField(max_length=25, null=True)
    apelido = models.CharField(max_length=25, null=True)
    email = models.EmailField(max_length=75, null=True)
    pergunta1 = models.CharField(max_length=6, null=True)
    pergunta2 = models.CharField(max_length=5, null=True)
    pergunta3 = models.CharField(max_length=1, choices=options()[0], blank=False, default='Unspecified')
    pergunta4 = models.CharField(max_length=1, choices=options()[1], blank=False, default='Unspecified')
    pergunta5 = models.CharField(max_length=1, choices=options()[2], blank=False, default='Unspecified')
    pergunta6 = models.CharField(max_length=1, choices=options()[3], blank=True, default='Unspecified')
    pergunta7 = models.IntegerField(default=1)
    pergunta8 = models.CharField(max_length=1, choices=options()[4], blank=True, default='Unspecified')
    pergunta9 = models.CharField(max_length=1, choices=options()[4], blank=True, default='Unspecified')

    def __str__(self):
        return self.nome[:25]


class Contato(models.Model):
    nome = models.CharField(max_length=25, null=True)
    apelido = models.CharField(max_length=25, null=True)
    telefone = models.CharField(max_length=15, null=True)
    email = models.EmailField(max_length=75, null=True)
    data_de_nascimento = models.DateField(max_length=15, null=True, blank=True)

    def __str__(self):
        return self.nome[:25]


class Author(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    nome = models.CharField(max_length=25)

    def __str__(self):
        return self.nome[:25]


class Categoria(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome[:50]


class Paleta(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    cor1 = models.CharField(max_length=7)
    cor2 = models.CharField(max_length=7)
    cor3 = models.CharField(max_length=7)
    cor4 = models.CharField(max_length=7)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    categoria = models.ManyToManyField(Categoria, blank=True, related_name="Paletas")

    def __str__(self):
        return f"Paleta - 000{self.id}"


class Comentario(models.Model):
    interface = models.CharField(max_length=1, choices=options()[5], blank=False, default='Unspecified')
    navegacao = models.CharField(max_length=1, choices=options()[5], blank=False, default='Unspecified')
    velocidade = models.CharField(max_length=1, choices=options()[5], blank=False, default='Unspecified')
    geral = models.CharField(max_length=200, null=True)
