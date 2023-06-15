from django.contrib import admin
from .models import Destinazione, Prenotazione, Struttura, Itinerario

admin.site.register(Destinazione)
admin.site.register(Prenotazione)
admin.site.register(Struttura)
admin.site.register(Itinerario)
