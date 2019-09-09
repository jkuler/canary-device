from django.conf.urls import url, include
from sensors import views
from .views import SensorViewSet, SimpleHelloWorld
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'devices', SensorViewSet)

urlpatterns = [
    path('', SimpleHelloWorld.as_view(), name='hello-view'),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls')),

]


