from django import forms
from .models import Usuario
from django.core.validators import RegexValidator


class UsuarioForm(forms.ModelForm):
    first_name = forms.CharField(initial=' ', 
                                 error_messages={
                                     'required': 'Completa este campo'},
                                 max_length=45,
                                 min_length=1,
                                 label='Nombre',
                                 validators=[
                                     RegexValidator(regex='^[a-zA-Z\s]*$',
                                                    message='El nombre debe contener solamente letras del alfabeto latino')]
                                 )
    last_name = forms.CharField(initial=' ', 
                                error_messages={
                                    'required': 'Completa este campo'},
                                max_length=35,
                                min_length=1,
                                label='Primer apellido',
                                validators=[
                                    RegexValidator(regex='^[a-zA-Z]*$',
                                                   message='El apellido debe contener solamente letras del alfabeto latino')]
                                )
    username = forms.CharField(initial=' ', 
                               error_messages={
                                   'required': 'Completa este campo',
                                   'invalid': 'El usuario no debe contener espacios'},
                               max_length=20,
                               min_length=1,
                               label='Usuario'
                               )
    segundo_apellido = forms.CharField(required=False,
                                       validators=[RegexValidator(
                                           regex='^[a-zA-Z]*$',
                                           message='El apellido debe contener solamente letras del alfabeto latino')]
                                       )
    password = forms.CharField(initial=' ', 
                               error_messages={
                                   'required': 'Completa este campo'},
                               max_length=20,
                               min_length=1, 
                               widget=forms.PasswordInput,
                               label='Contraseña'
                               )

    class Meta:
        model = Usuario

        fields = ('first_name', 'last_name',
                  'segundo_apellido', 'username', 'password')

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'segundo_apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }

        help_texts = {
            'username': None
        }

        def save(self, commit=True):
            user = super(UsuarioForm, self).save(commit=False)
            user.set_password(self.cleaned_data['password'])
            if commit:
                user.save()
            return user
