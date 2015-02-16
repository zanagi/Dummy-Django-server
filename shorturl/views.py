from django.shortcuts import render
import django.views.generic

class BaseView(django.views.generic.View):
    """
        Generic view infrastructure.
    """

    def render(self, request, template, **kwargs):
        return render(request, template, kwargs)
