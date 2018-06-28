"""
Author: harsh
"""

from rest_framework.serializers import ModelSerializer

from website.models import Event, Announcement, BoardMember, Photo


class EventSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'


class AnnouncementSerializer(ModelSerializer):
    class Meta:
        model = Announcement
        fields = '__all__'


class BoardMemberSerializer(ModelSerializer):
    class Meta:
        model = BoardMember
        fields = '__all__'


class PhotoSerializer(ModelSerializer):
    class Meta:
        model = Photo
        fields = '__all__'
