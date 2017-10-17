from django.conf.urls import url

from .views import CasoCreateView, CasoListView, TareasCreateView

urlpatterns = [
    url(r'^tarea', TareasCreateView.as_view(), name='tarea_nueva'),
    url(r'^nuevo', CasoCreateView.as_view(), name='caso_nuevo'),
    url(r'^', CasoListView.as_view(), name='caso_lista')

]
