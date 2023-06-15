from django.db import models
from django.contrib.auth.models import User


class Destinazione(models.Model):
    destinazione_id = models.PositiveIntegerField(primary_key=True)
    nome = models.CharField(max_length=100)
    descrizione = models.TextField()
    paese = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Prenotazione(models.Model):
    nome_completo = models.CharField(max_length=100, null=True)
    prenotazione_id = models.PositiveIntegerField(primary_key=True)
    destinazione = models.ForeignKey(Destinazione, on_delete=models.CASCADE)
    data_inizio = models.DateField()
    data_fine = models.DateField()
    numero_persone = models.PositiveIntegerField()
    prezzo = models.DecimalField(max_digits=6, decimal_places=2, null=True)

    def __str__(self):
        return self.prenotazione_id

class Struttura(models.Model):
    destinazione = models.ForeignKey(Destinazione, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    descrizione = models.TextField()
    indirizzo = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return self.nome
class Itinerario(models.Model):
    destinazione = models.ForeignKey(Destinazione, on_delete=models.CASCADE)
    titolo = models.CharField(max_length=100)
    descrizione = models.TextField()
    prezzo = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    day1 = models.CharField(max_length=200, blank=True, null=True)
    day2 = models.CharField(max_length=200, blank=True, null=True)
    day3 = models.CharField(max_length=200, blank=True, null=True)
    day4 = models.CharField(max_length=200, blank=True, null=True)
    day5 = models.CharField(max_length=200, blank=True, null=True)
    day6 = models.CharField(max_length=200, blank=True, null=True)
    day7 = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.titolo