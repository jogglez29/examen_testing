from django.test import TestCase
from usuarios.models import Usuario


class TestHumo(TestCase):

    def test_agrega_usuario(self):
        usuario = Usuario.objects.create(
            first_name='Juan Jose',
            last_name='Espinoza',
            segundo_apellido='Pinedo',
            username='prueba_models',
            password='1234'
        )

        usuario_uno = Usuario.objects.first()

        self.assertEqual(usuario_uno, usuario)
        self.assertEqual(usuario_uno.first_name, 'Juan Jose')
        self.assertEqual(str(usuario_uno), 'prueba_models')
        self.assertEqual(len(Usuario.objects.all()), 1)
