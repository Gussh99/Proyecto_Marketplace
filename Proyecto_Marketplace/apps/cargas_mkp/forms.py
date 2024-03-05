from django import forms
from . models import CatOfertasmarketplace
from django.forms.models import ModelForm

class VistaOfertasSeller(forms.ModelForm):

    class Meta:
        model:CatOfertasmarketplace