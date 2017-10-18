from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    DeleteView,
    UpdateView,
    CreateView
)
from .models import Cuadrilla, Familiares, Integrante

#vista de la creación de un nuevo integrante
class IntegranteCreateView(CreateView):
    model = Integrante
    template_name = 'cuadrillas/integrante_nuevo.html'
    context_object_name = 'integrante_nuevo'


#vista de la creción de una nueva cuadrilla
class FamiliarCreateView(CreateView):
    model = Familiar
    fields = [
        'nombre',
        'patentesco',
        'telefono',
        'cuadrilla'
    ]
    template_name = 'cuadrillas/familiar_nuevo.html'
    # succes_url es la dirección a la que se redirige 
    # al ompletar la transacción sólo si es exitosa
    succes_url = reverse_lazy('cuadrilla:familiar_list')



#vista de la creación de una nueva cuadrilla
class CuadrillaCreateView(CreateView):
    model = Cuadrilla
    fields = [
        'fecha_creacion',
    ]
    def __str__(self):
        return self.fecha_creacion

#vista de la lista de cuadrillas
class CuadrillaListView(ListView):
    model = Cuadrilla
    template_name = 'cuadrillas/cuadrillas_list.html'
    context_object_name = 'cuadrillas'

class IntegranteListView(ListView):
    model = Integrante
    template_name = 'cuadrillas/integrantes_list.html'
    context_object_name = 'integrantes'
