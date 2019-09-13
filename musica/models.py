from django.db import models

# Create your models here.
class Musica(models.Model):
    nome = models.CharField(
        max_length=255,
        verbose_name='nome'
    )
    artista = models.CharField(
        max_length=255,
        verbose_name ='artista'
    )
    genero = models.CharField(
        max_length=255,
        verbose_name='tempo'
    )
    link = models.CharField(
        max_length=255,
        verbose_name='genero'
    )
    def __str__(self):
        return self.nome