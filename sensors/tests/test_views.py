from django.test import TestCase, SimpleTestCase
from django.urls import resolve
from sensors.views import TemplateHome
from django.test.client import RequestFactory
from django.urls.base import reverse


def setup_view_callable(view, request, *args, **kwargs):
    """
     Mimic as_view() callable at urls resolvers
     Returns view instance
    """
    view.request = request
    view.args = args
    view.kwargs = kwargs
    return view


class FTTest_HomePage(SimpleTestCase):

    def test_url_resolve_correct(self):
        found = resolve('/')
        self.assertEqual(found.view_name, 'home-page')

    def test_url_returns_correct_Template(self):
        response = self.client.get(
            reverse('home-page')
        )
        self.assertTemplateUsed(response, 'sensors/home.html')
        self.assertEqual(response.status_code, 200)
        html = response.content.decode('utf8')
        self.assertIn('<title>sensors app</title>', html)




