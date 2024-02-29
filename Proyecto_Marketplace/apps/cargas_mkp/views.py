import datetime
from django.shortcuts import render
from django.views.generic import (
    TemplateView,
)


# Create your views here.
class FechaMixin(object):
     
    def get_context_data(self, **kwargs):
         context = super(FechaMixin, self).get_context_data(**kwargs)
         context['fecha'] = datetime.datetime.now()
         return context


class HomeView(FechaMixin, TemplateView):
    template_name = "index.html"
    
