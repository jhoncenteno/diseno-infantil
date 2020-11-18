
from django.shortcuts import render, get_object_or_404
from AppProyectos.models import Proyectos
from AppProyectos.forms import FiltroProyectos

def TodosLosProyectos(request):
    
    
    proyectos= Proyectos.objects.all()

    filtrado = FiltroProyectos(request.GET, queryset = proyectos)  

    proyectos = filtrado.qs


    return render(request, '2proyectos.html', { "proyectos" : proyectos, "filtrado" : filtrado })


def proyectos_detallados(request, proyecto_id):
    
    proyecto= get_object_or_404(Proyectos, id= proyecto_id)

    return render(request, '3proyecto_detallado.html', { "proyecto" : proyecto})