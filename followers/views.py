from rest_framework import generics, permissions
from p5_drf_api.permissions import IsOwnerOrReadOnly
from .models import Follower
from .serializers import FollowerSerializer


# Class taken from DRF-API walkthrough.
class FollowerList(generics.ListCreateAPIView):
    """
    Allow user to follow another user.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = FollowerSerializer
    queryset = Follower.objects.all()

    def perform_create(self, serializer):
        """
        Follow request is
        saved to the database
        for authenticated users.
        """
        serializer.save(owner=self.request.user)


# Class taken from DRF-API walkthrough.
class FollowerDetail(generics.RetrieveDestroyAPIView):
    """
    Allow a user to follow/unfollow another user.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = FollowerSerializer
    queryset = Follower.objects.all()
