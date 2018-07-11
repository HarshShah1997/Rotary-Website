from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView

from website.serializers import *


class EventList(ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class AnnouncementList(ListAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer


class BoardMemberList(ListAPIView):
    queryset = BoardMember.objects.all()
    serializer_class = BoardMemberSerializer


class PhotoList(ListAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    filter_backends = (DjangoFilterBackend, )
    filter_fields = ('fb_album_id', 'album_name')
