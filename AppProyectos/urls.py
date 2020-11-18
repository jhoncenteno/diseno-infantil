from django.urls import path
from AppProyectos import views
   

urlpatterns = [
    path('', views.TodosLosProyectos, name='proyectos'),
    path('<int:proyecto_id>', views.proyectos_detallados, name='proyectos_detallados'),
]

