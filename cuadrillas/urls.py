from django.conf.urls import url

from .views import IntegranteCreateView, FamiliarCreateView, CuadrillaCreateView, CuadrillaListView,IntegranteListView,

urlpatterns = [
    url(r'^tarea', TareasCreateView.as_view(), name='tarea_nueva'),
    url(r'^nuevo', CasoCreateView.as_view(), name='caso_nuevo'),
    url(r'^', CasoListView.as_view(), name='caso_lista')
