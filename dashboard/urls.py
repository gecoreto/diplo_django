from django.urls import path
from django.views.generic import TemplateView
from django.conf.urls import url
from . import views

app_name = 'dashboard'
urlpatterns = [
    # path('', views.index, name='index'),
    url(r'^', TemplateView.as_view(template_name="index.html")),
]