from django.db import models
from django.contrib.auth.models import User
from posts.models import Post


# Class taken from DRF-API walkthrough.
class Like(models.Model):
    """
    Likes Model.
    Model is related to "Owner" & Posts model.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post,
        related_name='likes',
        on_delete=models.CASCADE
    )
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        Same user can not like the same post twice.
        """
        ordering = ['-created_on']
        unique_together = ['owner', 'post']

    def __str__(self):
        return f'{self.owner} {self.post}'
