from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Profile
from .serializers import ProfileSerializer


# Class taken from DRF-API walkthrough.
class ProfileList(APIView):
    """
    List all created profiles.
    """
    def get(self, request):
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data)


# Class taken from DRF-API walkthrough.
class ProfileDetail(APIView):
    """
    Retrieve or update Profile fields if Owner.
    """
    def get_object(self, pk):
        try:
            profile = Profile.objects.get(pk=pk)
            return profile
        except Profile.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        profile = self.get_object(pk)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)