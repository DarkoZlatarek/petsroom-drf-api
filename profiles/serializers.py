from rest_framework import serializers
from .models import Profile


# Class provided by DRF-API walkthrough.
class ProfileSerializer(serializers.ModelSerializer):
    """
    Profile serializer.
    Providing readability to profile data in API.
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        """
        Lists of Profile model fields to display.
        """
        model = Profile
        fields = [
            'id',
            'owner',
            'created_on',
            'modified_on',
            'name',
            'image',
            'description',
            'place',
        ]
