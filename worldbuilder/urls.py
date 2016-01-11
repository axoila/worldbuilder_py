from django.conf.urls import url

from . import views

app_name = 'worldbuilder'
urlpatterns = [
    url(r'^$', views.IndexView, name='index'),
    url(r'^create/$', views.createEntry, name='createEntry'),
    url(r'^(?P<world_id>[\w-]+)/$', views.WorldView, name='world'),
    url(r'^(?P<world_id>[\w-]+)/(?P<entry_id>[\w-]+)/$', views.EntryView, name='entry'),
    # url(r'^(?P<question_id>[0-9]+)/modify/$', views.IndexView.as_view(), name='modify'),
]
