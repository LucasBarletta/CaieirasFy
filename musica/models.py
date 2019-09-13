from django.db import models
from artista.models import Artista

# Create your models here.
class Musica(models.Model):
    nome = models.CharField(
        max_length=255,
        verbose_name='nome'
    )
    artista = models.ForeignKey(
        Artista,
        on_delete=models.CASCADE,
        related_name='musica'
    )
    tempo = models.CharField(
        max_length=255,
        verbose_name='tempo'
    )
    genero = models.CharField(
        max_length=255,
        verbose_name='genero'
    )
    def __str__(self):
        return self.nome