from django.db import models


from django.urls import reverse

# Create your models here.
class Proyectos(models.Model):
    titulo = models.CharField(max_length=50)
    
    TYPE = (                                                                   
            ('Of', 'Office'),
            ('Res', 'Residential'),                                   
            ('Com', 'Commercial')                                     
    )                                                                      
    type = models.CharField(max_length=150, null=True, choices=TYPE)  
    
    contenido = models.CharField(max_length=150)
    imagen = models.ImageField(upload_to='Proyectos')
    created = models.DateTimeField(auto_now_add=True)   
    updated = models.DateTimeField(auto_now_add=True)   

    def __str__(self):
        return self.titulo 

    def get_absolute_url(self):
        return reverse("proyectos_detallados", kwargs={"proyecto_id": self.id})
    