import django_filters
from AppProyectos.models import Proyectos

class FiltroProyectos(django_filters.FilterSet):
    class Meta:
        model = Proyectos      
        fields = ['type']      