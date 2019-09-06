from django.db import models

# Create your models here.
class Musica(models.Model):
    nome = models.CharField(
        max_length=255,
        verbose_name='Nome'
    )
    artista = models.CharField(
        max_length=255,
        verbose_name ='Artista'
    )
    genero = models.CharField(
        max_length=255,
        verbose_name='Genero'
    )
    link = models.CharField(
        max_length=255,
        verbose_name='link'
    )
    def __str__(self):
        return self.nome