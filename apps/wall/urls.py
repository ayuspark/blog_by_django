from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.wall_index, name='wall_index'),
]
