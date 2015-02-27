from django.db import models


class Sensor(models.Model):
    sensor = models.CharField(max_length=250, unique=True)
    value = models.FloatField()
