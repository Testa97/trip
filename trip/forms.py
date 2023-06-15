from django import forms
from django.forms import ModelForm
from .models import Itinerario, Prenotazione
class ItinerarioForm(ModelForm):
    class Meta:
        model = Itinerario
        fields = ('destinazione', 'titolo', 'descrizione', 'day1', 'day2', 'day3', 'day4', 'day5', 'day6', 'day7')
        labels = {
            'destinazione': 'Destinazione',
            'titolo': 'Titolo',
            'descrizione': 'Descrizione',
            'day1': 'Giorno 1',
            'day2': 'Giorno 2',
            'day3': 'Giorno 3',
            'day4': 'Giorno 4',
            'day5': 'Giorno 5',
            'day6': 'Giorno 6',
            'day7': 'Giorno 7',
        }
        widgets = {
            'destinazione': forms.Select(attrs={'class': 'form-control'}),
            'titolo': forms.TextInput(attrs={'class': 'form-control'}),
            'descrizione': forms.Textarea(attrs={'class': 'form-control'}),
            'day1': forms.TextInput(attrs={'class': 'form-control'}),
            'day2': forms.TextInput(attrs={'class': 'form-control'}),
            'day3': forms.TextInput(attrs={'class': 'form-control'}),
            'day4': forms.TextInput(attrs={'class': 'form-control'}),
            'day5': forms.TextInput(attrs={'class': 'form-control'}),
            'day6': forms.TextInput(attrs={'class': 'form-control'}),
            'day7': forms.TextInput(attrs={'class': 'form-control'}),
        }

class PrenotationForm(ModelForm):
    class Meta:
        model = Prenotazione
        fields = ('nome_completo', 'destinazione', 'data_inizio', 'data_fine', 'numero_persone')
        labels = {
            'nome_completo': 'Nome e cognome',
            'destinazione': 'Destinazione',
            'data_inizio': 'Data inizio',
            'data_fine': 'Data fine',
            'numero_persone': 'Numero persone',
        }
        widgets = {
            'nome_completo': forms.TextInput(attrs={'class': 'form-control'}),
            'destinazione': forms.Select(attrs={'class': 'form-control'}),
            'data_inizio': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'data_fine': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'numero_persone': forms.NumberInput(attrs={'class': 'form-control'}),
        }
