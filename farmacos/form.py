from django import forms
from .models import Remedio

class RemedioForm(forms.ModelForm):

    class Meta:
        model = Remedio
        fields= ('descricao_Medicamento',)