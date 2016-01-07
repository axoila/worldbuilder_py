from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^worldbuilder/', include('worldbuilder.urls')),
    url(r'^admin/', admin.site.urls)
]
