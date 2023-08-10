from rest_framework import serializers
from likes.models import Like
from .models import Article


class ArticleSerializer(serializers.ModelSerializer):
    """
    Serializer for Articles model.
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')

    def get_is_owner(self, obj):
        """
        Return correct user.
        """
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        """
        Display fields.
        """
        model = Article
        fields = [
            'id',
            'owner',
            'is_owner',
            'title',
            'content',
            'article_link',
            'created_on',
            'modified_on',
            'profile_id',
            'profile_image',
        ]
