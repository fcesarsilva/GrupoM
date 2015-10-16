# -*- coding:utf-8 -*-
from django import forms
from .models import Paciente

class PacienteForm(forms.ModelForm):

    class Meta:
        model = Paciente
        fields = ('nome','cpf','cartao_SUS','data_Nascimento','sexo','estadoCivil','data_Atendimento','queixaPrincipal',)