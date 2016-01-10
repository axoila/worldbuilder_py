"""worldbuilder_py URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from . import views

app_name = 'base'
urlpatterns = [
    url(r'^admin/', admin.site.urls, name='admin'),
    url(r'^login/$',  views.login, name='login'),
    url(r'^auth/$',  views.auth_view, name='auth'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^loggedin/$', views.loggedin, name='loggedin'),
    url(r'^invalid/$', views.invalid_login, name='invalid'),
    url(r'^invalid/$', views.invalid_login, name='profile'),
    url(r'^register/$', views.register_user, name='register'),
    url(r'^register_success/$', views.register_success, name='register_success'),

    url(r'^', include('worldbuilder.urls')),
]
