from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.wall_index, name='wall_index'),
    url(r'^signin$', views.sign_in, name='sign_in'),
    url(r'^register$', views.register, name='register'),
    url(r'^dashboard$', views.dashboard, name='dashboard'),
    url(r'^dashboard/admin$', views.dashboard_admin, name='dashboard_admin'),
    url(r'^users/show/(?P<user_id>\d+)$', views.user_show, name='user_show'),
    url(r'^users/edit/(?P<user_id>\d+)$', views.user_edit, name='user_edit'),
    url(r'^users/delete/(?P<user_id>\d+)$', views.user_delete, name='user_delete'),
    url(r'^users/(?P<user_id>\d+)/message/post$', views.message_post, name='message_post'),
    url(r'^users/(?P<user_id>\d+)/message/comment/(?P<for_msg_id>\d+)$',
        views.comment, name='comment'),
]
