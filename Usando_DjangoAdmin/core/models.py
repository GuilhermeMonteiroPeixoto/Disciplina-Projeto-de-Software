from django.db import models

# Create your models here.
class Empregado(models.Model):
	TIPO = (
        ('H', 'Horista'),
        ('C', 'Comissionado'),
        ('A', 'Assalariado'),
    )

	nome = models.CharField(max_length=100)
	data_nascimento = models.DateField(blank=True, null=True)
	cpf = models.CharField(max_length=10)
	contrato = models.CharField(blank=True, max_length=1,choices=TIPO)
	salario = models.DecimalField(null=True, max_digits=6, decimal_places=2)
	sindicato = models.BooleanField(default=False)

	def __str__(self):
		return self.nome
