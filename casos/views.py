from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    DeleteView,
    UpdateView,
    CreateView
)

from .models import Caso, Tarea


class CasoListView(ListView):
    model = Caso
    template_name = 'casos/caso_list.html'
    context_object_name = 'casos'


class CasoCreateView(CreateView):
    model = Caso
    fields = [
        'fecha_inicio',
        'fecha_final',
        'nombre',
        'tipo',
        'descripcion',
        'direccion',
        'estado',
        'tareas'
    ]
    template_name = 'casos/caso_form.html'
    success_url = reverse_lazy('casos:caso_lista')

class TareasCreateView(CreateView):
    model = Tarea
    fields = [
        'nombre',
        'duracion',
        'estado',
    ]
    template_name = 'casos/tarea_form.html'
    success_url = reverse_lazy('casos:caso_lista')
