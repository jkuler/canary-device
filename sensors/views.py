from django.shortcuts import render
from django.http import Http404
from .models import Device
from .serializers import DeviceSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django.views.generic import TemplateView
from django.views.generic import View
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


class SimpleHelloWorld(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('<h1>hello world</h1>')


class SensorViewSet(ModelViewSet):
    """
     POST and PUT : create and update
    """

    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            {
             'message': 'device status set',
             'device_uuid': serializer.data['device_uuid']
            },
            status=status.HTTP_201_CREATED, headers=headers)





