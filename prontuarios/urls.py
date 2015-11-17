from django.conf.urls import include, url
from .views import *
from . import views



urlpatterns = [
		url(r'cadastro/', views.cadastroProntuario),
		url(r'lista/$', ProntuarioListVeiw.as_view(), name='prontuario-list'),
		url(r'edit/(?P<pk>\d+)$', views.ProntuarioUpdate.as_view(), name='Prontuario_update'),
    	url(r'delete/(?P<pk>\d+)$', views.ProntuarioDelete.as_view(), name='Prontuario_delete'),
    	url(r'detail/(?P<pk>[-\w]+)/$', ProntuarioDetailView.as_view(), name='Prontuario-detail'),
    	

]