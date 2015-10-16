from django.contrib import admin
from atendimentos.models import Paciente

class PacienteAdmin(admin.ModelAdmin):
	model = Paciente
	list_display = ['nome', 'cartao_SUS']
	search_fields = ['nome', 'cartao_SUS']
	#list_filter = ['nome', 'cartao_SUS', 'data_Atendimento']
	save_on_top = True

admin.site.register(Paciente, PacienteAdmin)

# Register your models here.
