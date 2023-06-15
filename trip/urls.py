from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('prenotazioni', views.visualizza_prenotazioni, name='prenotazioni'),
    path('search_destinations', views.search_destinations, name='search_destinations'),
    path('destinations/<str:nome>', views.destination_details, name='destination'),
    path('destinations', views.destinations, name='destinations'),
    path('add_itinerary', views.add_itinerary, name='add_itinerary'),
    path('add_prenotation/<str:destinazione_nome>', views.add_prenotation, name='add_prenotation'),
    path('about', views.about, name='about'),
]

