from django.db import models
from django.utils import timezone
from django_unixdatetimefield import UnixDateTimeField
import uuid


# Create your models here.
class Device(models.Model):
    device_uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    SENSOR_TYPE = (('humidity', 'Humidity'),
                   ('temperature', 'Temperature'))
    sensor_type = models.CharField(max_length=80, choices=SENSOR_TYPE,
                                   blank=False, null=False, default='temperature')
    sensor_value = models.DecimalField(max_digits=5, decimal_places=1, null=False, blank=False)
    sensor_reading_time = UnixDateTimeField(default=timezone.now)

    def __str__(self):
        return '{:12}, {}'.format(self.device_uuid, self.sensor_value)



