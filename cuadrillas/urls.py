from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import IntegranteCreateView, FamiliarDeleteView, FamiliarUpdateView, FamiliarCreateView, FamiliarListView, IntegranteUpdateView, IntegranteDeleteView, CuadrillaUpdateView, CuadrillaCreateView, CuadrillaListView, IntegranteListView, CuadrillaDeleteView

urlpatterns = [
    url(r'^eliminarfamiliar/(?P<pk>\d+)/', login_required(FamiliarDeleteView.as_view()), name='eliminar_familiar'),
    url(r'^editarfamiliar/(?P<pk>\d+)/', login_required(FamiliarUpdateView.as_view()), name='editar_familiar'),
    url(r'^listafamiliar', login_required(FamiliarListView.as_view()), name='lista_familiar'),
    url(r'^nuevofamiliar', login_required(FamiliarCreateView.as_view()), name='familiar_nuevo'),

    url(r'^eliminarintegrante/(?P<pk>\d+)/', login_required(IntegranteDeleteView.as_view()), name='eliminar_integrante'),
    url(r'^editarintegrante/(?P<pk>\d+)/', login_required(IntegranteUpdateView.as_view()), name='editar_integrante'),
    url(r'^listaintegrantes', login_required(IntegranteListView.as_view()), name='lista_integrantes'),
    url(r'^nuevointegrante', login_required(IntegranteCreateView.as_view()), name='integrante_nuevo'),

    url(r'^eliminarcuadrilla/(?P<pk>\d+)/', login_required(CuadrillaDeleteView.as_view()), name='eliminar_cuadrilla'),
    url(r'^editarcuadrilla/(?P<pk>\d+)/', login_required(CuadrillaUpdateView.as_view()), name='editar_cuadrilla'),
    url(r'^listacuadrilla', login_required(CuadrillaListView.as_view()), name='lista_cuadrilla'),
    url(r'^nuevacuadrilla', login_required(CuadrillaCreateView.as_view()), name='cuadrilla_nueva'),
    ]
