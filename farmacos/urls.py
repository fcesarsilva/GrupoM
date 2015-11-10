from django.conf.urls import include, url
from . import views
from .views import RemedioListVeiw,RemedioDelete,RemedioDetailView


urlpatterns = [
    
      url(r'lista/$', RemedioListVeiw.as_view(), name='remedio-list'),
      url(r'cadastro/', views.cadastroRemedio),
      url(r'edit/(?P<pk>\d+)$', views.RemedioUpdate.as_view(), name='remedio_update'),
      url(r'delete/(?P<pk>\d+)$', views.RemedioDelete.as_view(), name='remedio_delete'),
      url(r'detail/(?P<pk>[-\w]+)/$', RemedioDetailView.as_view(), name='remedio-detail'),
	
]
