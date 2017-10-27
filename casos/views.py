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

class CasoListView(ListView):
    model = Caso
    template_name = 'casos/caso_list.html'
    context_object_name = 'casos'
    def __str__(self):
        return self.nombre


class CasoUpdateView(UpdateView):
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

class CasoDeleteView(DeleteView):
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
    template_name = 'casos/caso_delete.html'
    success_url = reverse_lazy('casos:caso_lista')

class TareaCreateView(CreateView):
    model = Tarea
    fields = [
        'nombre',
        'duracion',
        'estado',
    ]
    template_name = 'casos/tarea_form.html'
    success_url = reverse_lazy('casos:tarea_lista')

class TareaListView(ListView):
    model = Tarea
    template_name = 'casos/tarea_list.html'
    context_object_name = 'tareas'

    def __str__(self):
        return self.nombre


class TareaUpdateView(UpdateView):
    model = Tarea
    fields = [
        'nombre',
        'duracion',
        'estado',
    ]
    template_name = 'casos/tarea_form.html'
    success_url = reverse_lazy('casos:tarea_lista')

class TareaDeleteView(DeleteView):
    model = Tarea
    fields = [
        'nombre',
        'duracion',
        'estado',
    ]
    template_name = 'casos/tarea_delete.html'
    success_url = reverse_lazy('casos:tarea_lista')
