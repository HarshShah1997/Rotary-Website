from rest_framework.generics import ListAPIView

from website.models import Event
from website.serializers import EventSerializer


class EventList(ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
