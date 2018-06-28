"""
Author: harsh
"""
from django.conf.urls import url
from website import views

urlpatterns = [
    url('events/$', views.EventList.as_view())
]
