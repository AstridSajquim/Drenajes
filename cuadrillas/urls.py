from django.conf.urls import url

from .views import IntegranteCreateView, FamiliarDeleteView, FamiliarUpdateView, FamiliarCreateView, FamiliarListView, IntegranteUpdateView, IntegranteDeleteView, CuadrillaUpdateView, CuadrillaCreateView, CuadrillaListView, IntegranteListView, CuadrillaDeleteView

urlpatterns = [
    url(r'^eliminarfamiliar/(?P<pk>\d+)/', FamiliarDeleteView.as_view(), name='eliminar_familiar'),
    url(r'^editarfamiliar/(?P<pk>\d+)/', FamiliarUpdateView.as_view(), name='editar_familiar'),
    url(r'^listafamiliar', FamiliarListView.as_view(), name='lista_familiar'),
    url(r'^nuevofamiliar', FamiliarCreateView.as_view(), name='familiar_nuevo'),

    url(r'^eliminarintegrante/(?P<pk>\d+)/', IntegranteDeleteView.as_view(), name='eliminar_integrante'),
    url(r'^editarintegrante/(?P<pk>\d+)/', IntegranteUpdateView.as_view(), name='editar_integrante'),
    url(r'^listaintegrantes', IntegranteListView.as_view(), name='lista_integrantes'),
    url(r'^nuevointegrante', IntegranteCreateView.as_view(), name='integrante_nuevo'),

    url(r'^eliminarcuadrilla/(?P<pk>\d+)/', CuadrillaDeleteView.as_view(), name='eliminar_cuadrilla'),
    url(r'^editarcuadrilla/(?P<pk>\d+)/', CuadrillaUpdateView.as_view(), name='editar_cuadrilla'),
    url(r'^listacuadrilla', CuadrillaListView.as_view(), name='lista_cuadrilla'),
    url(r'^nuevacuadrilla', CuadrillaCreateView.as_view(), name='cuadrilla_nueva'),
    ]
