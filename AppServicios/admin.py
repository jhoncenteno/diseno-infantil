from django.contrib import admin
from AppServicios.models import Servicios, Miembros

class ServiciosAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')   

class MiembrosAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')  

admin.site.register(Servicios, ServiciosAdmin)
admin.site.register(Miembros, MiembrosAdmin)