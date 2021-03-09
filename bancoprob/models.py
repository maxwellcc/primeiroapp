from django.db import models


class Area(models.Model):
    nome = models.CharField(
        max_length=30,
    )
    # Esse método permite incluir o nome do problema na visualizaçõa da lista
    def __str__(self):
        return self.nome

# Create your models here.
class BancoProblema(models.Model):
    area = models.ForeignKey(
        Area,
        related_name='banco_area',
        on_delete=models.SET_NULL,
        null=True,
    )
    problema = models.CharField(
        max_length=250,
    )
    cidade = models.CharField(
        max_length=50,
    )
    estado = models.CharField(
        max_length=2,
        null=True,
        blank=True # pode ser deixado em branco
    )

    # Esse método permite incluir o nome do problema na visualizaçõa da lista
    def __str__(self):
        return self.problema