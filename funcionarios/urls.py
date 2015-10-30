from django.conf.urls import include, url
from . import views

urlpatterns = [
        url(r'^$', views.logar),
        url(r'^sair', views.sair),
]
