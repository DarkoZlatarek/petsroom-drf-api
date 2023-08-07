from rest_framework import generics, permissions
from p5_drf_api.permissions import IsOwnerOrReadOnly
from likes.models import Like
from likes.serializers import LikeSerializer


# Class provided by DRF-API walkthrough.
class LikeList(generics.ListCreateAPIView):
    """
    Logged in users is able
    to like/unlike a post.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = LikeSerializer
    queryset = Like.objects.all()

    def perform_create(self, serializer):
        """
        Saves like or unlike to the database,
        if the user is authenticated.
        """
        serializer.save(owner=self.request.user)


# Class provided by DRF-API walkthrough.
class LikeDetail(generics.RetrieveDestroyAPIView):
    """
    The ability to create/delete
    a like.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = LikeSerializer
    queryset = Like.objects.all()
