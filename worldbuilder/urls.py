from django.conf.urls import url

from . import views

app_name = 'worldbuilder'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<world>[a-z][0-9]+)/$', views.WorldView.as_view(), name='world'),
    url(r'^(?P<world>[0-9]{4})/(?P<entry>[0-9]{2})/$', views.EntryView.as_view(), name='entry'),
]
