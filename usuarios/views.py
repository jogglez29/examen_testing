from django.views.generic.edit import CreateView
from django.views.generic import ListView
from django.urls import reverse_lazy

from usuarios.models import Usuario
from .forms import UsuarioForm


class NuevoUsuario(CreateView):
    model = Usuario
    template_name = 'usuarios/usuario_form.html'
    form_class = UsuarioForm
    extra_context = {'btn': 'Agregar'}
    success_url = reverse_lazy('usuarios:lista')

    def form_valid(self, form):
        form.save(commit=False)
        return super().form_valid(form)


class UsuarioList(ListView):
    model = Usuario
    template_name = 'usuarios/usuario_list.html'
