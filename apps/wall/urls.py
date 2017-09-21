from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.wall_index, name='wall_index'),
    url(r'^signin$', views.sign_in, name='sign_in'),
    url(r'^register$', views.register, name='register'),
    url(r'^dashboard$', views.dashboard, name='dashboard'),
    url(r'^dashboard/admin$', views.dashboard_admin, name='dashboard_admin'),
]
