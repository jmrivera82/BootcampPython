from django.test import SimpleTestCase


class InicioTests(SimpleTestCase):

    def test_url_exists_at_correct_location(self):
        response = self.client.get('/laboratorio/test/')
        self.assertEqual(response.status_code, 200)
    def test_url_available_by_name(self):
        response = self.client.get('/laboratorio/test/')
        self.assertEqual(response.status_code, 200)
    def test_template_name_correct(self):
        response = self.client.get('/laboratorio/test/')
        self.assertTemplateUsed(response,'laboratorio/test.html')
    def test_template_content(self):
        response = self.client.get('/laboratorio/test/')
        self.assertContains(response, "<h1>Página de test</h1>")
        self.assertNotContains(response, "No es la Página")