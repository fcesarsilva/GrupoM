# -*- coding: utf-8 -*-

from django.contrib import admin
from prontuarios.models import Prontuario
from atendimentos.models import *
from funcionarios.models import *
from django.contrib.admin.widgets import FilteredSelectMultiple
from farmacos.models import *


class ProntuarioAdmin(admin.ModelAdmin):
	model = Prontuario
	list_display = ['paciente'] #ESTE DISPLAY ESTA RETORNANDO O "NOME" QUE FOI ADICIONADO NO ATRIBUTO NOME DA 
	search_fields = ['nome'] #CLASSE PACIENTE. ESTA SENDO REFERENCIADO ATRAVES DO ATRIBUTO "paciente" QUE ESTA
	filter_horizontal = ('remedio','medico',) 					 #COM UMA RELAÇÃO FOREIGNKEY COM A CLASSE PACIENTE.
	save_on_top = True

admin.site.register(Prontuario, ProntuarioAdmin)

# Register your models here.
