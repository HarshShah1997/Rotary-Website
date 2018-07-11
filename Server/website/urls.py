"""
Author: harsh
"""
from django.conf.urls import url
from website import views

urlpatterns = [
    url('events/$', views.EventList.as_view()),
    url('announcements/$', views.AnnouncementList.as_view()),
    url('board_members/$', views.BoardMemberList.as_view()),
    url('photos/$', views.PhotoList.as_view()),
]
