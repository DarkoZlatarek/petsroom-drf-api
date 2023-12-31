from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import Comment


# Class taken from DRF-API walkthrough.
class CommentSerializer(serializers.ModelSerializer):
    """
    Comment Model serializer.
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    created_on = serializers.SerializerMethodField()
    modified_on = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        """
        Associate comment to user ID.
        """
        request = self.context['request']
        return request.user == obj.owner

    def get_created_on(self, obj):
        """
        Display time passed since the comment created.
        """
        return naturaltime(obj.created_on)

    def get_modified_on(self, obj):
        """
        Display time passed since comment modified.
        """
        return naturaltime(obj.modified_on)

    class Meta:
        """
        Return fields to display.
        """
        model = Comment
        fields = [
            'id',
            'owner',
            'is_owner',
            'profile_id',
            'profile_image',
            'post',
            'created_on',
            'modified_on',
            'content',
        ]


# Class taken from DRF-API walkthrough.
class CommentDetailSerializer(CommentSerializer):
    """
    Serializer for comment detail view.
    """
    post = serializers.ReadOnlyField(source='post.id')
