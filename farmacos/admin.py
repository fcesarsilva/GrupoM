from django.contrib import admin
from farmacos.models import *

class RemedioAdmin(admin.ModelAdmin):
	model = Remedio

	search_fields = ['descricao_Medicamento']
	list_display = ['descricao_Medicamento']
	save_on_top = True

admin.site.register(Remedio, RemedioAdmin)

# Register your models here.
