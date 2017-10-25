from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    DeleteView,
    UpdateView,
    CreateView
)
from .models import Cuadrilla, Familiar, Integrante

#vista de la creación de un nuevo integrante
class IntegranteCreateView(CreateView):
    model = Integrante
    fields = [
    'nombre',
    'apellido',
    'fecha_nacimiento',
    'direccion',
    'tipo',
    'cuadrilla',
    ]
    template_name = 'cuadrillas/integrante_nuevo.html'
    success_url = reverse_lazy('cuadrillas:lista_integrantes')

class IntegranteListView(ListView):
    model = Integrante
    template_name = 'cuadrillas/integrantes_list.html'
    context_object_name = 'integrantes'
#vista de la creción de una nueva cuadrilla

class IntegranteUpdateView(UpdateView):
    model = Integrante
    fields = [
    'nombre',
    'apellido',
    'fecha_nacimiento',
    'direccion',
    'tipo',
    'cuadrilla',
    ]
    template_name = 'cuadrillas/integrante_nuevo.html'
    success_url = reverse_lazy('cuadrillas:lista_integrantes')

class IntegranteDeleteView(DeleteView):
    model = Integrante
    fields = [
    'nombre',
    'apellido',
    'fecha_nacimiento',
    'direccion',
    'tipo',
    'cuadrilla',
    ]
    template_name = 'cuadrillas/integrante_delete.html'
    success_url = reverse_lazy('cuadrillas:lista_integrantes')

class FamiliarCreateView(CreateView):
    model = Familiar
    fields = [
        'nombre',
        'parentesco',
        'telefono',
        'integrante'
    ]
    template_name = 'cuadrillas/familiar_nuevo.html'
    # succes_url es la dirección a la que se redirige
    # al ompletar la transacción sólo si es exitosa
    success_url = reverse_lazy('cuadrillas:lista_familiar')

    def __str__(self):
        return self.nombre

class FamiliarListView(ListView):
        model = Familiar
        template_name = 'cuadrillas/familiar_list.html'
        context_object_name = 'familiar'

class FamiliarUpdateView(UpdateView):
    model = Familiar
    fields = [
        'nombre',
        'parentesco',
        'telefono',
        'integrante'
    ]
    template_name = 'cuadrillas/familiar_nuevo.html'
    success_url = reverse_lazy('cuadrillas:lista_familiar')

class FamiliarDeleteView(DeleteView):
    model = Familiar
    fields = [
        'nombre',
        'parentesco',
        'telefono',
        'integrante'
    ]
    template_name = 'cuadrillas/familiar_delete.html'
    success_url = reverse_lazy('cuadrillas:lista_familiar')



#vista de la creación de una nueva cuadrilla
class CuadrillaCreateView(CreateView):
    model = Cuadrilla
    fields = [
        'fecha_creacion',
    ]
    template_name = 'cuadrillas/cuadrilla_nuevo.html'
    # succes_url es la dirección a la que se redirige
    # al ompletar la transacción sólo si es exitosa
    success_url = reverse_lazy('cuadrillas:lista_cuadrilla')

    def __str__(self):
        return self.fecha_creacion

#vista de la lista de cuadrillas
class CuadrillaListView(ListView):
    model = Cuadrilla
    template_name = 'cuadrillas/cuadrillas_list.html'
    context_object_name = 'cuadrillas'

class CuadrillaUpdateView(UpdateView):
    model = Cuadrilla
    fields = [
        'fecha_creacion',
    ]
    template_name = 'cuadrillas/cuadrilla_nuevo.html'
    success_url = reverse_lazy('cuadrillas:lista_cuadrilla')

class CuadrillaDeleteView(DeleteView):
    model = Cuadrilla
    fields = [
        'fecha_creacion',
    ]
    template_name = 'cuadrillas/cuadrilla_delete.html'
    success_url = reverse_lazy('cuadrillas:lista_cuadrilla')
