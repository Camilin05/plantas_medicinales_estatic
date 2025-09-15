from django.shortcuts import render

# Create your views here.

def inicio(request):
    return render(request, 'inicio.html')

def lista_plantas(request):
    return render(request, 'lista_plantas.html')

def lista_sintomas(request):
    return render(request, 'lista_sintomas.html')

def nosotros(request):
    return render(request, 'nosotros.html')