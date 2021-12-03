from django.urls import path
from . import views

app_name = 'usuarios'

urlpatterns = [
    path('nuevo/', views.NuevoUsuario.as_view(), name='nuevo'),
    path('lista/', views.UsuarioList.as_view(), name='lista'),
]
