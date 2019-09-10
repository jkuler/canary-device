from rest_framework.serializers import ModelSerializer
from .models import Device


class DeviceSerializer(ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'

    def validate(self, attrs):
        instance = Device(**attrs)
        instance.clean()
        return attrs


class DeviceTimeSerializer(ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'
