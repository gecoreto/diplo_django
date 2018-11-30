from django.urls import path
from django.views.generic import TemplateView
from django.conf.urls import url
from . import views
from django.views.decorators.csrf import csrf_exempt

app_name = 'graficas'
urlpatterns = [
    # path('', views.index, name='index'),
    path('/uno', views.graficauno, name='graficauno'),
    path('/dos', views.graficados, name='graficados'),
    # path('/generar', views.generarGrafica, name='generarGrafica'),
    url(r'generar', csrf_exempt(views.generarGrafica))
]