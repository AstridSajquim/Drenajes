from django.conf.urls import url, include
from principal.views import index

urlpatterns = [
    url(r'^$', index),
]
