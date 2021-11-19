from django.db import models


# Create your models here.
class Flight(models.Model):
    flight_no = models.IntegerField()
    depart_dt = models.DateTimeField()
    arrival_dt = models.DateTimeField()
    depart_airport = models.CharField(max_length=120)
    arrival_airport = models.CharField(max_length=120)