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
    like_id = serializers.SerializerMethodField()
    likes_count = serializers.ReadOnlyField()
    comments_count = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        """
        Return correct user.
        """
        request = self.context['request']
        return request.user == obj.owner

    def get_like_id(self, obj):
        """
        Return & calculate total number
        of likes on post view.
        """
        user = self.context['request'].user

        if user.is_authenticated:
            like = Like.objects.filter(
                owner=user,
                post=obj
            ).first()
            return like.id if like else None

        return None

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
            'like_id',
            'likes_count',
            'comments_count',
        ]
