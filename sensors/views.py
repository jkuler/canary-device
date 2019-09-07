from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
# Create your views here.


class TemplateBase(TemplateView):
    """
     view that returns base template
    """
    def get(self, request, *args, **kwargs):

        template_name = 'base.html'
        return render(request, template_name)


class TemplateHome(TemplateView):
    """
    view that returns home template
    """
    def get(self, request, *args, **kwargs):
        template_name = 'sensors/home.html'
        return render(request, template_name)
