from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Disciplina(models.Model):
    titulo_disciplina = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.titulo_disciplina

class Conteudo(models.Model):
    titulo_conteudo = models.CharField(max_length=255, null=True)
    ano = models.CharField(max_length=255, null=True)
    disciplina = models.ManyToManyField(Disciplina)

    def __str__(self):
        return self.titulo_conteudo

class Tag(models.Model):
    nametag = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.nametag

class OA(models.Model):
    class NewManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='published')

    titulo = models.CharField(max_length=255)
    descricao = models.CharField(max_length=2048, null=True, blank=True)
    autor = models.CharField(max_length=255, null=True, blank=True)
    link = models.URLField(null=True)
    imagem = models.ImageField(upload_to='imagens/uploads/',
                               default='imagens/uploads/logo.png')
    tags = models.ManyToManyField(Tag)
    conteudo = models.ManyToManyField(Conteudo)
    favoritos = models.ManyToManyField(User, default=None, blank=True)

    def __str__(self):
        return self.titulo