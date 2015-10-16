from django.db import models

class CommonInfo(models.Model):
	nome = models.CharField(max_length = 100)
	matricula = models.PositiveIntegerField()
	data_Admissao = models.DateField()

class Meta:
	abstract = True

class Recepcionista(CommonInfo):
	cpf = models.PositiveIntegerField(primary_key = True)

class Enfermeiro(CommonInfo):
	coren = models.PositiveIntegerField()
	especialidade = models.CharField(max_length = 50)

class Medico(CommonInfo):
	CRM = models.PositiveIntegerField()
	especialidade = models.CharField(max_length = 50)

	def __str__(self):
               return self.nome
		
		

# Create your models here.
