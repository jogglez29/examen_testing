from django.test import TestCase
from usuarios.forms import UsuarioForm


class TestFromUsuario(TestCase):

    def test_usuario_nombre_vacio(self):
        form = UsuarioForm(
            data={
                'first_name': '',
                'last_name': 'Gonzalez',
                'segundo_apellido': 'Pinedo',
                'username': 'jozuelenuv_1',
                'password': 'jozue123'
            }

        )
        self.assertFalse(form.is_valid())

    def test_usuario_last_name_vacio(self):
        form = UsuarioForm(
            data={
                'first_name': 'Josue',
                'last_name': '',
                'segundo_apellido': 'Pinedo',
                'username': 'jozuelenuv_1',
                'password': 'jozue123'
            }

        )
        self.assertFalse(form.is_valid())

    def test_usuario_segundo_apellido_vacio(self):
        form = UsuarioForm(
            data={
                'first_name': 'Josue',
                'last_name': 'Gonzalez',
                'segundo_apellido': '',
                'username': 'jozuelenuv_1',
                'password': 'jozue123'
            }

        )
        self.assertTrue(form.is_valid())

    def test_usuario_username_vacio(self):
        form = UsuarioForm(
            data={
                'first_name': 'Josue',
                'last_name': 'Gonzalez',
                'segundo_apellido': 'Pinedo',
                'username': '',
                'password': 'jozue123'
            }

        )
        self.assertFalse(form.is_valid())

    def test_usuario_password_vacio(self):
        form = UsuarioForm(
            data={
                'first_name': 'Josue',
                'last_name': 'Gonzalez',
                'segundo_apellido': 'Pinedo',
                'username': 'jozuelenuv_1',
                'password': ''
            }

        )
        self.assertFalse(form.is_valid())

    def test_usuario_campos_correctos(self):
        form = UsuarioForm(
            data={
                'first_name': 'Josue',
                'last_name': 'Gonzalez',
                'segundo_apellido': 'Pinedo',
                'username': 'jozuelenuv_1',
                'password': 'jozue123'
            }

        )
        self.assertTrue(form.is_valid())

    def test_usuario_nombre_caracteres_especiales(self):
        form = UsuarioForm(
            data={
                'first_name': 'Josue#$#$',
                'last_name': 'Gonzalez',
                'segundo_apellido': 'Pinedo',
                'username': 'jozuelenuv_1',
                'password': 'jozue123'
            }

        )
        self.assertFalse(form.is_valid())

    def test_usuario_nombre_caracteres_numericos(self):
        form = UsuarioForm(
            data={
                'first_name': '222Josue11',
                'last_name': 'Gonzalez',
                'segundo_apellido': 'Pinedo',
                'username': 'jozuelenuv_1',
                'password': 'jozue123'
            }

        )
        self.assertFalse(form.is_valid())

    def test_usuario_last_name_caracteres_especiales(self):
        form = UsuarioForm(
            data={
                'first_name': 'Josue',
                'last_name': 'Gonzalez/(&!',
                'segundo_apellido': 'Pinedo',
                'username': 'jozuelenuv_1',
                'password': 'jozue123'
            }

        )
        self.assertFalse(form.is_valid())

    def test_usuario_last_name_caracteres_numericos(self):
        form = UsuarioForm(
            data={
                'first_name': 'Josue',
                'last_name': 'Gonzalez534534534',
                'segundo_apellido': 'Pinedo',
                'username': 'jozuelenuv_1',
                'password': 'jozue123'
            }

        )
        self.assertFalse(form.is_valid())

    def test_usuario_segundo_apellido_caracteres_especiales(self):
        form = UsuarioForm(
            data={
                'first_name': 'Josue',
                'last_name': 'Gonzalez',
                'segundo_apellido': '##$Pined!!!o',
                'username': 'jozuelenuv_1',
                'password': 'jozue123'
            }

        )
        self.assertFalse(form.is_valid())

    def test_usuario_segundo_apellido_caracteres_numéricos(self):
        form = UsuarioForm(
            data={
                'first_name': 'Josue',
                'last_name': 'Gonzalez',
                'segundo_apellido': 'P1n3d0',
                'username': 'jozuelenuv_1',
                'password': 'jozue123'
            }

        )
        self.assertFalse(form.is_valid())

    def test_usuario_username_longitud_21(self):
        form = UsuarioForm(
            data={
                'first_name': 'Josue',
                'last_name': 'Gonzalez',
                'segundo_apellido': 'Pinedo',
                'username': 'jozuelenuv_1345678901',
                'password': 'jozue123'
            }

        )
        self.assertFalse(form.is_valid())

    def test_usuario_username_espacios(self):
        form = UsuarioForm(
            data={
                'first_name': 'Josue',
                'last_name': 'Gonzalez',
                'segundo_apellido': 'Pinedo',
                'username': 'jozue lenuv',
                'password': 'jozue123'
            }

        )
        self.assertFalse(form.is_valid())

    def test_usuario_username_longitud_20(self):
        form = UsuarioForm(
            data={
                'first_name': 'Josue',
                'last_name': 'Gonzalez',
                'segundo_apellido': 'Pinedo',
                'username': 'jozuelenuv_134567890',
                'password': 'jozue123'
            }

        )
        self.assertTrue(form.is_valid())

    def test_usuario_password_longitud_21(self):
        form = UsuarioForm(
            data={
                'first_name': 'Josue',
                'last_name': 'Gonzalez',
                'segundo_apellido': 'Pinedo',
                'username': 'jozuelenuv_1',
                'password': 'jozue1234567890123456'
            }

        )
        self.assertFalse(form.is_valid())

    def test_usuario_password_longitud_20(self):
        form = UsuarioForm(
            data={
                'first_name': 'Josue',
                'last_name': 'Gonzalez',
                'segundo_apellido': 'Pinedo',
                'username': 'jozuelenuv_1',
                'password': 'jozue123456789012345'
            }

        )
        self.assertTrue(form.is_valid())

    def test_usuario_nombre_longitud_46(self):
        form = UsuarioForm(
            data={
                'first_name': 'Nominchuluunukhaanzayamunkherdeneenkhtuguldurf',
                'last_name': 'Gonzalez',
                'segundo_apellido': 'Pinedo',
                'username': 'jozuelenuv_1',
                'password': 'jozue1234567890123456'
            }

        )
        self.assertFalse(form.is_valid())

    def test_usuario_nombre_longitud_45(self):
        form = UsuarioForm(
            data={
                'first_name': 'Nominchuluunukhaanzayamunkherdeneenkhtuguldur',
                'last_name': 'Gonzalez',
                'segundo_apellido': 'Pinedo',
                'username': 'jozuelenuv_1',
                'password': 'jozue1234567890123456'
            }

        )
        self.assertFalse(form.is_valid())

    def test_usuario_last_name_longitud_36(self):
        form = UsuarioForm(
            data={
                'first_name': 'Josue',
                'last_name': 'Nominchuluunukhaanzayamunkherdeneenk',
                'segundo_apellido': 'Pinedo',
                'username': 'jozuelenuv_1',
                'password': 'jozue123'
            }

        )
        self.assertFalse(form.is_valid())

    def test_usuario_last_name_longitud_35(self):
        form = UsuarioForm(
            data={
                'first_name': 'Josue',
                'last_name': 'Nominchuluunukhaanzayamunkherdeneen',
                'segundo_apellido': 'Pinedo',
                'username': 'jozuelenuv_1',
                'password': 'jozue123'
            }

        )
        self.assertTrue(form.is_valid())

    def test_usuario_segundo_apellido_longitud_36(self):
        form = UsuarioForm(
            data={
                'first_name': 'Josue',
                'last_name': 'Gonzalez',
                'segundo_apellido': 'Nominchuluunukhaanzayamunkherdeneenk',
                'username': 'jozuelenuv_1',
                'password': 'jozue123'
            }

        )
        self.assertFalse(form.is_valid())

    def test_usuario_segundo_apellido_longitud_35(self):
        form = UsuarioForm(
            data={
                'first_name': 'Josue',
                'last_name': 'Gonzalez',
                'segundo_apellido': 'Nominchuluunukhaanzayamunkherdeneen',
                'username': 'jozuelenuv_1',
                'password': 'jozue123'
            }

        )
        self.assertTrue(form.is_valid())
