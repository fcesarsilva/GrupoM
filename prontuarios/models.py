#-*-coding: utf-8-*-
from django.db import models
from atendimentos.models import *
from funcionarios.models import *
from farmacos.models import * 
from simple_history.models import HistoricalRecords#importa todas as classes do modelo atendimento. Caso queira especificar
                                 #devemos tirar o "*" e colocar a classe desejada.
class Prontuario(models.Model):
        codigo_Prontuario = models.AutoField(primary_key=True)
        data_Consulta = models.DateField()
        paciente = models.ForeignKey(Paciente)
        medico = models.ManyToManyField(Medico)
        remedio = models.ManyToManyField(Remedio)
        
        def get_absolute_url(self):
            return reverse("Prontuario_list")

        history = HistoricalRecords()