from django.contrib import admin

from shorturl.sensors.models import Sensor

# Register your models here.
class SensorAdmin(admin.ModelAdmin):
    pass

admin.site.register(Sensor, SensorAdmin)
