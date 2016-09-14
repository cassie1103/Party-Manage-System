__author__ = 'adwo15511'

from django.conf.urls import url
from guest import views_interface

urlpatterns = [
    url(r'^add_event/$', views_interface.add_event),
    url(r'^search_event/$', views_interface.search_event),
]

