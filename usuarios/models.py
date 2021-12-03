from django.db import models
from django.contrib.auth.models import User


class Usuario(User):
    segundo_apellido = models.CharField(
        'Segundo apellido', max_length=35, null=True, blank=True)
