from django.urls import path
from django.views.generic import TemplateView
from django.conf.urls import url
from . import views

app_name = 'graficas'
urlpatterns = [
    path('', views.index, name='index'),
    path('/uno', views.graficauno, name='graficauno')
]