from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from petsroom_drf_api.permissions import IsOwnerOrReadOnly
from .models import EventComment
from .serializers import EventCommentSerializer, EventCommentDetailSerializer


# Class taken from DRF-API walkthrough and modified for Event model.
class EventCommentList(generics.ListCreateAPIView):
    """
    Create & Retrieve event comments.
    """
    serializer_class = EventCommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = EventComment.objects.all()

    filter_backends = [
        DjangoFilterBackend,
    ]

    filterset_fields = [
        'event',
    ]

    def perform_create(self, serializer):
        """
        Saves comments to the database,
        if the user is authenticated.
        """
        serializer.save(owner=self.request.user)


# Class taken from DRF-API walkthrough and modified for Event model.
class EventCommentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete event comment.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = EventCommentDetailSerializer
    queryset = EventComment.objects.all()
