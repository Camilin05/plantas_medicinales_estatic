from django.urls import path
from . import views

app_name = 'plantas'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('lista_plantas/', views.lista_plantas, name='lista_plantas'),
    path('lista_sintomas/', views.lista_sintomas, name='lista_sintomas'),
    path('nosotros/', views.nosotros, name='nosotros'),
]