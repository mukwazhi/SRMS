from django.db import models

# Create your models here.

class Flight_Detail(models.Model):
    flightNumber = models.CharField(max_length=10)
    registration = models.CharField(max_length=20)
    aircraftType = models.CharField(max_length=20)
    capacity = models.IntegerField()

    def __str__(self):
        return self.flightNo


class Flight_Movement(models.Model):
    flightNumber = models.ForeignKey(Flight_Detail, on_delete=models.DO_NOTHING)
    routing = models.CharField(max_length=20)
    arrivalTime = models.TimeField()
    departureTime = models.TimeField()
    cargoIn = models.IntegerField()
    cargoOut = models.IntegerField()
    mailIn  = models.IntegerField()
    mailOut = models.IntegerField()
    PaxIn = models.IntegerField()
    PaxOut = models.IntegerField()
    pad = models.IntegerField()
    asu = models.IntegerField()
    gpu = models.IntegerField()
    toiletBowser = models.IntegerField()
    pau = models.IntegerField()
    waterCart = models.IntegerField()

    def __str__(self):
        return self.routing
