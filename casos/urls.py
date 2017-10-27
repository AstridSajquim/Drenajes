from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from .views import CasoCreateView, CasoListView, TareaCreateView, TareaListView, TareaUpdateView, TareaDeleteView, CasoUpdateView, CasoDeleteView

# Estas son la urls de casos
urlpatterns = [
    url(r'^eliminartarea/(?P<pk>\d+)/', login_required(TareaDeleteView.as_view()), name='eliminar_tarea'),
    url(r'^editartarea/(?P<pk>\d+)/', login_required(TareaUpdateView.as_view()), name='editar_tarea'),
    url(r'^listatarea', login_required(TareaListView.as_view()), name='tarea_lista'),
    url(r'^tarea', login_required(TareaCreateView.as_view()), name='tarea_nueva'),

    url(r'^eliminarcaso/(?P<pk>\d+)/', login_required(CasoDeleteView.as_view()), name='eliminar_caso'),
    url(r'^editarcaso/(?P<pk>\d+)/', login_required(CasoUpdateView.as_view()), name='editar_caso'),
    url(r'^listacaso', login_required(CasoListView.as_view()), name='caso_lista'),
    url(r'^nuevo', login_required(CasoCreateView.as_view()), name='caso_nuevo')
]
