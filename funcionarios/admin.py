from django.contrib import admin
from funcionarios.models import CommonInfo #Classe com atributos comuns a outras; nossa abstract class.
from funcionarios.models import Meta #Esta classe deve ser declarada com o atributo: abstract = True. Para que se possa distribuir a classe abstract nas classes filhas.
from funcionarios.models import Recepcionista
from funcionarios.models import Enfermeiro
from funcionarios.models import Medico

class RecepcionistaAdmin(admin.ModelAdmin):
	model = Recepcionista
	list_display = ['nome', 'matricula']
	list_filter = ['nome','cpf', 'data_Admissao']
	save_on_top = True

class EnfermeiroAdmin(admin.ModelAdmin):
	model = Enfermeiro
	list_display = ['nome', 'matricula']
	list_filter = ['nome','coren', 'data_Admissao']
	save_on_top = True

class MedicoAdmin(admin.ModelAdmin):
	model = Medico
	list_display = ['nome', 'CRM']
	list_filter = ['nome', 'especialidade']
	save_on_top = True

admin.site.register(Recepcionista, RecepcionistaAdmin) #Todas as classes aqui registradas aparecem na tela e podem ser manipuladas,
admin.site.register(Enfermeiro, EnfermeiroAdmin) #neste caso nao declarei CommonInfo e nem Meta pois elas devem permanecerem intocadas.
admin.site.register(Medico, MedicoAdmin)
# Register your models here.
