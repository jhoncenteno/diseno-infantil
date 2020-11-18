from django.db import models

# Create your models here.

class Servicios(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = models.CharField(max_length=150)
    imagen = models.ImageField(upload_to='Servicios')
    url = models.URLField(blank=True)                   
    created = models.DateTimeField(auto_now_add=True)   
    updated = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return self.titulo 

class Miembros(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = models.CharField(max_length=150)
    imagen = models.ImageField(upload_to='Miembros')
    created = models.DateTimeField(auto_now_add=True)  
    updated = models.DateTimeField(auto_now_add=True)  
  
    def __str__(self):
        return self.titulo 