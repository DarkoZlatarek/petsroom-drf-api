from django.db import IntegrityError
from rest_framework import serializers
from .models import Follower


# Class taken DRF-API walkthrough.
class FollowerSerializer(serializers.ModelSerializer):
    """
    Serializer for Followers Model.
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    followed_name = serializers.ReadOnlyField(source='followed.username')

    class Meta:
        model = Follower
        fields = [
            'id',
            'owner',
            'created_on',
            'followed',
            'followed_name',
        ]

    def create(self, validated_data):
        """
        A user can not follow another
        user twice.
        """
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError(
                {'detail': 'possible duplicate'}
            )
