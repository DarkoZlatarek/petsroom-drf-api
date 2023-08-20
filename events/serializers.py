from rest_framework import serializers
from .models import Event


class EventSerializer(serializers.ModelSerializer):
    """
    Serializer for Events model.
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    eventcomments_count = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        """
        Return correct user.
        """
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        """
        Fields to display.
        """
        model = Event
        fields = [
            'id',
            'owner',
            'title',
            'place',
            'content',
            'date',
            'time',
            'created_on',
            'modified_on',
            'is_owner',
            'profile_id',
            'profile_image',
            'eventcomments_count',
        ]
