
from django.shortcuts import render
from tienda.models import venta
# Create your views here.

def tienda(request):
    tienda=venta.objects.all()
    return render(request,"tienda/tienda.html",{"tienda":tienda})