from typing import ValuesView
from django.contrib import admin
from django.urls import path
from . import views

app_name = "carga_mkp"
urlpatterns = [
    #path('admin/', admin.site.urls),
    path('home',views.HomeView.as_view(), name='inicio'),
    path('listviewOfferSeller/',views.OfertasSellerCount.as_view(), name='listOfferSeller'),
]
