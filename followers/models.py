from django.db import models
from django.contrib.auth.models import User


# Class taken from DRF-API walkthrough.
class Follower(models.Model):
    """
    Followers Model.
    Provide the ability for users to
    un/follow other users.
    """
    owner = models.ForeignKey(
        User,
        related_name='following',
        on_delete=models.CASCADE
    )
    followed = models.ForeignKey(
        User,
        related_name='followed',
        on_delete=models.CASCADE
    )
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        The user is unable to follow same
        profile more then once.
        """
        ordering = ['-created_on']
        unique_together = ['owner', 'followed']

    def __str__(self):
        return f'{self.owner} {self.followed}'
