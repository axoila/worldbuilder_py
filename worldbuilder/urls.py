from django.conf.urls import url

from . import views

app_name = 'worldbuilder'
urlpatterns = [
    url(r'^$', views.IndexView, name='index'),
    url(r'^(?P<user_name>[\w-]+)/$', views.userView, name='user'),
    url(r'^(?P<user_name>[\w-]+)/create/$', views.createEntry, name='createWorld'),
    url(r'^(?P<user_name>[\w-]+)/(?P<world_name>[\w-]+)/$', views.WorldView, name='world'),
    url(r'^(?P<user_name>[\w-]+)/(?P<world_name>[\w-]+)/create/$', views.WorldView, name='createEntry'),
    url(r'^(?P<user_name>[\w-]+)/(?P<world_name>[\w-]+)/(?P<entry_name>[\w-]+)/$', views.EntryView, name='entry'),
    # url(r'^(?P<question_id>[0-9]+)/modify/$', views.IndexView.as_view(), name='modify'),
]
