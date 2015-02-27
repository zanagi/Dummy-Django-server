import django.views.generic
from django.shortcuts import render, render_to_response

from django.http import JsonResponse, HttpResponse

from shorturl.sensors.models import Sensor, DateManager

from random import randint
from django.utils import timezone

class SensorData(django.views.generic.View):
    """
       Fake sensor data
    """

    def get(self, request):
        sensors = {}
        current_time = timezone.now()
        
        try:
            manager = DateManager.objects.get(pk=1)
        except DateManager.DoesNotExist:
            manager = DateManager(time=current_time)

        delta = current_time - manager.time
        overtime = delta.seconds >= 280

        # little less than 5 minutes
        if overtime:
            manager.update(time=current_time)
            manager.save()
        for s in Sensor.objects.order_by('-sensor'):
            #Update sensor value
            if overtime:
                old_value = s.value
                coeff = (10 - randint(0,20)) / 100.0
                new_value = old_value * (1 - coeff)

                if old_value * new_value >= 0:
                    s.update(value=new_value)
                    s.save()
                    
            # optimize string length
            temp1 = str(s.value)
            temp2 = temp1.split(".")
            temp3 = len(temp2[1])
            if temp3 > 2:
                string = ("%.2f" % s.value)
            else:
                string = str(s.value)
                
            sensors[s.sensor] = string
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
            Sensor.objects.get(sensor=sensor).save()
        except BaseException as e:
            print("error:" + str(e))
            return HttpResponse(status=500)
            
        return HttpResponse(status=200)
        
