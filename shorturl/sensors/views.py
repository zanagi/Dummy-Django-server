from django.shortcuts import render

from django.http import JsonResponse

class SensorData(django.views.generic.View):
    """
       Fake sensor data
    """

    def get(self, request):
        return JsonResponse({'foo':'bar'})
