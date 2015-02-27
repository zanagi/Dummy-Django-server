from django.db import models

from django.utils import timezone

class Sensor(models.Model):
    sensor = models.CharField(max_length=250, unique=True)
    value = models.FloatField()

class DateManager(models.Model):
    time = models.DateTimeField()
