from django.shortcuts import render

# Create your views here.

def inicio (request):
    return render(request,'core/index.html')

def nosotros (request):
    return render(request,'core/nosotros.html')

def perros (request):
    return render(request,'core/perros.html')

def gatos (request):
    return render(request,'core/gatos.html')

def formulario (request):
    return render(request,'core/formulario.html')