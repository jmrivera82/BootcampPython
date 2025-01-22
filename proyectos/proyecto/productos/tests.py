from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse

from .models import Proveedor

class InicioTests(SimpleTestCase):

    def test_url_exists_at_correct_location(self):
        response = self.client.get('/productos/test/')
        self.assertEqual(response.status_code, 200)
    def test_url_available_by_name(self):
        response = self.client.get('/productos/test/')
        self.assertEqual(response.status_code, 200)
    def test_template_name_correct(self):
        response = self.client.get('/productos/test/')
        self.assertTemplateUsed(response,'productos/test.html')
    def test_template_content(self):
        response = self.client.get('/productos/test/')
        self.assertContains(response, "<h1>Página de test</h1>")
        self.assertNotContains(response, "No es la Página")