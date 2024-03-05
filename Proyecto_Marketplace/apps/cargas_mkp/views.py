import datetime
from typing import Any
from django.db.models import Q
from django.shortcuts import render
from .forms import VistaOfertasSeller
from django.views.generic import (
    TemplateView,
    ListView
)
from .models import *
# Create your views here.
class FechaMixin(object):
     
    def get_context_data(self, **kwargs):
         context = super(FechaMixin, self).get_context_data(**kwargs)
         context['fecha'] = datetime.datetime.now()
         return context
    
class OfertasSellerCount(ListView):
    model:CatOfertasmarketplace
    template_name = "Ofertas_por_seller.html"
    form_class = VistaOfertasSeller
    context_object_name = 'catoffer' 

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        lista = CatOfertasmarketplace.objects.filter(
            Q(nom_parentpartnumber = palabra_clave) | Q( nom_tienda= palabra_clave) #| Q(idu_tienda = palabra_clave)           
        )
        print(lista)
        return lista 



class HomeView(FechaMixin, TemplateView):
    template_name = "index.html"
    
