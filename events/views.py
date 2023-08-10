from django.db.models import Count
from rest_framework import generics, permissions, filters
from petsroom_drf_api.permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from .models import Event
from .serializers import EventSerializer


class EventList(generics.ListCreateAPIView):
    """
    Retrieve events from database.
    Create new events.
    """
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Event.objects.all()

    filter_backends = [
        filters.SearchFilter,
    ]

    search_fields = [
        'owner__username',
        'title',
        'place',
    ]

    def perform_create(self, serializer):
        """
        Check if user is authenticated.
        """
        serializer.save(owner=self.request.user)


class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, Update and delete events.
    """
    serializer_class = EventSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Event.objects.all()
