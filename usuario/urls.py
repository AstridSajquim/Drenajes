from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from usuario.views import RegistroUsuario

urlpatterns = [
    url(r'^registrar', login_required(RegistroUsuario.as_view()), name='registrar_usuario'),
 ]
