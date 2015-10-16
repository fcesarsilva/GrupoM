# -*- coding: utf-8 -*- #colocar esta declaração para que seja permitido palavras acentuadas e cedilhas

from django.db import models
#from django_localflavor_br.forms import BRCPFField


class Paciente(models.Model):

        SEXO_CHOICES = (

                (u'masculino', u'Masculino'),
                (u'feminino', u'Feminino'),

        )

        ESTADO_CIVIL_CHOICES = (

                (u'solteiro(a)', u'Solteiro(a)'),
                (u'casado(a)', u'Casado(a)'),
                (u'divorciado(a)', u'Divorciado(a)'),
                (u'viuvo', u'Viuvo(a)'),

        )


        nome = models.CharField(max_length = 100)
        cpf = models.PositiveIntegerField()
        cartao_SUS = models.IntegerField(primary_key = True)
        data_Nascimento = models.DateField()
        sexo = models.CharField(max_length = 20, choices = SEXO_CHOICES)
        estadoCivil = models.CharField(max_length = 20, choices = ESTADO_CIVIL_CHOICES, verbose_name = 'Estado Civil')
        data_Atendimento = models.DateField()
        queixaPrincipal = models.CharField(max_length = 100, verbose_name = 'Queixa Principal')

        def __str__(self):
               return self.nome #Esta função deve existir para que o nome apareça em todas as chamadas de outras classes,
                                 #tipo prontuario que solicita o nome de pessoas que ja o possuem. Caso esra função nao exista
                                 #aparecerá pacienteobject.

# Create your models here.
