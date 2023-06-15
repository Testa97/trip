from django.shortcuts import render
from .models import Destinazione, Struttura, Prenotazione, Itinerario
from django.http import HttpResponseRedirect
from .forms import ItinerarioForm, PrenotationForm
from django.shortcuts import get_object_or_404
# Create your views here.
def visualizza_prenotazioni(request):
    prenotazioni = Prenotazione.objects.all()
    return render(request, "travel/prenotazioni.html", {"prenotazioni": prenotazioni})


def index(request):
    destinazioni = Destinazione.objects.all()
    return render(request, "travel/index.html", {"destinazioni": destinazioni})

def search_destinations(request):
    if request.method == "POST":
        searched = request.POST['searched']
        destinazioni = Destinazione.objects.filter(nome__contains=searched)
        return render(request, "travel/search_destinations.html", {'searched': searched, "destinazioni": destinazioni})
    else:
        return render(request, "travel/search_destinations.html", {})

def destinations(request):
    destinazioni = [
        {
            "nome": "Roma",
            "immagine": "static/images/roma.jpg",
        },
        {
            "nome": "Firenze",
            "immagine": "static/images/firenze2.jpeg",
        },
        {
            "nome": "Barcellona",
            "immagine": "static/images/barcellona.jpg",
        },
        {
            "nome": "Parigi",
            "immagine": "static/images/parigi2.jpeg",
        },
        {
            "nome": "New York",
            "immagine": "static/images/new_york2.jpeg",
        },
        {
            "nome": "Amsterdam",
            "immagine": "static/images/amsterdam.jpg",
        }
    ]

    context={
        "destinazioni": destinazioni
    }

    return render(request, "travel/destinations.html", context)

def destination_details(request, nome):
    destinazione = Destinazione.objects.get(nome=nome)
    strutture = Struttura.objects.filter(destinazione=destinazione)
    itinerari = Itinerario.objects.filter(destinazione=destinazione)

    context = {
        "destinazione": destinazione,
        "strutture": strutture,
        "itinerari": itinerari,
    }

    return render(request, "travel/destination_details.html", context)

def add_itinerary(request):
    submitted = False
    if request.method == "POST":
        form = ItinerarioForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_itinerary?submitted=True')
    else:
        form = ItinerarioForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, "travel/add_itinerary.html", {"form": form, "submitted": submitted})

def add_prenotation(request, destinazione_nome):
    submitted = False

    destinazione = get_object_or_404(Destinazione, nome=destinazione_nome)

    if request.method == "POST":
        form = PrenotationForm(request.POST, initial={'destinazione': destinazione})
        if form.is_valid():
            prenotazione = form.save(commit=False)
            itinerario = get_object_or_404(Itinerario, destinazione=destinazione)
            prenotazione.prezzo = itinerario.prezzo
            prenotazione.save()
            return HttpResponseRedirect('passenger_details?submitted=True')
    else:
        form = PrenotationForm(initial={'destinazione': destinazione})
        if 'submitted' in request.GET:
            submitted = True

    return render(request, "travel/add_prenotation.html", {"form": form, "submitted": submitted})


def about(request):
    return render(request, 'travel/aboutus.html')