from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import EventComment


# Class taken from DRF-API walkthrough.
class EventCommentSerializer(serializers.ModelSerializer):
    """
    Event comment Model serializer.
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    created_on = serializers.SerializerMethodField()
    modified_on = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        """
        Associate event comment to user ID.
        """
        request = self.context['request']
        return request.user == obj.owner

    def get_created_on(self, obj):
        """
        Display time passed since the event comment created.
        """
        return naturaltime(obj.created_on)

    def get_modified_on(self, obj):
        """
        Display time passed since event comment modified.
        """
        return naturaltime(obj.modified_on)

    class Meta:
        """
        Return fields to display.
        """
        model = EventComment
        fields = [
            'id',
            'owner',
            'is_owner',
            'profile_id',
            'profile_image',
            'event',
            'created_on',
            'modified_on',
            'content',
        ]


# Class taken from DRF-API walkthrough.
class EventCommentDetailSerializer(EventCommentSerializer):
    """
    Serializer for event comment detail view.
    """
    event = serializers.ReadOnlyField(source='event.id')
