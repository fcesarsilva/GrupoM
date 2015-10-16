from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.poslogin),
    url(r'^cadastro/', views.cadastroPaciente),
]
