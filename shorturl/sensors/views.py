import django.views.generic
from django.shortcuts import render, render_to_response

from django.http import JsonResponse, HttpResponse

from shorturl.sensors.models import Sensor

class SensorData(django.views.generic.View):
    """
       Fake sensor data
    """

    def get(self, request):
        sensors = {}
        for s in Sensor.objects.order_by('-sensor'):
            sensors[s.sensor] = str(s.value)
        return JsonResponse(sensors)


class SensorAdder(django.views.generic.View):
    """
       View for adding sensors
    """

    def get(self, request):
        return render(request, 'shorturl.sensors/index.html', dict())

    def post(self, request):
        sensor = request.POST.get("sensor", "")
        value = request.POST.get("value", "")

        try:
            s = Sensor.objects.create(sensor=sensor,value=float(value))
            s.save()
        except django.db.IntegrityError:
            Sensor.objects.filter(sensor=sensor).update(value=value)
        except BaseException as e:
            print("error:" + str(e))
            return HttpResponse(status=500)
            
        return HttpResponse(status=200)
        
