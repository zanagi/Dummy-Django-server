from django.db import models

class LongURL(models.Model):
    long_url = models.URLField()

