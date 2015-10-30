from django.conf.urls import include, url
from . import views
from .views import PacienteListVeiw,PacienteUpdate,PacienteDelete

urlpatterns = [
    url(r'^$', views.poslogin),
    url(r'cadastro/', views.cadastroPaciente),
    url(r'lista/$', PacienteListVeiw.as_view(), name='pacinente-list'),
    url(r'edit/(?P<pk>\d+)$', views.PacienteUpdate.as_view(), name='paciente_update'),
    url(r'delete/(?P<pk>\d+)$', views.PacienteDelete.as_view(), name='paciente_delete'),
]
