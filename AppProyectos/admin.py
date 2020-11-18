from django.contrib import admin
from AppProyectos.models import Proyectos
# Register your models here.

class ProyectosAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')   

admin.site.register(Proyectos, ProyectosAdmin)