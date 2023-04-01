from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Publicacion
from .forms import publicacionForm

# Create your views here.

def inicio(request):
    return render(request, 'paginas/inicio.html')

def nosotros(request):
    return render(request, 'paginas/nosotros.html')

def publicaciones(request):
    publicaciones = Publicacion.objects.all()
    return render(request, 'paginas/publicaciones/index.html', {'publicaciones':publicaciones})

def crear(request):
    formulario = publicacionForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('publicaciones')
    return render(request, 'paginas/publicaciones/crear.html', {'formulario':formulario})

def editar(request, codigo):
    publicaciones = Publicacion.objects.get(codigo=codigo)
    formulario = publicacionForm(request.POST or None, request.FILES or None, instance=publicaciones)
    if formulario.is_valid() and request.POST:
        formulario.save()   
        return redirect('publicaciones')
    return render(request, 'paginas/publicaciones/editar.html', {'formulario': formulario})

def eliminar(request, codigo):  
    publicaciones = Publicacion.objects.get(codigo=codigo)
    publicaciones.delete()
    return redirect('publicaciones')                