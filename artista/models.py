from django.db import models

# Create your models here.
class Artista(models.Model):
    nome = models.CharField(
        max_length=255,
        verbose_name='nome'
    )
    idade = models.IntegerField(
        verbose_name ='idade'
    )
    estilo = models.CharField(
        max_length=255,
        verbose_name='estilo'
    )
    def __str__(self):
        return self.nome