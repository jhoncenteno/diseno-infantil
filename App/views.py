from django.shortcuts import render
from AppServicios.models import Servicios, Miembros
from django.conf import settings
from django.core.mail import send_mail


def home(request):
    
    servicios= Servicios.objects.all()
    miembros= Miembros.objects.all()

    return render(request, '1home.html', { "servicios" : servicios, "miembros" : miembros })



def contacto(request):

    if request.method == 'POST':    
        
        name = request.POST['nombre']                                                              
        message = request.POST['mensaje'] + '\n\nMensaje escrito por: ' + request.POST['email']     
        email_from= settings.EMAIL_HOST_USER                                                        
        recipient_list = ['centenojhon100598@gmail.com']                                            
        
        send_mail(name, message, email_from, recipient_list)           
        
        return render(request, '4mensaje_enviado.html')  
         

    return render(request, '1home.html') 