from django.test import TestCase


class HomePage(TestCase):

    def test_can_get_base_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'base.html')

    def test_can_get_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')