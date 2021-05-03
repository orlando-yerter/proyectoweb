from django.shortcuts import render

# Create your views here.

def contacto(request):
    #contacto=servicio.objects.all()
    return render(request,"contacto/contacto.html")