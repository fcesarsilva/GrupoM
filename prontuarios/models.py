from django.db import models
from atendimentos.models import *
from funcionarios.models import *
from farmacos.models import * #importa todas as classes do modelo atendimento. Caso queira especificar
								 #devemos tirar o "*" e colocar a classe desejada.
class Prontuario(models.Model):
        codigo_Prontuario = models.IntegerField()
        data_Consulta = models.DateField()
        paciente = models.ForeignKey(Paciente)
        medico = models.ManyToManyField(Medico)
        remedio = models.ManyToManyField(Remedio)

# Create your models here.
