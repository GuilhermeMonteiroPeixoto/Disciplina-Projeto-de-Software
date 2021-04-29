from django.db import models

class Empregado(models.Model):
        nome = models.CharField(max_length=100)
        endereco = models.CharField(max_length=100)
        tipo_contrato = models.CharField(max_length=100)
        sindicato = models.BooleanField(blank=True, null=True)
        observacao = models.TextField(blank=True, null=True)

        def __str__(self):
                return self.nome
