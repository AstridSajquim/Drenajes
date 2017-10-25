from django.conf.urls import url

from .views import CasoCreateView, CasoListView, TareaCreateView, TareaListView, TareaUpdateView, TareaDeleteView, CasoUpdateView, CasoDeleteView

# Estas son la urls de casos
urlpatterns = [
    url(r'^eliminartarea/(?P<pk>\d+)/', TareaDeleteView.as_view(), name='eliminar_tarea'),
    url(r'^editartarea/(?P<pk>\d+)/', TareaUpdateView.as_view(), name='editar_tarea'),
    url(r'^listatarea', TareaListView.as_view(), name='tarea_lista'),
    url(r'^tarea', TareaCreateView.as_view(), name='tarea_nueva'),

    url(r'^eliminarcaso/(?P<pk>\d+)/', CasoDeleteView.as_view(), name='eliminar_caso'),
    url(r'^editarcaso/(?P<pk>\d+)/', CasoUpdateView.as_view(), name='editar_caso'),
    url(r'^listacaso', CasoListView.as_view(), name='caso_lista'),
    url(r'^nuevo', CasoCreateView.as_view(), name='caso_nuevo')
]
