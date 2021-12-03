from django.test import TestCase
from usuarios.models import Usuario
from django.urls import reverse


class TestViews(TestCase):

    def test_url_registro_usuarios(self):
        response = self.client.get(reverse('usuarios:nuevo'))
        self.assertEqual(response.status_code, 200)

    def test_template_registro_usuarios(self):
        response = self.client.get(reverse('usuarios:nuevo'))
        self.assertTemplateUsed(response, 'usuarios/usuario_form.html')

    def test_url_lista_usuarios(self):
        response = self.client.get(reverse('usuarios:lista'))
        self.assertEqual(response.status_code, 200)

    def test_template_lista_usuarios(self):
        response = self.client.get(reverse('usuarios:lista'))
        self.assertTemplateUsed(response, 'usuarios/usuario_list.html')

    def test_usuario_se_encuentra_en_template(self):
        self.agrega_usuario()
        response = self.client.get(reverse('usuarios:lista'))
        self.assertContains(response, 'prueba')

    def test_usuario_se_encuentra_en_template_en_un_td(self):
        self.agrega_usuario()
        response = self.client.get(reverse('usuarios:lista'))
        self.assertInHTML('<td>prueba</td>', response.rendered_content)

    def test_nombre_se_encuentra_en_template(self):
        self.agrega_usuario()
        response = self.client.get(reverse('usuarios:lista'))
        self.assertContains(response, 'Benito Antonio')

    def test_nombre_se_encuentra_en_template_en_un_td(self):
        self.agrega_usuario()
        response = self.client.get(reverse('usuarios:lista'))
        self.assertInHTML('<td>Benito Antonio</td>', response.rendered_content)

    def test_primer_apellido_se_encuentra_en_template(self):
        self.agrega_usuario()
        response = self.client.get(reverse('usuarios:lista'))
        self.assertContains(response, 'Martinez')

    def test_primer_apellido_se_encuentra_en_template_en_un_td(self):
        self.agrega_usuario()
        response = self.client.get(reverse('usuarios:lista'))
        self.assertInHTML('<td>Martinez</td>', response.rendered_content)

    def test_segundo_apellido_se_encuentra_en_template(self):
        self.agrega_usuario()
        response = self.client.get(reverse('usuarios:lista'))
        self.assertContains(response, 'Ocasio')

    def test_segundo_apellido_se_encuentra_en_template_en_un_td(self):
        self.agrega_usuario()
        response = self.client.get(reverse('usuarios:lista'))
        self.assertInHTML('<td>Ocasio</td>', response.rendered_content)

    def agrega_usuario(self):
        return Usuario.objects.create(
            first_name='Benito Antonio',
            last_name='Martinez',
            segundo_apellido='Ocasio',
            username='prueba',
            password='1234'
        )
