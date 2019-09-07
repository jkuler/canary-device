from django.test import TestCase
from sensors.models import Device
from django.utils.timezone import now

class DeviceModelTest(TestCase):

    def test_device_model_attributes(self):
        device = Device()
        self.assertEqual(device.sensor_type, 'temperature')
        self.assertIsNone(device.sensor_value, 'device_value should not be empty')

    def test_should_save_device_record(self):
        device = Device(sensor_reading_time=now(), sensor_value=2.0)
        device.save()

    def test_can_retrieve_data(self):
        device = Device.objects.create(sensor_value=2.1, sensor_type='humility')
        device.save()
        self.assertEqual(
            Device.objects.all().count(),
            1
        )

